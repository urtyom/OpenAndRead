# from contextlib import redirect_stdout


# cook_book = {
#   'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#   'Утка по-пекински': [
#     {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#     {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#     {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#     {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#   'Запеченный картофель': [
#     {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#     {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#     {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
#   }

# def writing_to_file(cook_book_new):
#   for name in cook_book_new:
#     print(name)
#     print(len(cook_book_new[name]))
#     for rec in cook_book_new[name]:
#       print(f"{rec['ingredient_name']} | "
#             f"{rec['quantity']} | "
#             f"{rec['measure']}")
#     print()

# with open('recipes.txt', 'w', encoding='utf-8') as f:
#   with redirect_stdout(f):
#     writing_to_file(cook_book)

def split_on(file, delimiter = ''):
  with open(file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

  lines_strip = []

  for line in lines:
    lines_strip.append(line.strip())

  splitted_recipes = [[]]
  
  for item in lines_strip:
    if item == delimiter:
      splitted_recipes.append([])
    else:
      splitted_recipes[-1].append(item)
  
  dict_recipes = {}

  for recipe in splitted_recipes:
    for i in recipe[2:]:
      dict_recipes[recipe[0]] = recipe[2:]

  name_list = []
  product_list = []

  for products in dict_recipes:
    c = []
    name_list.append(products)
    for i in dict_recipes[products]:
      b = i.split('|')
      c.append({'ingredient_name': b[0], 'quantity': b[1], 'measure': b[-1]})
    product_list.append(c)

  cook_book = {key: value for key, value in zip(name_list, product_list)}
  return cook_book

print(split_on('recipes.txt'))

# def get_shop_list_by_dishes(dishes, person_count):
#   shop_list_by_dishes = {}
#   for dish in dishes:  
#     for name_dish in cook_book[dish]:
#       if dish in shop_list_by_dishes:
#         shop_list_by_dishes.update(name_dish = {
#           'measure': name_dish['measure'],
#           'quantity': name_dish['quantity'] + 
#           (name_dish['quantity'] * person_count)
#           })
#       else:  
#         shop_list_by_dishes[name_dish['ingredient_name']]= {
#           'measure': name_dish['measure'],
#           'quantity': name_dish['quantity'] * person_count
#           }

# get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

