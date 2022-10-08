
def generate_consecutive_integers(n, arr=[]):
  # Problem - when the function is declared and "initialized", 
  # default parameters are initialized only once, and references do not change 
  # across executions of the function
  for i in range(n):
    arr.append(i)
  return arr

list1 = generate_consecutive_integers(5)
list2 = generate_consecutive_integers(3)

print("List1 =", list1)
print("List2 =", list2)

# Considerations:
#
# All variables are references in Python, ie, they point to a specific memory rather than containing
# the "real" value itself.
#
# arr = [1,2,3]
# arr2 = arr
# # arr and arr2 point to the same array, mutating one will affect another
#
# When writing values literally, ie, [1,2,3], 10, "abc", {'x':1}, we are defining a new memory block to
# contain those values, hence
#
# arr = [1,2,3]
# arr2 = [1,2,3]
# # arr and arr2 point to different arrays
