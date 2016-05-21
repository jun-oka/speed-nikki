# -*- coding: utf-8 -*-
#cvsから文章を取ってくる
from generate import wakati
import random
import re
import logging

def make_random_text(keyword,text_list):

    #https
    p1 = 'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+'
    #RT
    p2 = '[RQ]T[ ]+?@.+:+'
    #hash
    p3 = '(#|＃).*((RT|rt)|フォロ.?ー|)'
    #返信
    p4 = '@[.]+[ ]'


    message = ""
    for text in text_list:
        tmp = re.sub(p1, "",text)
        tmp2 = re.sub(p2, "",tmp)
        tmp3 = re.sub(p3, "",tmp2)
        tmp4 = re.sub(p4, "",tmp3)

        if keyword not in tmp4:
            pass
        else:
            tmp4 = tmp4 + "。"
            message += tmp4

    #logging
    logging.basicConfig(filename='message.log', level=logging.DEBUG)
    logging.debug(message)
    wordlist = wakati(message)

    # Create table of Markov Chain
    markov = {}
    prev1 = ""
    prev2 = ""
    for word in wordlist:
        if prev1 and prev2:
            if not prev2 in markov:
                markov[prev2] = {}
            if not prev1 in markov[prev2]:
                markov[prev2][prev1] = []
            markov[prev2][prev1].append(word)
        prev2 = prev1
        prev1 = word

    # Generate Sentence
    count = 0
    prev2= random.choice(list(markov.keys()))
    prev1 = random.choice(list(markov[prev2].keys()))
    sentence = prev2 + prev1
    while count < 25:
        tmp = random.choice(markov[prev2][prev1])
        sentence += tmp
        prev2 = prev1
        prev1 = tmp
        count += 1

    strs = ["衝撃！","はろー！","本日は休みー！！", "やっと一息。", "そういえば、", "久しぶりだぁ！", "やっぱり。"]
    random_first_text = random.choice(strs)
    final_sentence = random_first_text + sentence
    print(final_sentence)

if __name__ == '__main__':
    make_random_text("カツラ","a")
