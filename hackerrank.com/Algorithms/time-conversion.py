# https://www.hackerrank.com/challenges/time-conversion/problem

import os


#
# Complete the timeConversion function below.
#
def time_conversion(s):
    period = s[-2:]
    h = s[:2]
    if period == 'PM' and h != '12':
        return '{}:{}'.format(int(h)+12, s[3:-2])
    elif period == 'AM' and h == '12':
        return '00:{}'.format(s[3:-2])
    else:
        return s[:-2]


def main():
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = time_conversion(s)

    f.write(result + '\n')

    f.close()


if __name__ == '__main__':
    main()
