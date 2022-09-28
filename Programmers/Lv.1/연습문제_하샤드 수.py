# https://school.programmers.co.kr/learn/courses/30/lessons/12947
# 연습문제
# Lv.1
# < 하샤드 수 >
# 양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 
# 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 
# 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

### 내가 푼 방법 (+2)
def solution(x):
    xs = str(x)
    sum = 0
    for i in range(len(xs)):
        sum += int(xs[i])
        
    return x % (sum) == 0

## 다른 사람 플이
def Harshad(n):
    return n % sum([int(c) for c in str(n)]) == 0

