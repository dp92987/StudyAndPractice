# https://leetcode.com/problems/reverse-integer/

class SolutionV1:
    def reverse(self, x: int) -> int:
        if abs(x) > 2**31:
            return 0
        else:
            x_str = str(x)
            if x_str[0] in ['+', '-']:
                sign = -1
                x_str = x_str[1:]
            else:
                sign = 1
            x_str_rev = x_str[::-1]
            x_rev = int(x_str_rev)
            return sign * x_rev


class SolutionV2:
    def reverse(self, x: int) -> int:

        def len_int(x):
            n = abs(x)
            len_int = 0
            while n != 0:
                n = n // 10
                len_int += 1
            return len_int

        n = abs(x)
        sign = -1 if x < 0 else 1
        n_rev = 0
        n_len = len_int(n)
        for index in range(n_len - 1, -1, -1):
            # n_rev = n_rev + (n // abs(n)) * (abs(n) % 10) * (10 ** index)
            # n = (n // abs(n)) * (abs(n) // 10)
            n_rev = n_rev + (n % 10) * (10 ** index)
            if n_rev > 2**31:
                return 0
            n = n // 10
        return sign * n_rev


x = int(input('x: '))

x_rev = SolutionV2()
print(x_rev.reverse(x))
