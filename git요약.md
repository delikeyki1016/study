## 설치후 확인

* 버전 확인
* \>git --version

## git repository 폴더 초기화..
* 작업폴더에서 명령어 입력.. 
* \>git init

* git 명령어 도움말을 보고자 한다면.. 
* \>git help add
* \>git add --help
* \>git add -h

## git 상태 파악 및 add, commit
* 임의 신규 파일을 만들고.. 
* \>git status

* add
* \>git add a.txt
* \>git add *.txt
* 모든 파일을 명시할때 * 과 . 을 사용 가능
* 둘에 차이는 있다. .으로 시작하는 파일 포함이냐는 차이.. 
* . 은 포함시킨다..
* \>git add *
* \>git add .
* \>git status

* commit.. 영속적으로 저장.. 
* git commit
* 모든 커밋 명령은 커밋 메시지 꼭 입력해야 한다.
* 커밋 정보에는 이 커밋을 내리는 유저 정보가 설정되어야 한다. 
* user.name, user.email 설정되어 있어야 한다.
* user.email 에서의 email 은 검증하지 않음으로 아무거나 써도 상관은 없다.
* \>git config --global user.name "kkang"
* \>git config --global user.email "kkang104@daum.net"
* git commit
* 에디터를 바꾸지 않았다면 커밋 메시지를 입력받기 위해서 vim 에디터가 뜰거다..
* vim editor
* 명령형 -> 입력 : a
* 입력 -> 명령형 : esc
* 저장과 동시에 빠려자가려면 명령형 모드에서 :wq!

* commit 후에 상태를 보면 모든 것이 commit 된 상태.. 


* commit 후에 파일을 수정하거나 신규로 만들어 보자..


* 커밋 명령어입력하면서 메시지 지정
* \>git commit -m "두번째 커밋"


## log - 저장된 commit 객체 정보 파악
* \>git log
* 한화면에 다 안나오면 엔터로 한줄한줄 내리면서 보면 된다..
* 더이상 보기 싫으면 q 입력하면 된다.

* \>git log -n 2
* 갯수를 입력해서 로그 확인.. 

* \>git log --author="kkang"
* 커밋 내린 사람이름으로 필터링.. 

* \>git log --grep="두번째"
* 메시지로 필터링 해서.. 

* \>git log --oneline
* 각 커밋을 한줄로 요약해서 본다..

* \>git log --oneline --graph
* 한줄의 커밋 정보인데.. 라인을 그려줘서 약간의 그래프 모양으로..
* 브랜치 작업이 들어가기 시작하면 선이 어떻게 연결되는지가 커밋 메시지에서 중요해진다..

## show, 커밋 정보 확인.. 
* \>git show
* \>git show id
* id 는 예약어가 아니라.. commit 을 식별하기 위한 hash 값.. 
* \>git show head^
* head 는 예약어.. 
* head^ 1개 전... 
* \>git show head^^
* 전전...
* \>git show head~2
* 2개 이전꺼.. 


## rm - 파일 삭제, 옵션에 따라 다르게 동작
* \>git rm --cache a.txt
* --cache 를 추가하는 것은 실제 w/d 의 파일 삭제가 아니라 index 에 포함시켰던 파일을 index 에서 빼고자 할때..
* \>git rm b.txt 
* w/d 의 실제 파일을 제거.. 그 파일이 commited 상태여야 한다.. index 에 포함되어 있으면 제거 안된다.. 

* \>git rm -f c.txt
* -f 를 추가하면 그 파일일 index 에 포함되든 안되든 무조건, 강제적으로 삭제.. 
* git명령으로 파일을 삭제하면 실제 파일 삭제와 동시에 그 파일이 삭제되었다는 정보가 index 에 포함이 된다.. commit 만 시키면 된다..
* 편리성 차원에서 git 명령으로 삭제.. 삭제 + add

## restore, w/d 복원
* \>git restore --source=hash *
* restore 로 복원하면 w/d 는 복원되지만 그렇다고 head 가 변경되지는 않는다. 즉 commit 저장 객체들은 그대로 유지된다.
* restore 로 복원시키는 것은 commit 정보는 그대로 유지한 상태에서.. w/d 만 이전 상태로 만들고자 할때 사용..

## reset, 복원
* \>git reset hash
* reset 은 커밋 정보 변경이다. 특정 hash 까지 커밋 정보를 날려버려서 HEAD 가 지칭하는 커밋을 바꾸는 명령이다.
* W/D 까지 변경되지는 않는다. 
* \>git reset --hard hash
* commit 조정되면서.. head 가 지칭하는 commit 으로.. w/d 도 변경.. 

## amend 
* 새로운 commit 을 발생시킬때, 이전 commit 정보를 덥어쓰기 하고 싶은경우..
* \>git commit --amend -m "aaa"

## reflog
* reset 으로 삭제된 commit 정보가 유지되고 있다.. 그 정보까지 보고 싶을 때.. 
* 그 정보로 복원도 가능하다.. 
* \>git reflog
* \>git reset --hard hash
