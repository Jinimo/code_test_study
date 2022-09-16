# https://school.programmers.co.kr/learn/courses/30/lessons/12906


### 내가 푼 풀이
def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1, len(arr)):

        if arr[i - 1] != arr[i]:
            answer.append(arr[i])

    return answer

# Test 1
# Input 〉	[1, 1, 3, 3, 0, 1, 1]
# Expected 〉	[1, 3, 0, 1]
# Result 〉	테스트를 통과하였습니다.
# Test 2
# Input 〉	[4, 4, 4, 3, 3]
# Expected 〉	[4, 3]
# Result 〉	테스트를 통과하였습니다.