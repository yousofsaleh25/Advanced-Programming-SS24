#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
  # +++your code here+++
  """
  Args:
  s: A string to be modified.
  
  Returns:
  The modified string according to the rules.
  """

  if len(s) < 3: # check the length of the string
    return s
  elif s.endswith("ing"): # check if the string ends with ing
    return s + "ly"
  else:
    return s + "ing"  



# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
  # +++your code here+++
  """
  Args:
  s: The input string.
  
  Returns:
  The modified string with 'not'...'bad' replaced by 'good' if applicable.
  """

  not_inx = s.find("not") # find the first appearance of the word "not", return the "n" index
  bad_inx = s.find("bad") # fint the forst appearance of the word "bad", return the "b" index
  if not_inx != -1 and bad_inx != -1 and bad_inx > not_inx: # check if words "not" and "bad" exists and word "bad" appear after word "not"
    s = s[:not_inx] + "good" + s[bad_inx+3:] # replace the string from word "not" to "bad" with word "good"
  return s # the question only ask about first appearance so we don't mind if it appears many times or not and just the first appearance is considered


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
  # +++your code here+++
  """
  Args:
  a: First input string.
  b: Second input string.

  Returns:
  A new string formed by concatenating the front halves and back halves of both strings.
  """  
  # find the mid index for a and b. The +1 to handle odd lengths by giving the extra char to the front half
  a_mid = (len(a) + 1) // 2 
  b_mid = (len(b) + 1) // 2

  return a[:a_mid] + b[:b_mid] + a[a_mid:] + b[b_mid:]  #  a-front + b-front + a-back + b-back


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print()
  print('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print()
  print('front_back')
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
