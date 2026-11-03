#!/usr/bin/env python3
"""column/<slug>.<code>.md(記事)と column/ui/<code>.json(コラム画面の文言)を照合する。

    python -X utf8 scripts/validate_column.py            # 全部
    python -X utf8 scripts/validate_column.py fr ko      # 指定した言語だけ

検査: 先頭の項目(title / description / date / author)と --- の区切り、言語コード、英語版があること、
脚注の参照と定義が対応していること、サイト内リンクの言語接頭辞(/api を除く)、
ui の鍵が ui/en.json と同じで空でなく HTML が無いこと。問題があれば終了コード 1。
"""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..')
COL = os.path.join(ROOT, 'column')
LANGS = json.load(open(os.path.join(ROOT, 'lang', 'languages.json'), encoding='utf-8'))
UI_SRC = json.load(open(os.path.join(COL, 'ui', 'en.json'), encoding='utf-8'))
NAME = re.compile(r'^([a-z0-9]+(?:-[a-z0-9]+)*)\.([a-z]{2}(?:-[a-z]{2})?)\.md$')
TAG = re.compile(r'</?[a-zA-Z][^>]*>')
REQUIRED = ('title', 'description', 'date', 'author')


def check_article(path, code):
    errs = []
    text = open(path, encoding='utf-8').read()
    head, sep, body = text.partition('\n---\n')
    if not sep:
        return ['no "---" line between the header and the text']
    meta = dict(l.split(':', 1) for l in head.splitlines() if ':' in l)
    meta = {k.strip(): v.strip() for k, v in meta.items()}
    for k in REQUIRED:
        if not meta.get(k):
            errs.append('header has no ' + k)
    if meta.get('date') and not re.fullmatch(r'\d{4}-\d\d-\d\d', meta['date']):
        errs.append('date is not YYYY-MM-DD')
    refs = set(re.findall(r'\[\^([^\]]+)\](?!:)', body))
    defs = set(re.findall(r'^\[\^([^\]]+)\]:', body, re.M))
    if refs - defs:
        errs.append('footnote used but not defined: ' + ', '.join(sorted(refs - defs)))
    if defs - refs:
        errs.append('footnote defined but not used: ' + ', '.join(sorted(defs - refs)))
    pre = '' if code == 'en' else '/' + code
    for href in re.findall(r'\]\((/[^)\s]*)\)', body):
        if href.startswith('/api'):
            continue
        if code != 'en' and not (href == pre + '/' or href.startswith(pre + '/')):
            errs.append('site link without /%s prefix: %s' % (code, href))
    return errs


def check_ui(code):
    p = os.path.join(COL, 'ui', code + '.json')
    if not os.path.exists(p):
        return ['ui/%s.json missing' % code]
    try:
        d = json.load(open(p, encoding='utf-8'))
    except ValueError as e:
        return ['ui/%s.json invalid JSON: %s' % (code, e)]
    errs = []
    if list(d) != list(UI_SRC):
        errs.append('ui/%s.json keys or order differ from ui/en.json' % code)
    for k, v in d.items():
        if not isinstance(v, str) or not v.strip():
            errs.append('ui/%s.json empty or not a string: %s' % (code, k))
        elif TAG.search(v):
            errs.append('ui/%s.json HTML tag in: %s' % (code, k))
    return errs


def main():
    only = set(sys.argv[1:])
    found = {}
    bad = 0
    for f in sorted(os.listdir(COL)):
        if not f.endswith('.md'):
            continue
        m = NAME.match(f)
        if not m or m.group(2) not in LANGS:
            print(f, 'NG\n  file name must be <slug>.<language code>.md'); bad += 1; continue
        found.setdefault(m.group(2), []).append(m.group(1))
    slugs = set(s for v in found.values() for s in v)
    for s in sorted(slugs - set(found.get('en', []))):
        print(s, 'NG\n  no English version (%s.en.md)' % s); bad += 1
    for code in sorted(found):
        if only and code not in only:
            continue
        errs = check_ui(code)
        for s in found[code]:
            errs += ['%s: %s' % (s, e) for e in check_article(os.path.join(COL, '%s.%s.md' % (s, code)), code)]
        print(code, 'ok' if not errs else 'NG\n  ' + '\n  '.join(errs))
        bad += bool(errs)
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
