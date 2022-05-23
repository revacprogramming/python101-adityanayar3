def add(a, b):
  sum=a + b
  return sum


def main():
    a = float(input('Enter a number'))
    b = float(input('Enter a number'))

    c = add(a, b)
    print("Sum:",c)

main()