# https://school.programmers.co.kr/learn/courses/30/lessons/12928
# 연습문제
# Lv.1
# < 약수의 합 >
# 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

### 내가 푼 방법
def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if (n % i) == 0:
            answer += i

    return answer
