# Regular Expressions
# https://www.py4e.com/lessons/regex
import re
hand = open('mbox-short.txt')
sum=0
for line in hand:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    if len(x) > 0:
        sum=sum+0
print(sum)