
def add(a, b):
  c=a+b
  return c
    pass  # ...


def output(a, b, sum):
  print('Sum is',sum)
    pass  # ...


def main():
    a, b = input_two_numbers()
    sum = add(a, b)

    output(a, b, sum)


if __name__ == '__main__':
    main()
