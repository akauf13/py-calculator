first = float(input("First number: "))
second = float(input("Second number: "))


total = 0


def run():
  operation = input("Type a to add, s to subtract, m to multiply, d to divide, or e for exponent! ")

  if operation == 'a' or operation == 'A':
      total = first + second
      print(total)

  elif operation == 's' or operation == 'S':
      total = first - second
      print(total)

  elif operation == 'm'or operation == 'M':
      total = first * second
      print(total)

  elif operation == 'd' or operation == 'D':
      total = first / second
      print(total)


run()