# https://school.programmers.co.kr/learn/courses/30/lessons/12931
# 연습문제
# Lv.1
# < 자릿수 더하기 >
# 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
# 예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

### 내가 푼 방법
def solution(n):
    answer = 0

    for i in range(len(str(n))):
        answer += int(str(n)[i])

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer