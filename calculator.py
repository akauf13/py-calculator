def run():
  operation = input("Choose your operation. Type a to add, s to subtract, m to multiply, d to divide, e for exponent, or q to quit! ")


  if operation == 'a' or operation == 'A':
      first = float(input("First number: "))
      second = float(input("Second number: "))
      total = first + second
      print(total)
      run()

  elif operation == 's' or operation == 'S':
      first = float(input("First number: "))
      second = float(input("Second number: "))
      total = first - second
      print(total)
      run()

  elif operation == 'm'or operation == 'M':
      first = float(input("First number: "))
      second = float(input("Second number: "))
      total = first * second
      print(total)
      run()

  elif operation == 'd' or operation == 'D':
      first = float(input("First number: "))
      second = float(input("Second number: "))
      total = first / second
      print(total)
      run()

  elif operation == 'e' or operation == 'E':
      first = float(input("First number: "))
      second = float(input("Second number: "))
      total = first ** second
      print(total)
      run()

  elif operation == 'q' or operation == 'Q':
      return

  else:
      run()

run()