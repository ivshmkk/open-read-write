# import json
#
# def read_json(file_path, word_max_len=6, top_words_amt=10):
#     with open('newsafr.json', 'r') as f:
#         data = json.load(f)
#     description_words = []
#
#     for item in data['rss']['channel']['items']:
#         for word in item['description'].split():
#             if len(word) > word_max_len:
#                 description_words.append(word)
#
#     word_freq = {}
#     for word in description_words:
#         if word in word_freq:
#             word_freq[word] += 1
#         else:
#             word_freq[word] = 1
#     sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
#     top_words = [word for word, freq in sorted_words[:top_words_amt]]
#     return top_words

import xml.etree.ElementTree as ET

def read_xml(file_path, word_max_len=6, top_words_amt=10):
    tree = ET.parse(file_path)
    root = tree.getroot()
    description_words = []

    for item in root.iter('description'):
        for word in item.text.split():
            if len(word) > word_max_len:
                description_words.append(word)

    word_freq = {}
    for word in description_words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    top_words = [word for word, freq in sorted_words[:top_words_amt]]
    return top_words



