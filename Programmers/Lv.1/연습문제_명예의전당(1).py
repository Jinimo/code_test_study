# https://school.programmers.co.kr/learn/courses/30/lessons/138477
# 연습문제
# Lv.1
# < 명예의전당(1) >
# 명예의 전당 목록의 점수의 개수 k, 1일부터 마지막 날까지 출연한 가수들의 점수인 score가 주어졌을 때, 매일 발표된 명예의 전당의 최하위 점수를 return하는 solution 함수를 완성해주세요.

# 점수: + 9

### 내가 푼 방법
def solution(k, score):
    answer = []

    for i in range(len(score)):
        answer.append(min(sorted(score[:i+1], reverse=True)[:k]))

    return answer