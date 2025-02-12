# Importing Libraries

import re
from collections import Counter
import pandas as pd
import sys

def words(text): return re.findall(r'\w+', text.lower())

# Checking we are getting the supported arguments

if(len(sys.argv) != 3):
    print("Invalid Input")
    sys.exit()
""" 
CSV Supported Format:
word             frequency
word1            frequency1
....             ..........
....             ..........
....             ..........
....             ..........

"""
# Reading the csv file with the help of location
# Reading the csv file and creating a DataFrame from it
a = pd.read_csv(str(sys.argv[1]))

# Sorting the DataFrame with respect to frequency

a = a.sort_values("frequency", ascending = False)

# Resetting the redundant index values

a.reset_index(drop = True, inplace = True)

# Creating a counter with the words

WORDS = Counter(list(a.word))

# Storing the word from CLI into a variable

inp1 = sys.argv[2]

def P(word, N=sum(WORDS.values())): 
    return WORDS[word] / N

def correction(word): 
    return max(candidates(word), key=P)

def candidates(word): 
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

def known(words): 
    return set(w for w in words if w in WORDS)

# Creating different transpose and other methods for calculating the output

def edits1(word):
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)
def edits2(word): 
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

# Outputting 5 different word suggestions by iterating the loop 5 times.

for outputs in range(6):
    temp = (correction(inp1))
    del WORDS[temp]             # Deleting the already outputted  
    print(temp, end = " ")
