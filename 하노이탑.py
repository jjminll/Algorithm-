def hanoi(n, start, end, mid, answer):
    if n == 1:
        answer.append([start, end])
        return
    # 1. n-1개의 원판을 start에서 mid로 이동
    hanoi(n - 1, start, mid, end, answer)
    # 2. 가장 큰 원판을 start에서 end로 이동
    answer.append([start, end])
    # 3. n-1개의 원판을 mid에서 end로 이동
    hanoi(n - 1, mid, end, start, answer)

def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer)
    return answer
