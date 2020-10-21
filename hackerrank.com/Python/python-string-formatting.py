# https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(number):
    # your code goes here
    for i in range(1, number+1):
        print('{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}'.format(i, width=number.bit_length()))


if __name__ == '__main__':
    i = int(input())
    print_formatted(i)
