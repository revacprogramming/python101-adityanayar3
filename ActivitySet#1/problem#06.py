# Loops & Iterators

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        n = int(num)
    except:
        print("Invalid input")
        continue
    if smallest is None or n < smallest:
        smallest = n
    if largest is None or n > largest:
        largest = n

      bv

print("Maximum is", largest)
print("Minimum is", smallest)