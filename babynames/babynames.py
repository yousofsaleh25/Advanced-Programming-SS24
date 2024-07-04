#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  # Open the HTML file and read its content
  with open(filename, 'r', encoding='utf-8') as file:
      content = file.read()

  # Extract the year
  year_match = re.search(r'Popularity in (\d{4})', content)
  year = year_match.group(1)

  # Extract the names and rank numbers
  tuples = re.findall(r'<tr align="right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', content)
  
  # Add the names and rank side by side into a list
  # NOTE if we use dictionary for names and ranks the unique names only will be taken, but I found that there is names valid for male and female and has different ranks,
  # so it's important to not use a dictionary as a solution
  result = []
  for rank, male_name, female_name in tuples:
    result.append(f"{male_name} {rank}")
    result.append(f"{female_name} {rank}")

  # sort the names alpabetically
  result = sorted(result) # There is 1000 rank with 1000 names for male and 1000 names for female, so now the len(result) = 2000
  # insert the year into index 0
  result.insert(0, year)

  return result


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file

  # to run the code over all .html file run the following line command
  # python babynames.py --summaryfile baby1990.html baby1992.html baby1994.html baby1996.html baby1998.html baby2000.html baby2002.html baby2004.html baby2006.html baby2008.html
  # NOTE it's prefered to use file for output because there is too many lines the won't fit in your TERMINAL
  for filename in args:
    names_list = extract_names(filename)
    text_output = '\n'.join(names_list)

    if summary:
      with open(f"{filename.split('.')[0]}_output_names.txt", 'w') as summary_file:
        summary_file.write(text_output)
    else:
      print(text_output)

# to run the code over all .html file run the following line command
# python babynames.py --summaryfile baby1990.html baby1992.html baby1994.html baby1996.html baby1998.html baby2000.html baby2002.html baby2004.html baby2006.html baby2008.html
# NOTE it's prefered to use file for output because there is too many lines the won't fit in your TERMINAL
if __name__ == '__main__':
  main()
