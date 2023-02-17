CREATE TABLE users (
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL
);

--순서
SELECT DISTINCT
FROM
WHERE
GROUP BY
ORDER BY
LIMIT
OFFSET


--조회 기본 구조
SELECT first_name, age FROM users;

--전체 데이터 조회
SELECT * FROM users;

--rowid 조회
SELECT rowid, first_name FROM users;

--ORDER BY 조회
SELECT first_name, age FROM users
ORDER BY age ASC;

SELECT first_name, age FROM users
ORDER BY age DESC;

SELECT first_name, age, balance FROM users
ORDER BY age ASC, balance DESC;

--중복 없이 조회(DISTINCT)
SELECT DISTINCT country  FROM users;

SELECT DISTINCT country FROM users
ORDER BY country;

SELECT DISTINCT first_name, country FROM users;

SELECT DISTINCT first_name, country FROM users
ORDER BY country DESC;

--WHERE절 추가해서 조회
SELECT first_name, age, balance FROM users
WHERE age >= 30;

SELECT first_name, age, balance FROM users
WHERE age >= 30 AND balance > 500000;

--LIKE절 추가해서 조회
SELECT first_name, last_name FROM users
where first_name LIKE '%호%';

SELECT first_name, last_name FROM users
where first_name LIKE '%준';

SELECT first_name, phone FROM users
WHERE phone LIKE '02-%';

SELECT first_name, age FROM users
WHERE age LIKE '2_';

SELECT first_name, phone FROM users
WHERE phone LIKE '%-51__-%';

--IN
SELECT first_name, country FROM users
WHERE country NOT IN ('경기도', '강원도');

--BETWEEN
SELECT first_name, age FROM users
WHERE age NOT BETWEEN 20 AND 30;

--LIMIT
SELECT rowid, first_name FROM users
LIMIT 10;

SELECT first_name, balance FROM users
ORDER BY balance DESC
LIMIT 10;

SELECT first_name, age FROM users
ORDER BY age
LIMIT 5;

--OFFSET
SELECT rowid, first_name, balance FROM users
LIMIT 10 OFFSET 10; --10부터(OFFSET) 10개(LIMIT)

--GROUP BY
SELECT country, COUNT(*) FROM users
GROUP BY country;

--Aggregate function
SELECT COUNT(*) FROM users;

SELECT AVG(age) FROM users
WHERE age > 30;