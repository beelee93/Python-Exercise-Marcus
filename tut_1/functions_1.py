# Think about what the code is trying to do
# Then refactor

number = int(input('Number to square root:'))

iteration1 = (1**2 + number)
iteration1 /= 2 * 1

iteration2 = (iteration1**2 + number)
iteration2 /= 2 * iteration1

iteration3 = (iteration2**2 + number)
iteration3 /= 2 * iteration2

iteration4 = (iteration3**2 + number)
iteration4 /= 2 * iteration3

iteration5 = (iteration4**2 + number)
iteration5 /= 2 * iteration4

print("Square root of %.2f is %.3f" %(number, iteration5))
