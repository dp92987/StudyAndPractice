# https://www.hackerrank.com/challenges/diagonal-difference/problem

import os


#
# Complete the 'diagonal_difference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
def diagonal_difference(arr, n):
    # Write your code here
    d_1 = d2 = 0
    for i in range(0, n):
        d_1 += arr[i][i]
        d2 += arr[i][n-i-1]
    return abs(d_1-d2)


def main():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonal_difference(arr, n)

    fptr.write(str(result) + '\n')

    fptr.close()


if __name__ == '__main__':
    main()
