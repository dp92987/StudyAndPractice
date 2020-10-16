# https://www.hackerrank.com/challenges/designer-door-mat/problem

height, width = map(int, input().split())

for i in range(1, height, 2):
    print(('.|.'*i).center(width, '-'))

print('WELCOME'.center(width, '-'))

for i in range(height-2, -1, -2):
    print(('.|.' * i).center(width, '-'))
