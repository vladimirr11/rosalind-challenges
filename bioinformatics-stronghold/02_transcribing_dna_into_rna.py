file_path = 'C:/Users/user/AppData/Local/Temp/rosalind_rna.txt'
mode = 'r'
encoding = 'UTF-8'

with open(file_path, mode, encoding=encoding) as file:
    seq = file.read()
    seq = seq.replace('T', 'U')

    print(seq)