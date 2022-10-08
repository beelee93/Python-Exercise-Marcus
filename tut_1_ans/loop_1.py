
def find_largest(arr):
  largest = None
  for num in arr:
    if largest is None or num > largest:
      largest = num
  return largest

def find_largest_recursive(arr):
  # Base case
  if len(arr) == 0:
    return None
  if len(arr) == 1:
    return arr[0]

  first = arr[0]
  rest = find_largest_recursive(arr[1:]) # The recursion

  return max(first, rest)

numbers = [1,5,4,6,3,-1,0]

print("Largest number is:", find_largest(numbers))


# Considerations:
#
# 1. For loop or while loop?
# 2. Can this be done recursively?
# 3. Describe the structure of the function.