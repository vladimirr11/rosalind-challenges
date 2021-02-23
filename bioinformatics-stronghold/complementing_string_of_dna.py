file_path = 'C:/Users/user/AppData/Local/Temp/rosalind_revc.txt'
mode = 'r'

with open(file_path, mode) as file:
    seq = file.read()

    complem_seq = ''

    for n in seq:
        if n == 'A':
            complem_seq += 'T'
        elif n == 'T':
            complem_seq += 'A'
        elif n == 'G':
            complem_seq += 'C'
        elif n == 'C':
            complem_seq += 'G'


rev_compl_seq = complem_seq[::-1]

print(rev_compl_seq)