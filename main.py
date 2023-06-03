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
print(a)
