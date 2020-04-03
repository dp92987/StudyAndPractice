def calc_sum_sqr(n):
    sum_sqr = 0
    while n != 0:
        sum_sqr = sum_sqr + (n % 10) ** 2
        n = n // 10
    return sum_sqr


def main():
    n = int(input('n: '))

    sum_sqr = n
    sum_list = []
    while True:
        sum_sqr = calc_sum_sqr(sum_sqr)
        if sum_sqr == 1:
            reult = True
            break
        elif sum_sqr in sum_list:
            reult = False
            break
        else:
            sum_list.append(sum_sqr)

    print(result)
    return result

if __name__ == '__main__':
    main()
