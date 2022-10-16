# 8기 Django 라이브 코드

| Day  | Subject                      |
| ---- | ---------------------------- |
| 01   | Django Intro                 |
| 02   | Django Model                 |
| 04   | Django Form                  |
| 05   | Django Authentication System |
| 07   | Django managing staticfiles  |
| 08   | Django REST Framework        |



#### 데이터베이스의 장점
- 운영체제에 관계 없이 어디에서나 쉽게 사용가능
- 이메일이나 메신저를 이용해 간편하게 전송 가능
---
#### 데이터베이스의 단점
- 성능과 보안적 측면에서 한계가 명확
- 대용량 데이터를 다루기에 적합하지 않음
- 데이터를 구조적으로 정리하기에 어려움
- 확장이 불가능한 구조
---
#### RDB(Relational Database) = 관계현 데이터베이스
- 데이터를 테이블, 행, 열 등으로 나누어 구조화 하는 방식
- 자료를 여러 테이블로 나누어서 관리하고, 이 테이블간 관계를 설정해 여러 데이터를 쉽게 조작할 수 있다는 장점이 있음
---

#### 스키마
- 테이블의 구조
- 데이터베이스에서 자료의 구조, 표현 방법, 관게 등 전반적인 명세를 기술한 것
---

#### 테이블
- 필드와 레코드를 사용해 조직된 데이터 요소들의 집합
- 관계라고도 부름
- 필드 = 속성, 컬럼 : 고유한 데이터 형식이 지정됨
- 레코드 = 튜플, 행 : 테이블의 데이터는 레코드에 저장됨

---
#### PK
- 기본 키
- 각 레코드의 고유한 값
-   각각의 데이터를 구분할 수 있는 고윳값
- 기술적으로 다른 항목과 절대로 중복될 수 없는 단일 값(unique)

---
#### SQLite
- 응용 프로그램에 파일 형식을 ㅗ넣어 사용하는 비교적 가벼운 데이터베이스
- 오픈 소스 프로젝트이기 때문에 자유롭게 사용 가능
#### 단점
- 대규모 동시 처리 작업에는 부적합
- 다른 RDMBS에서 지원하는 SQL 기능을 지원하지 않을 수 있음

---
#### SQL 이란
- RDBMS의 데이터를 관리하기 위해 설게된 특수 목적의 프로그래밍 언어
- 데이터베이스와 상호작용하는 방법

---
#### DDL
- create
- drop
- alter

---
#### DML
- insert
- select
- update
- delete

---
#### SQL Syntax
- 모든 SQL문은 SELECT, INSERT, UPDATE 등과 같은 키워드로 시작하고, 하나의 statement는 세미콜론(;)으로 끝남
- SQL 키워드는 대소문자를 구분하지 않음 하지만 대문자로 작성하는 것을 권장

---
#### Data Types 종류
- NULL, INTEGER, REAL, TEXT, BLOB(입력된 그대로 저장된 데이터 덩어리 예시:이미지 데이터)

---
#### Constraints 종류
- NOT NULL, UNIQUE, PROMARY KEY(각 테이블에는 하나으 ㅣ기본 키만 있음), AUTOINCREMENT(사용되지 않은 값이나 이전에 삭제된 행의 값을 재사용하는 것을 방지)

---
## DDL

---
#### CREATE TABLE
```python
CREATE TABLE contacts (
  name TEXT NOT NULL,
  age INTERGER NOT NULL,
  email TEXT NOT NULL UNIQUE
);
```
- 실행하고자 하는 명령문에 커서를 두고 마우스 우측버튼 -> Run Selected Query 선택
- id 컬럼은 직적 정의하지 않으면 자동으로 rowid라는 컬럼으로 만들어짐

---
#### ALTER TABLE
- SQLite의 ALTER TABLE 문을 사용하면 기존 테이블을 다음과 같이 변경할 수 있음
-   Rename a table(ALTER TABLE table_name RENAME TO new_table_name;) : 테이블명 변경
-   Rename a column(ALTER TABLE table_name RENAME COLUMN column_name TO new_column_name;) : 컬럼명 변경
-   Add a new clumn to a table(ALTER TABLE table_name ADD COLUMN column_name;) : 새 컬럼 추가
-   Delete a column(ALTER TABLE table_name DROP COLIMN column_name;) : 컬럼 삭제(컬럼이 다른 부분에서 참조되는 경우 삭제 불가)

