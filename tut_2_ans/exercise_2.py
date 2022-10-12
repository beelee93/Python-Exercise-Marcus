# Write a program that takes 2 inputs: a number, and a unit (either C or F)
# If user indicates C, then convert the number from Celsius to Fahrenheit
# If user indicates F, then convert the number from Fahrenheit to Celsius
#
# Example:
# 0 C = 32 F
# 32 F = 0 C

amount = float(input('Amount: '))
unit = input('Unit (C/F):')

if unit == 'C':
  converted = amount * 9/5 + 32
  print(f'{amount} C = {converted} F')
elif unit == 'F':
  converted = (amount - 32) * 5/9
  print(f'{amount} F = {converted} C')
else:
  print("Unsupported unit", unit)
