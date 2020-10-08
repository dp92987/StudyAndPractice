# https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring_loop(string, sub_string):
    counter = 0
    n = 0
    for i in range(len(string)-len(sub_string)+1):
        print(string[n:len(sub_string)+n], sub_string)
        if string[n:len(sub_string)+n] == sub_string:
            counter += 1
        n += 1
    return counter


def count_substring(string, sub_string, counter=0):
    if string[:len(sub_string)] == sub_string:
        counter += 1
    if len(string) == len(sub_string):
        return counter
    else:
        return count_substring(string[1:], sub_string, counter)


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)