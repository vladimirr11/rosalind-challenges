from Bio.Seq import Seq

file_path = 'C:/Users/user/AppData/Local/Temp/rosalind_prot.txt'
mode = 'r'

with open(file_path, mode) as file:
    rna_seq = file.read()
    messenger = Seq(rna_seq)

print(messenger.translate())