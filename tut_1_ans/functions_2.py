
number = 123

def function_1():
  print("number =", number) # Closest reference is the one defined in global scope

def function_2(number = 456):
  print("number =", number) # Closest reference is the one defined in the parameter (local variable)

def function_3():
  number = 789
  print("number =", number) # References the local variable

def function_4():
  global number # Explicit reference to global variable
  number = 789
  print("number =", number)

print(">> Function 1")
function_1()

print(">> Function 2")
function_2()

print(">> Function 3")
function_3()
function_1()

print(">> Function 4")
function_4()
function_1()
