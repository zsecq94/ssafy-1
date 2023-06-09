# JIRA & GIT

---

## JIRA

---

#### JIRA를 사용하는 이유

- 소프트웨어 개발 프로세스
  
  - 폭포수모델
    
    - 처음부터 끝까지 다 계획하고 실행
  
  - 애자일
    
    - 돌아가는 코드 >> 넘사벽 >> 계획
    
    - 단기간 개발 & 회고 => 점진적 개선
    
    - 변화가 생기면 그때그때 대응 가능
    
    - 스프린트란 일정 기간 동안 우리 팀의 목표

- JIRA 사용 흐름
  
  - 매주 월요일 오전 스크럼 회의를 통해 할 일 논의
  
  - 백로그에 이슈 생성
  
  - 스프린트 생성 후 이슈 이동
  
  - 스프린트 시작!

---

#### 일의 단위

- 에픽
  
  - 완료하기까지 여러번의 스프린트가 요구되는 큰 업무 단위
  
  - ex) 회원관리, 상품목록, 상품상세

- 스토리
  
  - 유저 스토리, 유저의 관점에서 작성된 요구사항
  
  - ex) 유저는 로그인을 할 수 있다.

- 태스크
  
  - 스토리를 완료하기 위해 개발자가 작업해야 하는 단위 작업
  
  - ex) 로그인 Store 구현, User 데이터베이스 설계

- 팀에서 정한 규칙에 따라 사용

---

#### 에픽 생성

- 로드맵 탭에서 에픽 생성

- 로드맥에서 백로그 탭으로 옮겨 이슈 생성, 보통 스토리먼저 생성

- 에픽 연결

- 스토리 포인트란? 일의 난이도를 나타내는지표

- SSAFY에서는 1포인트 = 1시간

- 1일 8포인트, 1주 40포인트 달성해야함

- 최대 4포인트까지 부여 가능

- 이슈 작성을 마치면 스토리, 태스크를 백로그로 옮기기

- 모든 이슈를 옮겼다면, 스프린트 시작!

- 해당 업무담당자는 1명밖에 등록이 안됨으로 번거롭지만 같이 업무를 할 때는 여러번 등록

---

#### 스크럼과 칸반

- 매일 스크럼 진행 시, 칸반 보드를 보면서 진행상황을 공유하고 계획을 수정

- 칸반 보드 사용하기
  
  - InProgress 칸에는 진행 중인 작업 하나만 올려두는 것이 일반적!

---

#### 번다운 차트 확인하기

- 보고서 => 번다운 차트

- 이상적인 번다운 차트는 = 스토리포인트를 점차 줄여나가는 방식

- 백로그에서 스프린트로 이슈를 먼저 이동!!!!

---

## GIT

---

#### Git Flow

- main 브랜치(배포)

- develop 브랜치(개발)

---

#### Merge Request

- git merge <브랜치 이름> 대신 gitlab에 Merge request 버튼으로 생성

- Title: 커밋메세지에 표시된 내용

- Description: 해당 MR에서 개발한 내역, 진행내역

- Assignee: 해당 작업 담당자

- Reviewer: 코드 리뷰 담당자

---

#### MR 충동 피하는 방법

- git commit -m '커밋메세지'

- git merge develop

- git push origin feature

- gitlab에서  MR 생섯
