# https://www.hackerrank.com/challenges/simple-array-sum/problem

import os


#
# Complete the simpleArraySum function below.
#
def simple_array_sum(array):
    #
    # Write your code here.
    #
    return sum(array)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simple_array_sum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
