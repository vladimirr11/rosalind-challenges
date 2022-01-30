file_path = 'C:/Users/user/AppData/Local/Temp/rosalind_ini6.txt'
mode = 'r'

with open(file_path, mode) as file:
    seq = file.read()

my_dict = {}

for w in seq.split():
    if w not in my_dict:
        my_dict[w] = 1
    else:
        my_dict[w] += 1

for k, v in my_dict.items():
    print(f'{k} {v}')