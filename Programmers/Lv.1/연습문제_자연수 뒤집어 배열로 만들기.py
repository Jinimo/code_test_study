# https://school.programmers.co.kr/learn/courses/30/lessons/12932
# 연습문제
# Lv.1
# < 자연수 뒤집어 배열로 만들기 >
# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 
# 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

### 내가 푼 방법
def solution(n):
    answer = []
    new = str(n)
    for i in range(len(new)):
        answer.append(int(new[-i-1]))
    return answer

## 다른 사람 플이
def digit_reverse(n):
    return list(map(int, reversed(str(n))))