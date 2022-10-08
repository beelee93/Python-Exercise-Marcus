
def has_one(grid):
  # Checks if any of the grid cells have a 1
  found = False
  for row in grid:
    for col in row:
      if col == 1:
        found = True
        break

    if found:
      break

  return found

def count_ones(grid):
  # Count the number of grid cells with a 1
  count = 0
  for row in grid:
    for col in row:
      if col == 1:
        count += 1
  return count

grid = [
  [0,0,0,0],
  [0,1,0,0],
  [0,0,1,0],
  [0,0,0,0],
]

if has_one(grid):
  print("Number of ones in grid:", count_ones(grid))
else:
  print("Grid has no cells with `1`")


# Considerations:
#
# 1. What does a break/continue statement do?
#    Can the answer be rewritten with a continue instead of a break
# 2. How does break/continue behave in a nested loop?
#