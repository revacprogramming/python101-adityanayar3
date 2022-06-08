# Regular Expressions
# https://www.py4e.com/lessons/regex
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    if len(x) > 0:
        print(x)