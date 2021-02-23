from Bio import SeqIO

file_path = 'C:/Users/user/AppData/Local/Temp/rosalind_gc-1.txt'
mode = 'r'

max_gc_content = 0
with open(file_path, mode) as file:
    fasta_file = SeqIO.parse(file, 'fasta')

    for fasta_seq in fasta_file:
        rosalind_name, seq = fasta_seq.id, fasta_seq.seq
        
        gc_counter = 0
        nucl_counter = 0
        for i in range(len(seq)):
            nucl_counter += 1

            if seq[i] == 'G':
                gc_counter += 1
            elif seq[i] == 'C':
                gc_counter += 1
        
        gc_content = (gc_counter / nucl_counter) * 100

    if max_gc_content < gc_content:
        rosalind_id = rosalind_name
        max_gc_content = gc_content


print(rosalind_id)
print(max_gc_content)