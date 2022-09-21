-- https://school.programmers.co.kr/learn/courses/30/lessons/59036

-- < SELECT >
-- 아픈 동물 찾기
-- 동물 보호소에 들어온 동물 중 아픈 동물의 아이디와 이름을 조회하는 SQL 문을 작성해주세요. 
-- 이때 결과는 아이디 순으로 조회해주세요.

--  내가 푼 방법 

-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME  FROM ANIMAL_INS
WHERE INTAKE_CONDITION = 'Sick'

-- 아픈 동물: INTAKE_CONDITION이 Sick인 경우