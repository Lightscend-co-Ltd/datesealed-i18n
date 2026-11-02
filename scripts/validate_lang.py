#!/usr/bin/env python3
"""lang/{code}.json を en.json(原文)と照合する。

    python -X utf8 scripts/validate_lang.py            # 見つかった全言語
    python -X utf8 scripts/validate_lang.py ru ko      # 指定した言語だけ

検査: 鍵の過不足と順序、文字列であること、空でないこと、HTML タグが無いこと、
かなが残っていないこと(ja / zh / zh-tw 以外)、文字種(ru/uk/zh/zh-tw/ko/th/ar/hi は固有の文字を含む)、
英語の文のまま残っていないこと(固有名詞を除く)。問題があれば終了コード 1。
"""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
LANG = os.path.join(HERE, '..', 'lang')
LANGS = json.load(open(os.path.join(LANG, 'languages.json'), encoding='utf-8'))
SRC = json.load(open(os.path.join(LANG, 'en.json'), encoding='utf-8'))
KANA = re.compile(r'[぀-ヿ]')
TAG = re.compile(r'</?[a-zA-Z][^>]*>')
SCRIPT = {'ru': r'[Ѐ-ӿ]', 'uk': r'[Ѐ-ӿ]', 'zh': r'[一-鿿]', 'zh-tw': r'[一-鿿]', 'ko': r'[가-힯]',
          'th': r'[฀-๿]', 'ar': r'[؀-ۿ]', 'hi': r'[ऀ-ॿ]', 'ja': r'[぀-ヿ一-鿿]'}
EN_STOP = {'the', 'and', 'of', 'to', 'is', 'are', 'for', 'with', 'that', 'this', 'you', 'your', 'can', 'it', 'not', 'your'}
# 英語のままでよい鍵(固有名詞・記号だけ)
SAME_OK = {'nav_api', 'a_title', 'c_hash', 'operator'}


def check(code):
    errs = []
    p = os.path.join(LANG, code + '.json')
    if not os.path.exists(p):
        return ['missing file']
    try:
        d = json.load(open(p, encoding='utf-8'))
    except ValueError as e:
        return ['invalid JSON: %s' % e]
    if list(d) != list(SRC):
        miss = [k for k in SRC if k not in d]; extra = [k for k in d if k not in SRC]
        if miss: errs.append('missing keys: %s' % ', '.join(miss[:8]))
        if extra: errs.append('extra keys: %s' % ', '.join(extra[:8]))
        if not miss and not extra: errs.append('key order differs from en.json')
    txt_all = ''
    for k, v in SRC.items():
        w = d.get(k)
        if w is None:
            continue
        if not isinstance(w, str) or not w.strip():
            errs.append('empty or not a string: ' + k); continue
        txt_all += w
        if TAG.search(w): errs.append('HTML tag in: ' + k)
        if code not in ('ja', 'zh', 'zh-tw') and KANA.search(w): errs.append('kana left in: ' + k)
        if code != 'en' and w == v and k not in SAME_OK and len(v) > 12:
            errs.append('untranslated (same as English): ' + k)
        elif code != 'en' and len(v) > 40 and sum(1 for t in re.findall(r'[a-z]+', w.lower()) if t in EN_STOP) >= 3 and code in SCRIPT:
            errs.append('looks English: ' + k)
    sp = SCRIPT.get(code)
    if sp and txt_all and len(re.findall(sp, txt_all)) < 0.3 * len(re.findall(r'\w', txt_all)):
        errs.append('too little %s script' % code)
    return errs


def main():
    codes = sys.argv[1:] or [c for c in LANGS if c != 'en' and os.path.exists(os.path.join(LANG, c + '.json'))]
    bad = 0
    for c in codes:
        if c not in LANGS:
            print(c, 'unknown language code'); bad += 1; continue
        e = check(c)
        print(c, 'ok' if not e else 'NG\n  ' + '\n  '.join(e))
        bad += bool(e)
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
