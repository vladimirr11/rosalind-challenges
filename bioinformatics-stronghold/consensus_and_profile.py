from Bio import SeqIO


def read_fasta_file(file_path, mode):
    """
    """
    sequences = []
    with open(file_path, mode) as file:
        fasta_file = SeqIO.parse(file, 'fasta')

        for fasta_seq in fasta_file:
            sequences.append(fasta_seq.seq)
    
    return sequences


def fill_profile_dict(sequences):
    """
    """
    nucleotide_dict = {
        'A': [],
        'C': [],
        'G': [],
        'T': []
    }

    for col in range(len(sequences[0])):
        a, c, g, t = 0, 0, 0, 0
        for row in range(len(sequences)):
            if sequences[row][col] == 'A':
                a += 1
            elif sequences[row][col] == 'C':
                c += 1
            elif sequences[row][col] == 'G':
                g += 1
            elif sequences[row][col] == 'T':
                t += 1
        
        nucleotide_dict['A'].append(a)
        nucleotide_dict['C'].append(c)
        nucleotide_dict['G'].append(g)
        nucleotide_dict['T'].append(t)

    return nucleotide_dict


def get_consensus_seq(nucl_dict: dict):
    """
    """
    consensus_seq = ''
    lenght_values = [len(v) for v in nucl_dict.values()]

    for idx in range(lenght_values[0]):
        max_num = 0
        nucl = None
        for k, _ in nucl_dict.items():
            if nucl_dict[k][idx] > max_num:
                max_num = nucl_dict[k][idx]
                nucl = k
        consensus_seq += nucl
    
    return consensus_seq


def format_profile(nucl_dict: dict):
    """
    """
    for k, v in nucl_dict.items():
        print(f'{k}: {" ".join(map(str, v))}')


file_path = 'C:/Users/user/AppData/Local/Temp/rosalind_cons.txt'
mode = 'r'

print(get_consensus_seq(fill_profile_dict(read_fasta_file(file_path, mode))))
format_profile(fill_profile_dict(read_fasta_file(file_path, mode)))