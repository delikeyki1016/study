# table 형식으로 저장. 
# 행(row) : 값 / 열(row) : 속성
# 자동차테이블
#  : 개체 1 => 이름: P/ 컬러: 레드/ 원산지: 독일
#  : 개체 2 => 이름: F/ 컬러: 레드/ 원산지: 이탈리아 
#  속성적 공통점 : 컬러 레드 (관계 형성)
# 개체(Entity) : 속성과(attribute) 값(record)
# 데이터베이스 : 개체들의 집합 (Entities), 개체와 관계의 집합 

# SQL : Structured Query Languge(구조화된 질의어), 자연어에 가까운 언어 
# DBMS : data base management system 
# ANSI-SQL :  select, insert, update, delete 

# DDL : Data Definition Languge 개체 관리를 위함(create, drop, alter)
# DCL : Data Control Languge 접근권한등의 사용자 관리를 위함 ex) 디비엠에스 계정추가,권한부여, 보통 DBA가 사용함
# TCL : Transaction Control Languge 사용자의 작업관리를 위함
# *DML : Data Management Languge (select, insert, update, delete)
# 트랜잭션 : 테이블에 입력,수정,삭제 시 중간에 실패하는 경우가 있어서 로그를 임시로 저장해둠(트랜잭션).

# 환경설정 MSSQL 
# 1. 특별에디션 MSSQL Express 다운로드 https://www.microsoft.com/ko-kr/sql-server/sql-server-downloads 설치
# 2. SSMS 다운로드 https://learn.microsoft.com/ko-kr/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16 위의 연결에서 설치하지 말고, 해당 파일로 따로 설치 
#    (SQL Sever Management Studio)
# 3. mssql adventureworks(샘플DB) https://learn.microsoft.com/ko-kr/sql/samples/adventureworks-install-configure?view=sql-server-ver16&tabs=ssms SSMS에서 연결

# < 기초 DML >=============================================================
# 자료형 : 문자형 (문자, 날짜 )'STR' 숫자형 (정수,실수,통화,이진) 7

# INSERT INTO TABLE_NAME(FIELD1, FIELD2,...) VALUES(VALUES1, VALUES2,...)
# - 속성과 값의 개수가 일치해야한다.

# UPDATE TABLE_NAME SET 속성=변경될속성값 WHERE 조건=조건식

# DELETE FROM TABLE_NAME WHERE 조건=조건식

# * 업데이트,딜리트는 조건식이 꼭 필요함, 조건이 없다면 데이터가 모두 바뀜

# SELECT * FROM TABLE_NAME : TABLE_NAME에서 모든 데이타를 가져와 

# SELECT [Name], [GroupName] FROM [HumanResources].[Department] WHERE [DepartmentID]=7  : [HumanResources].[Department]에서 DepartmentID=7 것의 Name, GroupName을 가져와

# Primary Key : 개체를 식별해주는 고유의 값

# SELECT * FROM TABLE_NAME WHERE 조건=조건식 ORDER BY FIELD1(ASC/DESC) 오름차순,내림차순 => order by 는 항상 맨 마지막 구문으로

# null 값도 값으로 인식 : 어떤 값이 들어올 지 모르는 상태를 뜻함, 크기를 알 수 없음. 연산 불가능 IS NULL 또는 IS NOT NUll 

# and, or 연산자 
# x : 1 / y: 1 => and : 1 / or : 1
# x : 1 / y: 0 => and : 0 / or : 1
# x : 0 / y: 1 => and : 0 / or : 1
# x : 0 / y: 0 => and : 0 / or : 0

# 특수연산자 LIKE
# select * from table where field LIKE '%조건%' => 조건의 유사한 값도 찾는다. 문자 유형에만 사용 가능 
# % 어떤 단어라도 상관없음
# ex) %A => A로 끝나는 단어 
# ex) A% => A로 시작하는 단어
# ex) %A% => A가 어디에 포함되든 상관없이 다 찾음 

# 특수연산자 BETWEEN 
# select * from table where field BETWEEN '조건1' AND '조건2' => 조건1, 조건2 사이의 값만 찾는다.
# ex) A >= 100 and A <= 300 ==> A BETWEEN 100 and 300

# 특수연산자 IN
# select * from table where field IN(조건1, 조건2,...) => 복수의 조건에 해당하는 값을 찾음
# ex) where A=100 or A=200 or A=300 ==> where A in (100,200,300) A가 100,200,300인 값을 찾음
# where A not in (100,200,300) => A가 100,200,300이 아닌 값 찾음

# 숫자함수 
# Round(x1,x2,[x3]) => x1 : 반올림을 처리할 대상, x2 : 소수점 몇자리부터 반올림할 지, [x3] : 선택  ex) Round(x1, 0) 소수점을 버리고 반올림
# Rand() => 0~1 사이의 난수 발생, RAND() AS 별칭 => 필드명을 별칭으로 해서 난수를 발생시킴

# 문자함수
# LEFT(x1,x2) => x1 : 대상 문자, x2 : 왼쪽부터 몇째 자리부터 줄일 것인지. ex) Left('MSSQL', 2) => MS 
# RIGHT(x1,x2)
# SUBSTRING(x1,x2,x3) => x1 : 대상 문자, x2 : 시작위치, x3 : 시작위치로 부터 몇자까지 출력할 지
# LEN(x1) => x1의 문자열 길이 숫자로 반환
# REPLACE(x1,x2,x3) => x1 : 대상 문자, x2 : 특정한 문자를, x3 : 해당 문자로 바꿔서 전달

