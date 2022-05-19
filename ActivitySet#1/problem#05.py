# Functions
def computepay(h, r):
    if h <= 40:
        p=(h*r)
    elif h > 40:
        p= 40 * r + (h - 40)*1.5*r
    return p

hrs = input("Enter Hours:")
hrs=float(hrs)
rate=input("Enter rate:")
rate=float(rate)
p = computepay(hrs,rate)
print("Pay", p)