import json
import re

text = open('text.txt', 'r', encoding='utf-8').read()
data = text.split('##oyp##')[1:]
_list = []


def double(matched):
    return matched.group(1)


for i in data:
    item = i.split('\t')[1:]
    _list.append({
        'type': re.sub('\s*(.*?)\s*', double, item[0]),
        'topic': item[1],
        'A': item[2],
        'B': item[3],
        'C': item[4],
        'D': item[5],
        'answer': re.sub('\s*(.*?)\s*', double, item[6]),
        'difficulty': re.sub('\s*(.*?)\s*', double, item[7])
    })
json.dump(_list, open('data.json', 'w', encoding='utf-8'), ensure_ascii=False)
