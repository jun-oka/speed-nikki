# -*- coding: utf-8 -*-
from microsofttranslator import Translator

def translate_tag(keyword):
    # enter your application name and key.
    translator = Translator('', '')
    print("日本語タグ:" + translator.translate(keyword, "ja"))
    return(translator.translate(keyword, "ja"))
