--테이블 생성
CREATE TABLE contacts (
  name TEXT NOT NULL,
  age INTERGER NOT NULL,
  email TEXT NOT NULL UNIQUE
);

--수정1
ALTER TABLE contacts
RENAME TO new_contacts;

--수정2
ALTER TABLE new_contacts
RENAME COLUMN name TO last_name;

--추가
ALTER TABLE new_contacts 
ADD COLUMN address TEXT NOT NULL;

--컬럼 삭제
ALTER TABLE new_contacts
DROP COLUMN address;

--테이블 삭제
DROP TABLE new_contacts;