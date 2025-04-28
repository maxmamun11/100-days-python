import art

def add(n1, n2):
    return n1 + n2
# TODO: Write out the other 3 functions - sumtract, multiply and divdie.
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2  

def divide(n1, n2):
    return n1 / n2



#TODO: Add these 4 functions into a dictionary as the value. Keys = "+", "-", "*", "/"

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide 
}

#TODO: Use the dictionary operations to perform the calculation. multiply 4 * 8

# result = operations["*"](4, 8)
# print(result)

def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("What's the first number?: "))

    while should_accumulate:
    
      for symbol in operations:
        print(symbol)
      operation_symbol = input("Pick an operation from the line above: ")
      num2 = float(input("What's the second number?: "))
      answer = operations[operation_symbol](num1, num2)
      print(f"{num1} {operation_symbol} {num2} = {answer}")

      choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation, or 'exit' to quit: ").lower()

      if choice == "y":
        num1 = answer
      elif choice == "n":
        continue
      elif choice == "exit":
        should_accumulate = False
      else:
        print("Invalid input. Exiting.")
        should_accumulate = False


calculator()

