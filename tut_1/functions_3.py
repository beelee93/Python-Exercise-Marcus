
def generate_consecutive_integers(n, arr=[]):
  # Generates n consecutive integers into the array `arr`
  for i in range(n):
    arr.append(i)
  return arr

list1 = generate_consecutive_integers(5)
list2 = generate_consecutive_integers(3)

print("List1 =", list1)
print("List2 =", list2)