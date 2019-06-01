# lost-in-translation

A script to send a sentence multiple times through Google Translator

This project uses the Google Cloud Translate Python API.

## Preparation:

You need a [Google Cloud Platform account](https://cloud.google.com/docs/overview/) to use this.

```
$ git clone https://github.com/felsenhower/lost-in-translation.git
$ cd lost-in-translation
$ python -m venv --system-site-packages .venv
$ . .venv/bin/activate
$ pip install --user google-cloud-translate
$ ./lost-in-translation.py
```

For more info on the Google Cloud Translate API, visit the [pypy page](https://pypi.org/project/google-cloud-translate/) and the [Google Cloud Translate Python API documentation](https://cloud.google.com/translate/docs/reference/libraries#client-libraries-install-python)

## Usage:

```
Usage: ./lost-in-translation.py <input> <languages> <iterations>
  <input> must be a sentence as a string. Don't forget to quote!
          The language of the sentence will be automatically determined.
  <languages> must be a comma-separated list. If a language occurs twice,
              that step will be ignored.
  <iterations> must be an integer. If a cycle of translations gets
               detected during translation, the process will be
               prematurely terminated.
  Example: ./lost-in-translation.py 'This is a test.' 'ja,zh,de' '2' will translate the text in the following manner:
           en -> ja -> zh -> de -> en -> ja -> zh -> de -> en
```

## Example output:

```
$ ./lost-in-translation.py 'The fabulous lost-in-translation will be beautifully demonstrated by this stupid example!' \
'de,zh,nl,ja' 2
Iteration #1
[en -> de]: Das fabelhafte Lost-in-Translation wird durch dieses blöde Beispiel wunderbar demonstriert!

[de -> zh]: 这个愚蠢的例子精美地展示了神话般的迷失翻译！

[zh -> nl]: Dit stomme voorbeeld toont prachtig de mythische verloren vertaling!

[nl -> ja]: このばかげた例は、神話上の失われた翻訳を美しく見せています！

[ja -> en]: This ridiculous example shows the mythical lost translation beautifully!

Iteration #2
[en -> de]: Dieses lächerliche Beispiel zeigt die mythische verlorene Übersetzung wunderschön!

[de -> zh]: 这个荒谬的例子表明神话失落的翻译很漂亮！

[zh -> nl]: Dit belachelijke voorbeeld laat zien dat de vertaling van mythologie prachtig is!

[nl -> ja]: このばかげた例は、神話の翻訳が美しいことを示しています！

[ja -> en]: This ridiculous example shows that mythic translation is beautiful!


Input:
The fabulous lost-in-translation will be beautifully demonstrated by this stupid example!

Output
This ridiculous example shows that mythic translation is beautiful!
```

## Authors:
- [Ruben Felgenhauer](https://github.com/felsenhower)
- [Leonhard Reichenbach](https://github.com/Zehvogel)
