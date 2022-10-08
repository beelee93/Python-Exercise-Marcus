
# Write a function that
# 1. Takes an integer input from the user
# 2. Sums the digits
# 
# Example:
#   "1463"   -> 14
#   "80912"  -> 20
#

def sum_digits(num):
  total = 0
  while num:
    total += num % 10
    num //= 10
  return total

num = int(input("Number: "))
print("Sum of digits:", sum_digits(num))
