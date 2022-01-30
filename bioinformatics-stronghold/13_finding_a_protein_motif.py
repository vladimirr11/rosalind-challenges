from urllib.request import urlopen
from collections import OrderedDict
import re

BASE_UNIPROT_URL = 'http://www.uniprot.org/uniprot/'

rosalind_local_file_path = 'C:\\Users\\user\\AppData\\Local\\Temp\\' + 'rosalind_mprt-1.txt'
glycosylation_pattern = r'N[^P][ST][^P]'


def read_uniprot_fasta_file_from_url(access_numner, base_url):
    """
    """
    fasta_url = base_url + access_numner + '.fasta'
    response = urlopen(fasta_url)
    fasta = response.read().decode('utf-8', 'ignore')

    return fasta


def make_glycolisation_pattern_dict(local_file_path: str, uni_prot_url: str, glyco_pattern: str):
    """
    """
    glyco_pattern_dict = OrderedDict()

    with open(local_file_path, 'r') as file:
        for access_num in file:

        # for access_num in ['A2Z669', 'B5ZC00', 'P07204_TRBM_HUMAN', 'P20840_SAG1_YEAST']:
            fasta_seq = read_uniprot_fasta_file_from_url(access_num.strip(), uni_prot_url)

            _, *prot_seq = fasta_seq.split('\n')

            protein_seq = ''.join(prot_seq)
            for idx in range(0, len(protein_seq)):
                if re.match(glyco_pattern, protein_seq[idx: idx + 4]):
                    glyco_pattern_dict.setdefault(access_num.strip(), []).append(idx + 1)

    return glyco_pattern_dict


def print_result_in_required_format(glycosylation_pattern_dict: OrderedDict):
    """
    """
    for (k, v) in glycosylation_pattern_dict.items():
        print(k)
        print(' '.join(list(map(str, v))))


glyco_dict = make_glycolisation_pattern_dict(rosalind_local_file_path, BASE_UNIPROT_URL, glycosylation_pattern)

print_result_in_required_format(glyco_dict)
