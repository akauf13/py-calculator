# first = float(input("First number: "))
# second = float(input("Second number: "))

def run():
  operation = input("Type a to add, s to subtract, m to multiply, d to divide, e for exponent, or q to quit! ")
  first = float(input("First number: "))
  second = float(input("Second number: "))

  if operation == 'a' or operation == 'A':
      total = first + second
      print(total)
      run()

  elif operation == 's' or operation == 'S':
      total = first - second
      print(total)
      run()

  elif operation == 'm'or operation == 'M':
      total = first * second
      print(total)
      run()

  elif operation == 'd' or operation == 'D':
      total = first / second
      print(total)
      run()

  elif operation == 'e' or operation == 'E':
      total = first ** second
      print(total)
      run()

  elif operation == 'q' or operation == 'Q':
      return

  else:
      run()

run()