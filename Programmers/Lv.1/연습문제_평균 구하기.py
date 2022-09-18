# https://school.programmers.co.kr/learn/courses/30/lessons/12944
# 연습문제
# Lv.1
# < 평균 구하기 >
# 정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.

# 점수: + 1

### 내가 푼 방법
def solution(arr):
    answer = 0

    answer = sum(arr) / len(arr)

    return answer