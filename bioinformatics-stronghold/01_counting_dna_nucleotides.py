file_path = 'C:/Users/user/AppData/Local/Temp/rosalind_dna.txt'
mode = 'r'
encoding = 'UTF-8'

A, C, G, T = 0, 0, 0, 0

with open(file_path, mode, encoding=encoding) as file:
    seq = file.read()

    for idx in range(len(seq)):
        if seq[idx] == 'A':
            A += 1
        elif seq[idx] == 'C':
            C += 1
        elif seq[idx] == 'G':
            G += 1
        elif seq[idx] == 'T':
            T += 1


print(A, C, G, T)