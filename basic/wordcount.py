57#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys
import string
# +++your code here+++

# To run the code open the terminal window and change the directory where the code and .txt files placed then run the following 
# -- python wordcount.py --topcount "alice.txt" or -- python wordcount.py --count "alice.txt"


# this function takes a filename and read it and split it into words
def read_file_into_words(filename):
  """
  Reads the content of a file, converts it to lowercase, and splits it into words.

  Parameters:
  filename (str): The path to the file to be read.

  Returns:
  list: A list of words from the file, all in lowercase.
  """

  # open the file and read it's content
  with open(filename, 'r') as file:
    content  = file.read()

  words = content.strip().lower().split() # convert the content into lowercase, then split it into words based on space separator and sort them
  return words

# this function takes a list of words and count them and return a dictionary with numbers
# it counts the punctuations also as mentioned in the criteria
def count_words(words):
  """
  Counts the occurrences of each word and punctuation character in a list of words.

  Parameters:
  words (list): A list of words (strings).

  Returns:
  dict: A dictionary where keys are words and punctuation characters, and values are their counts.
  """
  count_dict = {}
  punctuation_chars = string.punctuation # List of punctuation characters

  # count the words and the punctuations
  for word in words:
    
    # count the punctuations, if we don't need to count the punctuations we can comment this part
    for char in word:
      if char in punctuation_chars:
        if char not in count_dict.keys():
          count_dict[char] = 1
        else:
          count_dict[char] += 1

    # count the words after removing the punctuations
    new_word = ''.join(char for char in word if char not in punctuation_chars)
    if len(new_word) == 0: continue   # this condition will happen if the entire word was just a punctuations, so the new_word becomes empty
    if new_word not in count_dict.keys():
      count_dict[new_word] = 1
    else:
      count_dict[new_word] += 1

  return count_dict


def print_words(filename):
  """
  Reads a file, counts the occurrences of each word and punctuation character,
  sorts the results alphabetically, and prints the counts.

  Parameters:
  filename (str): The name of the file to read and process.
  """
  words = read_file_into_words(filename)
  count_dict = count_words(words)
  count_dict = sorted(count_dict.items(), key= lambda x: x[0]) # sort the words alphabetically 
  print(dict(count_dict))

def print_top(filename):
  """
  Reads a file, counts the occurrences of each word and punctuation character,
  sorts the results by frequency in descending order, and prints the top 20 most frequent items.

  Parameters:
  filename (str): The name of the file to read and process.
  """
  words = read_file_into_words(filename)
  count_dict = count_words(words)
  count_dict = sorted(count_dict.items(), key= lambda x: x[1], reverse=True)[:20] # sort the words based in it's number of appearance in the file, and take only the top 20 word
  print(dict(count_dict))
  
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
