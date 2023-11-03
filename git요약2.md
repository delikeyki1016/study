## branch 
* branch 목록 조회.. 
* \>git branch
* 새로운 브랜치 만들기
* 브랜치를 만들기 위해서는 최소한 하나의 commit 은 가지고 있어야 한다. 
* \>git branch dev1
  
* branch 이동.. 
* \>git switch dev1
  
* 모든 브랜치의 커밋 로그
* \>git log --oneline --graph --all
    
* 병합 (merge)
* \>git merge dev2
  
* 브랜치 삭제..
* \>git branch -d dev2
  
* 브랜치간의 비교
* \>git diff main dev1
  
* commit 객체간의 비교
* \>git diff hash hash


## tag, 개발자가 원하는 커밋 객체에 추가하는 일종의 별칭.. 이 별칭으로 커밋 객체를 식별할 수 있다.
* \>git tag v1.0.0

* tag 목록 보기
* \>git tag

* 태그로 reset 도 가능.. 식별역할
* \>git reset --hard tag
  
## remote
* 원격 저장소 정보(url + 인증)
* remote 조회..
* \>git remote

* remote 등록
* \>git remote add test1 https://xxx.com

* url 까지 조회하려면
* \>git remote -v

* remote 삭제
* \>git remote rm test1


## github 인증키 발급
* 프사 -> settings -> developer setting -> personal access tokens -> tokens -> generate new token

* 완성된 url 을 remote 로 등록..

## push
* local commit 정보를 github 에 업로드..
* \>git push -u origin main
* main 브랜치의 내용을 origin remote 에 올리겠다.. -u 는 최초에 한번만 줘도 되고.. 

* 브랜치 명 명시해서 해당 브랜치만 올린다.
* \>git push -u origin dev
* 만약 모든 브랜치의 내용을 한꺼번에 올리겠다면.. 
* \>git push -u origin --all


## pull
* \>git pull origin main

## fetch
* pull 은 remote 의 내용을 다운로드 개념이고..
* fetch 는 remote 의 정보를 가져와서.. local 과 비교후(diff) 후에.. 받을것인지를 판단하는 방법
* fetch 를 하면 remote 내용이 별도의 branch 로 저장이된다..
* main 과 remote 브랜치를 비교해서.. 반영하려면 merge 시켜 사용하는 방법이다.
* \>git fetch origin main
* 아직 반영은 되지 않는다..

* \>git branch -r
* 원격지의 내용의 브랜치까지 확인

* 로컬 브랜치와, 원격지 브랜치를 비교
* \>git diff main origin/main

* 반영하려면.. merge
* \>git merge origin/main

## clone
* \>git clone url