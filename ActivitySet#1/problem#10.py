# Dictionaries
filename = "dataset/mbox-short.txt"
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
mail=dict{}
for line in handle:
    if not line.startswith("From"):
        continue
    word=line.split()
    email=word[1]
    if email in mail:
        mail[email]=1+mail[email]
    else:
        mail.update({email:1})



