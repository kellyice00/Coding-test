def solution(n):
    add = []
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            add.append(i)
        answer = sum(add)
    return answer