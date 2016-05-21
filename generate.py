# -*- coding: utf-8 -*-
import os
import sys
import random
import MeCab

def wakati(text):
    t = MeCab.Tagger("-Ochasen")
    t.parse('')  # これを追記！
    node = t.parseToNode(text)

    result = []
    while node:
        #noun=node.feature.split(",")[0]
        word = str(node.surface)
        result.append(word)
        node=node.next
    return result

if __name__ == "__main__":
    filename = "random_text.txt"
    src = open(filename, "r").read()
    wordlist = wakati(src)

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
    print(markov)
    prev2= random.choice(list(markov.keys()))
    prev1 = random.choice(list(markov[prev2].keys()))
    sentence = prev2 + prev1
    while count < 20:
        tmp = random.choice(markov[prev2][prev1])
        sentence += tmp
        prev2 = prev1
        prev1 = tmp
        count += 1

    #print(sentence)
