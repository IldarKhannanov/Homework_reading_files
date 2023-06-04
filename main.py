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





