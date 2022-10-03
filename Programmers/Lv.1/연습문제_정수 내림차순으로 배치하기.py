# https://school.programmers.co.kr/learn/courses/30/lessons/12933
# 연습문제
# Lv.1
# < 정수 내림차순으로 배치하기>
# 함수 solution은 정수 n을 매개변수로 입력받습니다. 
# n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 
# 예를들어 n이 118372면 873211을 리턴하면 됩니다.

### 내가 푼 방법 (+1)
def solution(n):
    sort = sorted(str(n), reverse=True) #list
    new = ''
    for i in sort:
        new += i 
    return int(new)

## 다른 사람 풀이
def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))