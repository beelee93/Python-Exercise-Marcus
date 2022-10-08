
def get_next_iteration(prev_value, number_to_sqrt):
  return (prev_value**2 + number_to_sqrt) / 2 / prev_value

number = int(input('Number to square root:'))

iteration1 = get_next_iteration(1, number)
iteration2 = get_next_iteration(iteration1, number)
iteration3 = get_next_iteration(iteration2, number)
iteration4 = get_next_iteration(iteration3, number)
iteration5 = get_next_iteration(iteration4, number)

print("Square root of %.2f is %.3f" %(number, iteration5))

# Considerations:
#
# 1. How do you shave off more lines of code?
# 2. Extra: Why does this method work in calculating the square root?
#