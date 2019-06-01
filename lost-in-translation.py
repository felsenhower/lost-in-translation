#!/usr/bin/env python3

from google.cloud import translate
import sys
import html

def translate_text(text, src_lang, trgt_lang):
    client = translate.Client(target_language=trgt_lang)
    tl = client.translate(text, source_language=src_lang)
    return html.unescape(tl['translatedText'])

def detect_lang(text):
    client = translate.Client()
    return client.detect_language([text])[0]["language"]

def get_languages():
    client = translate.Client()
    return set(map(lambda l: l["language"], client.get_languages()))

def translate_cycles(text, languages, iterations):
    detected_language = detect_lang(text)
    languages = [detected_language] + languages + [detected_language]
    dict = { detected_language : set(text) }
    cycle_detected = False
    for i in range(iterations):
        print("Iteration #{}".format(i+1), file=sys.stderr)
        for j in range(len(languages)-1):
            src_lang = languages[j]
            trgt_lang = languages[j+1]
            if (src_lang == trgt_lang):
                continue
            text = translate_text(text, src_lang, trgt_lang)
            print("[{} -> {}]: {}".format(src_lang, trgt_lang, text), file=sys.stderr)
            print("", file=sys.stderr)
            if not trgt_lang in dict:
                dict[trgt_lang] = set()
            if text in dict[trgt_lang]:
                cycle_detected = True
            else:
                dict[trgt_lang].add(text)
        if cycle_detected:
            return text
    return text

def usage():
    print("Usage: {} <input> <languages> <iterations>".format(sys.argv[0]), file=sys.stderr)
    print("  <input> must be a sentence as a string. Don't forget to quote!", file=sys.stderr)
    print("          The language of the sentence will be automatically determined.", file=sys.stderr)
    print("  <languages> must be a comma-separated list. If a language occurs twice,", file=sys.stderr)
    print("              that step will be ignored.", file=sys.stderr)
    print("  <iterations> must be an integer. If a cycle of translations gets", file=sys.stderr)
    print("               detected during translation, the process will be", file=sys.stderr)
    print("               prematurely terminated.", file=sys.stderr)
    print("  Example: {} '{}' '{}' '{}' will translate the text in the following manner:".format(
          sys.argv[0],
          "This is a test.",
          "ja,zh,de",
          "2"
    ), file=sys.stderr)
    print("           en -> ja -> zh -> de -> en -> ja -> zh -> de -> en", file=sys.stderr)
    sys.exit(1)

if len(sys.argv) != 4:
    usage()

input = sys.argv[1]
languages = [l.strip() for l in sys.argv[2].split(",")]
iterations = int(sys.argv[3])

supported_langs = get_languages()
for l in languages:
    if not l in supported_langs:
        print("Unsupported language '{}' given!".format(l), file=sys.stderr)
        print("", file=sys.stderr)
        usage()

result = translate_cycles(input, languages, iterations)

print("", file=sys.stderr)
print("Input:", file=sys.stderr)
print(input, file=sys.stderr)
print("", file=sys.stderr)
print("Output", file=sys.stderr, flush=True)
print(result, flush=True)
