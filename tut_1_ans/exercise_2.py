
# Write a program that will calculate the mean test scores for a group of students
# 1. Keeps prompting the user for a name and their test score
# 2. If user types nothing, that ends the prompting and begins the calculations
# 3. Print the mean score, and the names of students whose scores at least the mean
#
# Example:
#   "Tim"
#   "80"
#   "Joseph"
#   "60"
#   "Andy"
#   "40"
#   ""
#   --> Mean: 60, Students with scores >= 60: Tim, Joseph
#

def get_scores_dict():
  scores_dict = {}
  while True:
    name = input("Name of student (type 'end' to stop): ")
    if not name:
      break

    score = float(input("Test score of %s: " % name))
    scores_dict[name] = score
  return scores_dict

def calculate_mean(scores_dict):
  total = sum(scores_dict.values())
  return total / len(scores_dict)

def get_students_above_score(scores_dict, lower_bound):
  return [n for n,s in scores_dict.items() if s >= lower_bound]

scores_dict = get_scores_dict()
if len(scores_dict) == 0:
  print("No scores to compute")
else:
  mean = calculate_mean(scores_dict)
  students_above_mean = get_students_above_score(scores_dict, mean)

  print("Mean:", mean, "Students with scores >=", mean, ":", students_above_mean)
