-- https://school.programmers.co.kr/learn/courses/30/lessons/59035

-- < SELECT >
-- 역순 정렬하기
-- 동물 보호소에 들어온 모든 동물의 이름과 보호 시작일을 조회하는 SQL문을 작성해주세요. 
-- 이때 결과는 ANIMAL_ID 역순으로 보여주세요.

--  내가 푼 방법 

-- 코드를 입력하세요
SELECT NAME,  DATETIME FROM ANIMAL_INS
ORDER BY ANIMAL_ID DESC -- 내림차순 

-- ASC: 오름차순 / DESC: 내림차순
-- ORDER BY 절 -> 항상 SELECT 문 맨 마지막 위치
-- 기본 구조
-- SELECT*FROM table_name
-- ORDER BY column_name (ASC, DESC)