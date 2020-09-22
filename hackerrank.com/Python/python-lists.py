# https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        choice = input().split()
        action = choice[0]
        if action == 'insert':
            arr.insert(int(choice[1]), int(choice[2]))
        elif action == 'print':
            print(arr)
        elif action == 'remove':
            arr.remove(int(choice[1]))
        elif action == 'append':
            arr.append(int(choice[1]))
        elif action == 'sort':
            arr.sort()
        elif action == 'pop':
            arr.pop()
        elif action == 'reverse':
            arr.reverse()
