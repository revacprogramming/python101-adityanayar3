# Strings

text = "X-DSPAM-Confidence:    0.8475"
p= text.find(':')
c=text[p+1:]
f=float(c)
print(f)