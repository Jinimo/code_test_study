-- https://school.programmers.co.kr/learn/courses/30/lessons/59034

-- < SELECT >
-- 모든 레코드 조회하기
-- 동물 보호소에 들어온 모든 동물의 정보를 ANIMAL_ID순으로 회하는 SQL문을 작성해주세요. 

--  내가 푼 방법 

-- 코드를 입력하세요
SELECT*FROM ANIMAL_INS
ORDER BY  ANIMAL_ID ASC 

-- ASC: 오름차순 / DESC: 내림차순
-- ORDER BY 절 -> 항상 SELECT 문 맨 마지막 위치
-- 기본 구조
-- SELECT*FROM table_name
-- ORDER BY column_name (ASC, DESC)