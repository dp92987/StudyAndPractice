# https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    new_s = ''
    for c in s:
        if c.islower():
            new_s += c.upper()
        else:
            new_s += c.lower()
    return new_s


def main():
    s = input()
    result = swap_case(s)
    print(result)


if __name__ == '__main__':
    main()
