# Write a function called `diff` that determines the first index when two list differ
# If the lists are the same, then return -1
# Example: 
#   [1,2,3], [1,2,4]    -> 2
#   [5,1], [5,1]        -> -1
#   [0,6,7], [0,6,7,8]  -> 3 (differ by the presence of the 4th element)
#   [0,6,7], [0,0,7,8]  -> 1

def diff(list1, list2):
  if len(list1) == len(list2):
    # Trivial case, just go thru each element and compare
    for index in range(len(list1)):
      if list1[index] != list2[index]:
        return index
    
    # No different element
    return -1

  # Non-trivial case, we loop up to the end of the smaller list
  different_index = 0
  smallest_len = min(len(list1), len(list2))

  while different_index < smallest_len:
    if list1[different_index] != list2[different_index]:
      break
    different_index += 1
  
  return different_index
