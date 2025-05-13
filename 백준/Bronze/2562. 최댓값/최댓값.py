import sys

num = list(map(int, sys.stdin.read().split()))
print(max(num))
for i in range (len(num)):
    if num[i] == max(num):
        print(i+1)

    