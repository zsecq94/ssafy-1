# 8기 Django 라이브 코드

| Day  | Subject                      |
| ---- | ---------------------------- |
| 01   | Django Intro                 |
| 02   | Django Model                 |
| 04   | Django Form                  |
| 05   | Django Authentication System |
| 07   | Django managing staticfiles  |
| 08   | Django REST Framework        |


## N:1
---
#### 1:1
- One-to-one relationships
- 한 테이블의 레코드 하나가 다른 테이블의 레코드 단 한 개와 관련된 경우
#### N:1
- Many-to-one relationships
- 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 경우
- 여러 개의 주문 입장에서 각각 어떤 주문에 속해 있는지 표현해야 하므로 고객 테이블의 PK를 주문 테이블에 FK로 집어 넣어 관계를 표현
- 고객(1)은 여러 주문(N)을 진행할 수 있음

---
#### Foreign Key
- 외래 키
- 다른 테이블의 행을 식별할 수 있는 키
- 키를 사용하여 부모 테이블의 유일한 값을 참조(by 참조 무결성)
- 외래 키의 값이 반드시 부모 테이블의 기본 키 일 필요는 없지만 유일한 값이어야 함
```python
ForeignKey(to, on_delete, **options)
```
- 2개의 필수 위치 인자가 필요 (to = 참조하는 model class, on_delete옵션)
- on_delete옵션 중 CASCADE : 부모 객체가 삭제 됐을 때 이를 참조하는 객체도 삭제

---
#### 데이터 무결성
- 데이터의 정확성과 일관성을 유지하고 보증하는 것
- 개체 무결성
- 참조 무결성
- 범위 무결성






