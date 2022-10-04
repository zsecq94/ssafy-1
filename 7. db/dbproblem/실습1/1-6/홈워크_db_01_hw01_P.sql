
CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

-- 1) 데이터 저장 방식이 잘못됐다.
INSERT INTO zoo VALUES 
(5, 180, 210, 'gorilla', 'omnivore');

-- 2) 기존에 만들어 놓은 스키마와 지금 저장하려는 형태가 다르다.
INSERT INTO zoo (rowid, name, eat, weight, age) VALUES
(10,'dolphin', 'carnivore', 210, 3),
(10, 'alligator', 'carnivore', 250, 50);

-- 3) height와 age에도 NULL을 넣어 주어야 한다.
INSERT INTO zoo (name, eat, age) VALUES
('dolphin', 'carnivore', 3);
