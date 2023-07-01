from contextlib import redirect_stdout


cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }

def writing_to_file(cook_book_new):
  for name in cook_book_new:
    print(name)
    print(len(cook_book_new[name]))
    for rec in cook_book_new[name]:
      print(f"{rec['ingredient_name']} | "
            f"{rec['quantity']} | "
            f"{rec['measure']}")
    print()

with (open('список рецептов из основного файла.txt', 'w', encoding='utf-8')
      as f):
  with redirect_stdout(f):
    writing_to_file(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
  shop_list_by_dishes = {}
  for dish in dishes:  
    for name_dish in cook_book[dish]:
      if dish in shop_list_by_dishes:
        shop_list_by_dishes.update(name_dish = {
          'measure': name_dish['measure'],
          'quantity': name_dish['quantity'] + 
          (name_dish['quantity'] * person_count)
          })
      else:  
        shop_list_by_dishes[name_dish['ingredient_name']]= {
          'measure': name_dish['measure'],
          'quantity': name_dish['quantity'] * person_count
          }

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

