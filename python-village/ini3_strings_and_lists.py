file_path = 'C:/Users/user/AppData/Local/Temp/rosalind_ini1.txt'
mode = 'r'

with open(file_path, mode) as file:
    seq = file.read()

idx1 = int(input())
idx2 = int(input())
idx3 = int(input())
idx4 = int(input())

f_w = seq[idx1:idx2 + 1]
s_w = seq[idx3:idx4 + 1]

print(f'{f_w} {s_w}')