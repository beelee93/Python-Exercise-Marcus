
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
  return None

name = input('Name of student: ')
print('Test score for %s is %d' % (name, get_test_score(name)))
