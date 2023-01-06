## 221028 - Github Advanced

---

#### git status 수시로 확인하기

---

- touch 파일명 : 파일 생성

- git init : 브랜치

- git status : 현재 깃 상태

- git add . : staging area로 올리기

- git rm --cached 파일명 : staging area에서 내리기

- git log : 지금까지 했던 commit 목록을 자세하게 보여준다

- git log --oneline : commit 목록 간단하게

- git log --oneline --all : 모든 목록

- git log --oneline --all --graph

- git commit --amend : 커밋내용 덮어쓰기, (:wq 로 빠져나온다)

- git reset --soft <커밋 id> : 지햣 정한 커밋으로 가고 나머지는 staging area에 있음(commit했던걸 빼고 add한 상태로)

- git reset --mixed <커밋 id> : 지정한 커밋으로 가고 나머지 는 아무것도 안 한상태(add도 안 한 상태)

- git reset --hard <커밋 id> : 지정한 커밋으로 가고 나머지 파일을 삭제
  
  - 실수로 삭제 했을 때 한번 더 사용 하면 되돌리기 가능

- git reflog : 지운 커밋까지 내가 한 모든 커밋을 보여준다

- gi revert <커밋 id> : 데이터를 추가하는 방식으로 코드를 되돌림(추가설명 필요)

---

#### git branch

---

- git branch : 브랜치가 몇개 있는지 확인

- git branch <만들 브랜치 이름> : 브랜치 만들기

- git switch <브랜치 이름> : 헤더 위치 변경

- git branch -d <브랜치 이름> : 브랜치 삭제

- git switch -c <브랜치 이름> : 한번에 브랜치 만들고 헤더위치까지 변경

- git merge <합칠 브랜치 이름> : 기준이 되는 브랜치로 이동 후에 합쳐야 함

---

#### 오픈소스로 개발하기

- git remote add upstream <clone 주소> : 주소 추가

- git remote -v : 리모트 상태 확인

- 머지가 되면 브랜치를 마스터로 옮기기 -> git pull upstream master -> 생성했던 브랜치 삭제(안해도 됨)

- git reflog : 작업내용 확인하기

- git reset HEAD@{1} : 작업 실행 취소하기

- git checkout -- {되돌릴 파일 이름} : 파일 수정 내용 초기화하기
