from contextlib import redirect_stdout


with open('1.txt', 'r', encoding='utf-8') as f1:
  lines_1 = f1.readlines()
  lines_1_strip = []
  for line_1 in lines_1:
    lines_1_strip.append(line_1.strip())

with open('2.txt', 'r', encoding='utf-8') as f2:
  lines_2 = f2.readlines()
  lines_2_strip = []
  for line_2 in lines_2:
    lines_2_strip.append(line_2.strip())

list_all = []

list_all.append([len(lines_1), '1.txt', lines_1_strip])
list_all.append([len(lines_2), '2.txt', lines_2_strip])

def union_txt(list_all_txt):
  sorted(list_all_txt, key=lambda x: x[0])
  for name in list_all_txt:
    print(f'{name[1]}\n{name[0]}')
    for string_txt in name[2]:
      print(string_txt)

with (open('объединенный.txt', 'w', encoding='utf-8') as f3):
  with redirect_stdout(f3):
    union_txt(list_all)
