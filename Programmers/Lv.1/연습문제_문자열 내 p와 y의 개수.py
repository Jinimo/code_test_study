# https://school.programmers.co.kr/learn/courses/30/lessons/12928
# 연습문제
# Lv.1
# < 약수의 합 >
# 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

### 내가 푼 방법
def solution(s):
    s_new = s.replace("P", "p").replace("Y", "y")
    
    if s_new.count("p") ==  s_new.count("y"):
        answer = True
    else:
        answer = False
    return answer

## 다른 사람 플이
def numPY(s):
    # 함수를 완성하세요
    return s.lower().count('p') == s.lower().count('y')
