#coding:utf-8
from GetTagFromImage import RecognizeImage
from TranslateEnToJa import translate_tag
from GetMessageFromTw import  GerMessageFromTw
from RandomTextGereration import make_random_text
import sys

if __name__ == '__main__':
    param = sys.argv
    #タグ取得
    img_path = param[1]
    capture = RecognizeImage()
    keyword = capture.recognize_captcha(img_path)
    #翻訳
    keyword_ja = translate_tag(keyword)
    #ツイート取得
    text_list = GerMessageFromTw(keyword_ja)
    make_random_text(keyword_ja, text_list)
