# Regular Expressions
# https://www.py4e.com/lessons/regex
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

count = {}
for line in handle:
    word = line.split()
    if len(word) < 3 or word[0] != "From" : continue
    time = word[5]
    hour = time.split(":")
    hour = str(hour[:1])
    hour = hour[2:4]
    if hour in count :
        count[hour] = 1 + count[hour]
    else :
        count.update({hour:1})
l = list()
for i, j in count.items():
    value = (i, j)
    l.append(value)
 
l = sorted(l)    
for i, j in l:
    print(i,j)