import sys
count = 0
total = int(input())
num_list = list(map(int, sys.stdin.readline().split()))
find = int(input())

for i in range (len(num_list)):
    if num_list[i]== find:
        count +=1
print(count)