---
#### DROP TABLE
- 데이터베이스에서 테이블을 제거
-   DROP TABLE table_name;(존재하지 않는 테이블을 제거하면 SQLite에서 오류가 발생)
-   한 번에 하나으 ㅣ테이블만 삭제할 수 있음
-   실행 취소하거나 복구할 수 없음(각별히 주의)

---
## DML

---
#### SELECT
- SELECT column1, column2 FROM table_name; : 특정 테이블에서 데이터를 조회 FROM절에서 데이터를 가져올 테이블을 지정
- ORDER BY
- DISTINCT
- WHERE
- LIMIT
- LIKE
- GROUP BY
- SELECT first_name, age FROM users; (유저테이블에서 첫번째 이름과 나이를 조회)
- SELECT * FROM usersl (전체 데이터를 조회[*])

---
#### ORDER BY
- SELECT select_list FROM table_name ORDER BY column_1 ASC, column_2 DESC;
- ORDER BY 절은 FROM 절 뒤에 위치함
- ASC : 오름차순(기본 값)
- DESC : 내림차순

---
#### DISTINCT
- SELECT DISTINCT select_list FROM table_name;
- 조회 결과에서 중복된 행을 제거
- DISTINCT 절은 SELECT 에서 선택적으로 사용할 수 있음
- SELECT절 뒤에 나와야함 DISTINCT 뒤에 컬럼 또는 컬럼 목록을 작성
- NULL 값을 중복으로 간주

---
#### WHERE
- select COLUMN_LIST from TABLE_NAME where SERCH_CONDITION;
- SELECT 문 외에도 UPDATE 및 DELETE 문에서 WHERE 절을 사용할 수 있음
- FROM 절 뒤에 작성
- WHERE column_1 = 10
- WHERE column_1 = LIKE 'Ko%'
- WHERE column_1 = IN (1, 2)
- WHERE column_1 = BETWEEN 10 AND 20

---
#### GROUP BY
```python
SELECT column_1, aggregate_function(column_2)
From table_name
GROUP BY column_!, column_2;
```
- 특정 그룹으로 묶인 결과를 생성
- SELECT 문의 FROM 절 뒤에 작성
- AS 키워드를 사용해 컬럼명을 임시로 변경하여 조회할 수 있음

```python
# 인원이 가장 많은 성씨 순으로 조회
SELECT last_name, COUNT(*) FROM users
GROUP BY last_name ORDER BY COUNT(*) DESC;
```
```python
# 각 지역별 평균 나이 조회하기
SELECT country, AVG(age) FROM users
GROUP BY country;
```

---
#### INSERT
- 먼저 INSERT INTO 키워드 뒤에 데이터를 삽입할 테이블의 이름을 지정
- 테이블 이름 뒤에 쉼표로 구분된 컬럼 목록을 추가
- VALUES 키워드 뒤에 쉼표로 구분된 값 목록을 추가(만약 컬럼 목록을 생략하는 경우 값 목록의 모든 컬럼에 대한 값을 지정해야 함)
```python
INSERT INTO classmates (name, age, address)
VALUES ('홍길동', 23, '서울');
```
```python
INSERT INTO classmates
VALUES ('홍길동', 23, '서울');
```
- 여러 행 삽입하기
```python
INSERT INTO classmates
VALUES
  ('김철수', 30, '경기'),
  ('김철수', 30, '경기'),
  ('김철수', 30, '경기'),
  ('김철수', 30, '경기'),
  ('김철수', 30, '경기');
```

---
#### UPDATE
- 테이블에 있는 기존 행의 데이터를 업데이트
- UPDATE 절 이후에 업데이트할 테이블을 지정
- SET 절에서 테이블의 각 컬렁메 대해 새 값을 설정
- WHERE 절의 조건을 사용하여 업데이트할 행을 지정(선택사항이며, 생략하면 테이블의 모든 행에 있는 데이터를 업데이트 함)
```python
UPDATE classmates
# 2번 데이터의 이름과 주소를 수정하기
SET name='김철수한무두루미',
    address='제주도'
WHERE rowid = 2;
```

---
#### DELETE
- 한행, 여러행 및 모든 행을 삭제할 수 있음
- DELETE FROM 키워드 뒤에 행을 제거하려는 테이블의 이름을 지정
- WHERE 절에 검색 조건을 추가하여 제거할 행을 식별(생략하면 테이블의 모든 행을 삭제)
```python
# 5번 데이터 삭제하기
DELETE FROM classmates WHERE rowid = 5;
```
```python
# 이름에 '영'이 포함되는 데이터 삭제하기
DELETE FROM classmates WHERE name LIKE '%영%';
```
```python
# 테이블의 모든 데이터 삭제하기
DELETE FROM classmates;
```

