file_path = 'C:/Users/user/AppData/Local/Temp/rosalind_hamm-1.txt'
mode = 'r'

with open(file_path, mode) as file:
    sequences = file.readlines()

seq_to_compare = [seq for seq in sequences]

hamming_distance = 0
s, t = seq_to_compare[0], seq_to_compare[1]

for n in range(len(s)):
    if s[n] != t[n]:
        hamming_distance += 1

# def calc_hamming_distance(s, t):
#     """
#     """
#     return len(list(filter(lambda pair: pair[0] != pair[1], zip(list(s), list(t)))))

# print(calc_hamming_distance(s, t))

print(hamming_distance)