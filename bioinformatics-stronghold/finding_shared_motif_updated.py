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


def find_min_lenght_seq(seqs: list):
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


def find_subseq(target: str, seqs: list):
    """
    """
    for seq in seqs:
        if target not in seq:
            return
    else:
        return True


def find_all_subseq(shortest_seq: str, seqs: list):
    """
    """
    subseqs = []
    for i in range(len(shortest_seq)):
        for j in range(len(shortest_seq) - 1, i, -1):
            if find_subseq(shortest_seq[i:j], seqs):
                subseqs.append(shortest_seq[i:j])

    return subseqs


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


print(find_the_longest_subseq(find_all_subseq(shortest_seq, sequences)))

print(f'Running time: {time() - start:.2f}')