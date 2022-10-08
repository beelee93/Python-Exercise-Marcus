
TEST_SCORES = {
  'Jerry': 80,
  'Bob': 76,
  'Alice': 86,
  'Matt': 77,
  'Jerome': 90,
  'Samantha': 85,
}

def get_test_score(student_name):
  # Gets the score based on the TEST_SCORES
  if student_name in TEST_SCORES:
    return TEST_SCORES[student_name]

  return 0

name = input('Name of student: ')
print('Test score for %s is %d' % (name, get_test_score(name)))

# Considerations:
#
# 1. How do you handle the situation when the name does not exist in the dictionary?
# 2. Is the name case-sensitive?
#
