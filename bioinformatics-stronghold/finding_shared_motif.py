from Bio import SeqIO
from sys import maxsize
from time import time

start = time()

file_path = 'C:/Users/user/AppData/Local/Temp/rosalind_lcsm.txt'
mode = 'r'

sequences = []
with open(file_path, mode) as file:
    fasta_file = SeqIO.parse(file, 'fasta')
    for seq in fasta_file:
        sequences.append(seq.seq)


def find_min_lenght_seq(seqs):
    """
    """
    MIN_LEN = maxsize
    min_lenght_seq = ''
    for seq in seqs:
        if len(seq) < MIN_LEN:
            MIN_LEN = len(seq)
            min_lenght_seq = seq
    
    return min_lenght_seq


shortest_seq = find_min_lenght_seq(sequences)
sequences.remove(shortest_seq)


def find_all_subseqs(seqs: list):
    """
    """
    longest_subseqs = []
    for i in range(len(shortest_seq)):
        for j in range(1, len(shortest_seq)):
            for seq in seqs:
                if shortest_seq[i:j] not in seq:
                    break
            else:
                longest_subseqs.append(shortest_seq[i:j])
    
    return longest_subseqs


all_subseqs = find_all_subseqs(sequences)


def find_the_longest_subseq(all_subseqs: list):
    """
    """
    max_lenght_seq = 0
    longest_seq = ''
    for seq in all_subseqs:
        if len(seq) > max_lenght_seq:
            max_lenght_seq = len(seq)
            longest_seq = seq
    
    return longest_seq


print(find_the_longest_subseq(all_subseqs))

stop = time()

print(f'Running time: {stop - start:.2f}')