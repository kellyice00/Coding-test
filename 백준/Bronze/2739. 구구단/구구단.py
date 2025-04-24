N = int(input())

answer = 0

for i in range(1, 10):
    answer = N*i
    print('%d * %d = %d' %(N, i, answer))
    