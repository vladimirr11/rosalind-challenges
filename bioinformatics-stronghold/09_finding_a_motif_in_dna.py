file_path = 'C:/Users/user/AppData/Local/Temp/rosalind_subs-1.txt'
mode = 'r'

with open(file_path, mode) as file:
    s, t = file.read().split()
    
for i in range(0, len(s) - len(t)):
    if s[i:i + len(t)] == t:
        print(i + 1, end = ' ')