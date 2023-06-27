import re

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pymorphy2
from telethon.tl.types import PeerChannel


def get_first_sentence(text):
    text_replace = text.replace('!', '.').replace('?', '.')
    sentences = text_replace.split('. ')
    first_sentence = sentences[0]
    return first_sentence


def check_verb(word):
    morph = pymorphy2.MorphAnalyzer()
    p = morph.parse(word)[0]
    return 'VERB' in p.tag or 'INFN' in p.tag


def get_first_verb(text):
    sentence = text.split(' ')
    for word in sentence:
        if word.endswith(',') or word.endswith(':') or word.endswith(';'):
            word = word[:-1]
        if check_verb(word):
            return word
    return sentence[0]


def check_link(link):
    pattern = r'(https?://(?:www\.)?t\.me/[^\s]+)'
    return re.search(pattern, link)


def save_figure(x, y, chanel_name):
    x = np.array(x)
    y = np.array(y)
    matplotlib.rc('font', family='Arial')
    #matplotlib.rcParams['font.family'] = 'monospace'
    plt.title(f'статистика по {chanel_name}')
    plt.xlabel('посты')
    plt.ylabel('максимальное кол-во реакции на пост')
    plt.plot(x, y, marker='o')
    plt.savefig('saved_figure.png')


def check_is_dight(link):
    if link.isdigit():
        return PeerChannel(int(link))
    return link
