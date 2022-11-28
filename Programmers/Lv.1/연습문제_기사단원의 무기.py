# https://school.programmers.co.kr/learn/courses/30/lessons/136798
# 연습문제
# Lv.1
# < 기사단원의 무기 >
# 기사단원의 수를 나타내는 정수 number와 이웃나라와 협약으로 정해진 공격력의 제한수치를 나타내는 정수 limit와 제한수치를 초과한 기사가 사용할 무기의 공격력을 나타내는 정수 power가 주어졌을 때, 
# 무기점의 주인이 무기를 모두 만들기 위해 필요한 철의 무게를 return 하는 solution 함수를 완성하시오.

# 점수: + 14

### 내가 푼 방법


def solution(number, limit, power):
    answer = 0
    for n in range(1, number+1):
        divisor = 0 # 약수 
        for i in  range(1, int(n ** 0.5) + 1):
            if (n % i == 0): # 약수라면
                divisor += 1

                if i ** 2 != n: 
                    divisor += 1

        if (divisor>limit): 
            divisor = power

        answer +=divisor

    return answer