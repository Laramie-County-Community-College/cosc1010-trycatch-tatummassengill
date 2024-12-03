isError = True
num1 = 11

while isError == True and num1 > 10:
  try:
    num1 = int(input("Enter a whole number less than 10"))
    isError = False

    if num1 > 10:
      print("You must enter a number less than 10")
      isError = True  
  
  except ValueError:
    print("You must enter a whole number.")
    
  
# What data type is the isError variable?
  # Answer

# What is the purpose of the isError variable?
  # Answer

# Give two example of input that would trigger the except code.  
  # Answer

# Give an example of input that would trigger the 'You must enter a number less than 10' error message.
  # Answer