import argparse
import re
import sys
from tqdm import tqdm
import time

"""A palindrome is a word, phrase, number or other sequence of units that
can be read the same way in either direction. E.g. the word level, the number 1234321, the
phrase Step on no pets.
Write a Python program, that reads a text file and searches for all palindromes in this file. The
program should write all found palindromes (except phrases), together with their multiplicity to
an output file. Handle all strings case insensitive, i.e. the word Level is also a palindrome. Both
input and output files should be specified as command line arguments. Copy some arbitrary text
(e.g. from the internet) and apply your program to it.

References:
https://docs.python.org/3.7/library/argparse.html
https://docs.python.org/3.7/library/re.html
"""

def getArgs():
    """Get arguments from terminal."""

    parser = argparse.ArgumentParser(description='It searches for all palindromes in the file.')
    parser.add_argument('infile', type=argparse.FileType('r'),
                   help='A file with a text to search for palindromes.')
    parser.add_argument('-o', '--outfile', type=argparse.FileType('w'), default=sys.stdout,
                    help='Output file to save all palindromes found (default: print on terminal)')
    
    return parser.parse_args()

def hyphenated(word):
    """Test if it is a hyphenated word"""

    found = False # True when find a symbol
    word_corrected = ""
    first = True # symbols in the first position
    for letter in word:        
        if letter.isalnum():
            word_corrected += letter
            found = False
            first = False        
        else:
            if found:
                return word_corrected[:-1]
            if first:
                continue
            word_corrected += letter
            found = True
            first = False
    else:
        if found:
            return word_corrected[:-1]    
        
    return word_corrected

def searchPalindromes(args):
    """Search for palindromes in the text file."""

    text = args.infile.read()
    words = text.split()
    palindromes = []    
    
    for word in tqdm(words, ascii=True, desc="Searching for palindromes"):
        print(word)
        word = hyphenated(word)
        print(word)
        input()
        if len(word) > 1:
            reverse = word[::-1]
            if word == reverse:
                palindromes.append(word)

    return palindromes

def writeFile(palindromes, args):
    """Write all palindromes found to an output file."""

    if len(palindromes) == 0:
        print("\nPalindrome not found\n")
        return ""

    print("\n------------------")
    args.outfile.write("\n".join(palindromes))
    print("\n------------------\n")


if __name__ == "__main__":
    start_time = time.time()
    args = getArgs()
    palindromes = searchPalindromes(args)
    writeFile(palindromes, args)
    print("--- %s seconds ---" % (time.time() - start_time))