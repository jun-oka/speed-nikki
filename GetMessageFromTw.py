# coding: utf-8
from twitter import *
from twkey import twkey
import json
import logging

CONSUMER_KEY = twkey['cons_key']
CONSUMER_SECRET = twkey['cons_sec']
ACCESS_TOKEN_KEY = twkey['accto_key']
ACCESS_TOKEN_SECRET = twkey['accto_sec']


def GerMessageFromTw(keyword):
    # Twitterへの接続
    t = Twitter(auth=OAuth(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

    # 検索する
    apiresults = t.search.tweets(q=keyword.encode("utf-8"), lang="ja", result_type="recent", count=30)
    encode_results_data = json.dumps(apiresults)
    decode_json_data = json.loads(encode_results_data)

    text_list = []

    for k,v in decode_json_data.items():
        if k == "statuses":
            for contents in v:
                text_list.append(contents['text'])
    #print(text_list)
    return(text_list)

if __name__ == '__main__':
    GerMessageFromTw("カツラ")
