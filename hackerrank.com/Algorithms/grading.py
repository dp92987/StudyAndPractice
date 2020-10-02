# https://www.hackerrank.com/challenges/grading/problem

import os


#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#
def grading_students(grades):
    # Write your code here
    return [grade + 5 - grade % 5 if grade >= 38 and grade % 5 >= 3 else grade for grade in grades]


def main():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = grading_students(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


if __name__ == '__main__':
    main()
