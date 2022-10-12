# Write a program such that, given a user input (a number), draw a triangle of *
#
# Example:
# Input: 3
# Output:
# *
# **
# ***
#
# Input: 2
# Output: 
# *
# **

size = int(input('Size of triangle: '))

for level in range(size):
  print('*' * (level+1))
