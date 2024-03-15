import os

path = 'C:\\Users\\Иван\\Desktop\\open-read-write\\files_txt'
txt_list = []
for file in os.listdir(path):
    if file.endswith('.txt'):
        txt_list.append(file)

f_dict = {}
for file in txt_list:
    with open(os.path.join(path, file), 'r', encoding='utf-8') as f:
        lines = f.readlines()
        f_dict[file] = len(lines), lines
f_dict_sort = dict(sorted(f_dict.items(), key=lambda x: x[1]))
# print(f_dict_sort)
with open('4res.txt', 'w', encoding='utf-8') as f4:
    for file, value in f_dict_sort.items():
        f4.write(file + '\n')
        f4.write(str(value[0]) + '\n')
        for line in value[1]:
            f4.write(line)
        f4.write('\n')
git init