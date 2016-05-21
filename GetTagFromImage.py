#!/usr/bin/python
#coding:utf-8
import base64
import json
from requests import Request, Session
import logging

# Cloud Vision APIで画像を分析
class RecognizeImage():

    def __init__(self):
        return

    # CAPTCHAの分析
    def recognize_captcha(self, str_image_path):
        # CAPTCHA画像の読み込み
        bin_captcha = open(str_image_path, 'rb').read()

        # base64でCAPTCHA画像をエンコード
        str_encode_file = base64.b64encode(bin_captcha).decode()

        # APIのURLを指定
        str_url = "https://vision.googleapis.com/v1/images:annotate?key="

        # 事前に取得したAPIキー
        str_api_key = ""

        # Content-TypeをJSONに設定
        str_headers = {'Content-Type': 'application/json'}

        # Cloud Vision APIの仕様に沿ってJSONのペイロードを定義。
        # CAPTCHA画像からテキストを抽出するため、typeは「TEXT_DETECTION」にする。
        str_json_data = {
            'requests': [
                {
                    'image': {
                        'content': str_encode_file
                    },
                    'features': [
                        {
                            'type': "LABEL_DETECTION",
                            'maxResults': 10
                        }
                    ]
                }
            ]
        }

        # リクエスト送信
        obj_session = Session()
        obj_request = Request("POST",
                              str_url + str_api_key,
                              data=json.dumps(str_json_data),
                              headers=str_headers
                              )
        obj_prepped = obj_session.prepare_request(obj_request)
        obj_response = obj_session.send(obj_prepped,
                                        verify=True,
                                        timeout=60
                                        )

        # 分析結果の取得
        if obj_response.status_code == 200:
            #logging
            logging.basicConfig(filename='example.log', level=logging.DEBUG)
            logging.debug(obj_response.text)
            #1番目のみを取得
            obj = obj_response.text
            keywords = json.loads(obj)
            keyword = keywords['responses'][0]['labelAnnotations'][0]['description']
            print("Tag:" + keyword)
            return(keyword)
        else:
            return "error"

if __name__ == '__main__':
    test = RecognizeImage()
    path = './aircraft.jpg'
    test.recognize_captcha(path)
