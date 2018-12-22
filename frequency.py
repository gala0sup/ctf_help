from collections import Counter
from string import ascii_lowercase

with open('ciphertext', 'r') as f:
    ciphertext = f.read()
    '''
    chiphertext=""
    '''

charcount = Counter(c for c in ciphertext if c in ascii_lowercase)
total_chars = sum(charcount.values())
for char, count in charcount.items():
    print(f'{char}: {(count*100)/total_chars}% ({count})')
