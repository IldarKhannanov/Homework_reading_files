with open('recipes.txt', 'r', encoding = 'utf-8') as f:
    cook_book = {}
    for recipe in f:
        ingridient_count = int(f.readline())
        ingridient_list = []
        for ingridient in range(ingridient_count):
            ingridient_name, quantity, measure = f.readline().strip().split(' | ')
            ingridient_list.append({
                'ingridient_name': ingridient_name,
                'quantity': quantity,
                'measure': measure
            })
        f.readline()
        cook_book[recipe.strip()] = ingridient_list

import json

a = json.dumps(cook_book, indent=2, ensure_ascii=False)

def get_shop_list_by_dishes(person_count: int, dishes: list):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['ingridient_name'] in result:
                    result[consist['ingridient_name']]['quantity'] += consist['quantity'] * person_count
                else:
                    result[consist['ingridient_name']] = {'measure': consist['measure'],'quantity': (consist['quantity'] * person_count)}
        else:
            print('This dish is not in the cook book')
    print(result)
get_shop_list_by_dishes(2, ['Запеченный картофель', 'Омлет'])


import os

name = os.path.basename(r'1.txt')
print(name)
from pprint import pprint
text_1 = '1.txt'
text_2 = '2.txt'
text_3 = '3.txt'

import os.path


files = [text_1, text_2, text_3]
for file in files:
    with open(file, 'r', encoding='utf-8') as file:
        name = os.path.basename(str(file))
        pprint(name)
        print(len(file.readlines()))

with open ('1.txt', encoding = 'utf-8') as f1,\
        open('2.txt', encoding = 'utf-8') as f2,\
        open('3.txt', encoding = 'utf-8') as f3:
    text1 = f1.readlines()
    text1.insert(0, os.path.basename(r'C:\Users\Ильдар\Desktop\homework_read_files\1.txt'))
    text2 = f2.readlines()
    text2.insert(0, os.path.basename(r'C:\Users\Ильдар\Desktop\homework_read_files\2.txt'))
    text3 = f3.readlines()
    text3.insert(0, os.path.basename(r'C:\Users\Ильдар\Desktop\homework_read_files\3.txt'))

with open('4.txt', 'w', encoding = 'utf-8') as f4:
    text4 = [text1, text2, text3]
    text4.sort(key=len)
    for text in text4:
        f4.write(text[0])
        f4.write('\n')
        f4.write(str(len(text[1:])))
        f4.write('\n')
        f4.writelines(text[1:])

