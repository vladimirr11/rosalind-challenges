file_path = 'C:/Users/user/AppData/Local/Temp/rosalind_ini5.txt'
mode = 'r'

with open(file_path, mode, encoding='utf-8') as file:
    text = file.readlines()
    for idx, line in enumerate(text):
        if idx % 2 != 0:
            print(line.rstrip('\r\n'))