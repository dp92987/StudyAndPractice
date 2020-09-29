# https://www.hackerrank.com/challenges/mini-max-sum/problem

# Complete the miniMaxSum function below.
def mini_max_sum(arr):
    sorted_arr = sorted(arr)
    return sum(sorted_arr[0:4]), sum(sorted_arr[4:0:-1])


def main():
    arr = list(map(int, input().rstrip().split()))

    print(*mini_max_sum(arr))


if __name__ == '__main__':
    main()
