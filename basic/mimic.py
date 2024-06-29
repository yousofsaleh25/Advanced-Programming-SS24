#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys

## To run the program you should change the directory in the terminal window to be where the code "mimic.py" and text "small.txt" are
## the directory in my computer is 'C:\Users\Dell\Documents\GitHub\Advanced-Programming-SS24\basic>'
## Then run the following    -- python mimic.py "small.txt" --

def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it."""
  # +++your code here+++
  """
  Args: 
  filename: the .txt file to be read

  Returns: 
  dictionary mapping each word to a list of all the words that immediately follow that word in the file.
  """

  ## Open the file and read it's content
  with open(filename, 'r', encoding='utf-8') as file:
    content = file.read()
  
  # split the text into words depending on the space seperator
  words = content.split()
  mimic_dict = {}

  # mapping each word to a list of all the words that immediately follow that word in the file and the first word is mapped based on emtpy string "" as a key
  prev_word = ""
  for word in words:
    if prev_word not in mimic_dict.keys():
      mimic_dict[prev_word] = [word]
    else:
      mimic_dict[prev_word].append(word)
    prev_word = word

  return mimic_dict


def print_mimic(mimic_dict, word):
  """Given mimic dict and start word, prints 200 random words."""
  # +++your code here+++
  """
  Args:
  mimic_dict: The dictionary returned by mimic_dict() function.
  word: The starting word for generating random text.
  """
  line_lenght = 0   # count the number of character at each line
  for _ in range(200):

    print(word, end=' ')
    
    line_lenght += len(word) + 1
    if line_lenght >= 70: # linebreaks around 70 columns, so the output looks better.
      print() # print a new line
      line_lenght = 0 # Count again starting from 0 for the next line

    next_words = mimic_dict.get(word, mimic_dict[""]) # get the list of words that immediately following the given word and if the word is not exist as a key return default value which the first word in the string ""
    word = random.choice(next_words) # obtain ramdom word from the list of words

  print()


# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print('usage: ./mimic.py file-to-read')
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


if __name__ == '__main__':
  main()
