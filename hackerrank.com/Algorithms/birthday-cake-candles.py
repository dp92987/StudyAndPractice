# https://www.hackerrank.com/challenges/birthday-cake-candles/problem

import os


#
# Complete the 'birthday_cake_candles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#
def birthday_cake_candles(candles):
    # Write your code here
    return candles.count(max(candles))


def main():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthday_cake_candles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


if __name__ == '__main__':
    main()