# 날짜함수
# sysdatetime() => 
# getdate() => 서버 상의 시간과 날짜 전달, year(x1), month(x1), day(x1), hour(x1), second(x1), minute(x1) 
# ex) SELECT getdate() AS t_date, year(getdate()) AS t_year, month(getdate()) AS t_month

# DATEPart(x1, x2) => x1 : 기준, x2 : 어떤 날짜로 부터 (YY,MM,HH,MI => 년,월,일,시간)
# ex) SELECT getdate() AS t_date, datepart(YY, getdate()) AS T_Y ==> getdate()로 부터 연도만 뽑아와라 
# ex) where DATEPart(YY, ModifiedDate) = 2014 AND DATEPart(MM, ModifiedDate) = 1 ==> 2014년, 1월만 뽑아와라 

# DATEDiff(x1,x2,x3) => ex) SELECT DATediff(YY, '2020-01-01', getdate()) ==> 2020년 1월 1일부터  현재날짜까지의 연도 차이

# DateAdd(x1,x2,x3) => ex) SELECT dateadd(dd, 1000, '2022-01-01') ==> 2022-01-01로 부터 1000일 뒤의 날짜
# ex) SELECT datepart(w, dateadd(dd, 1000, '2022-01-01')) ==> 2022-01-01로 부터 1000일 뒤의 날짜의 요일 구하기 (1~7 => 월~일)

# 집계처리 : group by 
# 작성순서 : select 출력할 대상 from 어떤 테이블로부터 where 조건 group by 그룹 조건 order by 정렬조건

# RDB : 관계형DB

# view 가상테이블(임시저장, 물리적공간을 차지X) 주의점: view 내용이 삭제,수정되면 원본 내용도 삭제,수정된다. 즉 원본 내용과 연결되어있다.
# in-line view : 휘발성으로 사용하고 버림. 
# ex) select * from (select FIELD1, FIELD2 AS F_2 from Table_A) AS Temp_T => temp_T라는 이름으로 인라인뷰를 생성해서 사용하겠다.
# => select * from (select FIELD1, FIELD2 AS F_2 from Table_A) AS Temp_T where F_2 > 10 => ()인라인뷰로 묶게되면 인라인뷰 안에서 사용한 AS 컬럼명을 where절에서 사용할 수 있다.

# 서브쿼리 : where절에서 사용하는 쿼리 
# ex) select * from [HumanResources].[EmployeeDepartmentHistory]
# where DepartmentID in (select DepartmentID from [HumanResources].[Department]
# where GroupName='Sales and Marketing')

# 중복쿼리

# *Cross,union은 활용도가 높진않음 
# Cross join(A*B) => A테이블, B테이블의 조합
# : select * frome tableA cross join tableB
# Union join (합집합), interset(교집합)
# : select field1, field2 from tableA union select field1, field2 from tableB ==> field1,field2 필드(명이 같은것이 아닌)개수가 같아야 유니온 가능

# **Join 구문(중요!!)
# 1. outer join 
# : select * from table1 as 별칭1 [left or right or full] outer join table2 as 별칭2 on 별칭1.아이디 = 별칭2.아이디 => 별칭1을 기준으로 [left] 조인 

# 2. inner join(공통분모 찾기)
# : select * from table1 as 별칭1 inner join table2 as 별칭2 on 조건식 
# (inner join 명령을 쓰지 않을 경우에는 아래처럼)
# : select * from table1 as 별칭1, table2 as 별칭2 where 조건식 

# 응용
# select * into copy_table from basic_table (테이블 카피)
# Insert into table1 select * from table2 => table2에 있는 모든 내용을 table1에 한번에 추가 

# pivot(sum(ST) for YY in([2011],[2012],[2013],[2014])) as pivot_T  => 피벗은 컬럼명으로 변경하기



######## MySQL ########
# -- 주석 
# 좌측 네비게이터에서 디비를 선택해서 (더블클릭) 해당 디비를 이용하겠다는 선언을 해줘야 함. 아니면 use 디비명; 선언해준 후 쿼리를 써야한다.
# select * from membertbl; 문장 끝에 세미콜론 붙이기 
# 한문장만 실행 ctrl + enter / 전체 문장 실행 Ctrl+Shift+Enter
# 인덱스 : 튜닝의 개념이며, 검색의 속도를 빨리하기 위해 사용, 책의 색인과 같은 개념 
# 대소문자 구분 없음, 관습적으로 키워드는 대문자로 사용

# 뷰 : 가상의 테이블, 실제 테이블에 링크된 개념. (보안)
# create view uv_테이블명 as select memberName, memberAddress from membertbl

# 스토어드 프로시저(stored procedure, 저장 절차) : 여러개의 쿼리문을 묶어 한번에 실행함 
# delimiter //
# create procedure myProc()
# begin
# 	select * from membertbl where memberName = '당탕이';
# 	select * from producttbl where productName = '냉장고';
# end //
# delimiter ;  # 항상 한 칸 띄워줘야 함! 

# call myProc(); # 사용

# 트리거 등록
# delimiter //
# create trigger trg_deleteMemberTBL
# 	after delete -- 언제 실행되는 트리거인지 명시, 삭제 후에 실행 
#     on membertbl -- 트리거가 부착될 테이블 명시 
#     for each row -- 각 행마다 적용시킨다.
# begin 
# 	insert into deleteMemberTBL
# 		-- OLD는 예약어. 기존 테이블을 지칭.
#       -- CURDATE()는 현재 시간을 지칭하는 내장함수
# 		values(OLD.memberId, OLD.memberName, OLD.memberAddress, CURDATE());
# end //
# delimiter ;

# ERD : Entity Relation Diagram 