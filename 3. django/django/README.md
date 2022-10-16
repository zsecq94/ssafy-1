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
#### CREATE TABLE
```python
CREATE TABLE contacts (
  name TEXT NOT NULL,
  age INTERGER NOT NULL,
  email TEXT NOT NULL UNIQUE
);
```
