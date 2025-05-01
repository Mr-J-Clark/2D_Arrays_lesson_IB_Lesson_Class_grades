#
#
# Task/*A teacher has decided to use a 2D array to store the marks for one of their classes.
# The grade book takes the following form:
# Mark book
#
#            Test 1  Test 2    Test 3    Test 4     Test 5
#
# Student A   67%	50%	93%	83%	43%
# Student B   70%	52%	96%	85%	48%
# Student C   90%	81%	100%	93%	68%
# Student D   55%	32%	71%	72%	58%
# Student E   60%	47%	65%	74%	61%
# Convert the above into a suitable 2D array then write code to determine the following
# Determine the overall average mark (everything)
# Determine the average mark for each individual student
# Determine the average mark for each individual assessment (e.g. test 1)
# Given the following grade cutoffs, determine the grade for each student: A = 85%, B = 70%, C = 55%, D = 40%, F < 40%


# 2D array for the mark book: each row is a student, each column a test
mark_book = [
    [67, 50, 93, 83, 43],   # Student A
    [70, 52, 96, 85, 48],   # Student B
    [90, 81, 100, 93, 68],  # Student C
    [55, 32, 71, 72, 58],   # Student D
    [60, 47, 65, 74, 61]    # Student E
]

student_names = ["Student A", "Student B", "Student C", "Student D", "Student E"]
num_students = len(mark_book)
num_tests = len(mark_book[0])

# 1. Determine the overall average mark
total_marks = sum(sum(student) for student in mark_book)
total_entries = num_students * num_tests
overall_average = total_marks / total_entries
print(f"Overall average mark: {overall_average:.2f}%")

# 2. Determine the average mark for each student
print("\nAverage mark per student:")
for i in range(num_students):
    student_average = sum(mark_book[i]) / num_tests
    print(f"{student_names[i]}: {student_average:.2f}%")

# 3. Determine the average mark for each assessment
print("\nAverage mark per test:")
for test_index in range(num_tests):
    test_total = sum(mark_book[student_index][test_index] for student_index in range(num_students))
    test_average = test_total / num_students
    print(f"Test {test_index + 1}: {test_average:.2f}%")

# 4. Determine the grade for each student
def get_grade(score):
    if score >= 85:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 55:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"

print("\nGrades:")
for i in range(num_students):
    student_average = sum(mark_book[i]) / num_tests
    grade = get_grade(student_average)
    print(f"{student_names[i]}: {grade}")

