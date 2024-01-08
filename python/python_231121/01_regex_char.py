from regex_check import match_check # from 파일명(모듈명) import 함수명

# [] =>  안의 모든 문자
# . => \n을 제외한 모든 문자 1개 
# * => 앞에 있는 문자가 0번 이상
# + => 앞에 있는 문자가 1번 이상
# {n,m} => n번 이상 m번 이하 
# ? => {0,1}
# ^ => not 또는 시작
# $ => 끝
# | => or
# () => group, group(0) 은 전체 

match_check('[abc]', 'alphabet') # T
match_check('[abc]', 'liberty') # T
match_check('[abc]', 'digit') # F
print("1.=====================")
match_check('[0-9]', '123') # T
match_check('[^0-9]', '123') # F
print("2.=====================")
match_check('[a-z]', 'Alphabet') # T
match_check('[a-zA-Z]', 'Alphabet') # T
print("3.=====================")
match_check('[a-zA-Z0-9]', 'GilDong123') # T, match_check('\w', 'GilDong123')
match_check('[^a-zA-Z0-9]', 'GilDong123') # F, match_check('\W', 'GilDong123')
print("4.=====================")
match_check('\s', 'Hello World') # T,  \s 스페이스 
print("5.=====================")
match_check('\W', '홍길동') # F
match_check('[^a-zA-Z0-9]', '홍길동') # T 
match_check('[가-힣]', '홍길동') # T


# . 은 줄바꿈\n을 제외한 모든 문자와 매치 
# ex) a.b => a와 b 사이에 \n을 제외한 어떠한 문자가 들어가야 트루인데, 그 문자가 하나가 있어야 트루 ex) abb 는 트루  
print("6.=====================")
match_check("a.b", "a0b") # T
match_check("a.b", "a.b") # T
match_check("a.b", "aaab") # T 뒤에 aab가 매칭이 됨 
match_check("a.b", "a\nb") # F
match_check("a.b", "a\tb") # T
match_check("a.b", "a    b") # F 한개만 들어가야 함 
match_check("a.b", "a b") # T
match_check("a.b", "acb") # T
match_check("a.b", "a\n\tb") # F
print("7.=====================")
match_check("a[.]b", "a.b") # T 가운데에 .이 있어야 트루 
match_check("a[.]b", "a0b") # F
match_check("a[.]b", "a\nb") # F

print("8.=====================")
# * =>  * 바로 앞의 문자 o가 0번 이상 반복되면 트루, * = {0,} 와 같음 
# + =>  + 바로 앞의 문자 o가 1번 이상 반복되면 트루, + = {1,} 와 같음 

match_check("go*d", 'gd') # T o가 0번 나왔다고 볼수있다.
match_check("go*d", 'god') # T o가 1번 나왔기 때문에 트루
match_check("go*d", 'gooooood') # T

print("9.=====================")
match_check("go+d", 'gd') # F
match_check("go+d", 'god') # T
match_check("go+d", 'gooooood') # T

print("10.=====================")
match_check("g[A-Z]+d", 'goooooood') # F
match_check("g[A-Z]+d", 'gOOOOOOOd') # T 

print("11.=====================")
# {2,5} 2번 이상 반복 5번 이하 반복이면 트루

match_check("hel{2}o", 'hello') # T
match_check("hel{1,3}o", 'heo') # F # 바로 앞의 문자 l이 1번 or 2번 or 3번 반복되면 트루
match_check("hel{1,3}o", 'helo') # T l이 1번 이상 반복, h,e,o와는 무관함 
match_check("hel{1,3}o", 'hello') # T
match_check("hel{1,3}o", 'helllo') # T
match_check("hel{1,3}o", 'hellllo') # F

print("12.=====================")
# ? = {0,1} 0번 이상 1번 이하 반복이면 트루 ex) s? => s가 없거나 한번 있으면 트루 
match_check("hell?o", 'heo') # F ? 바로 앞의 문자 l이 0번 또는 1번 등장하는 것을 나타냄
match_check("hell?o", 'helo') # T l이 0번 반복
match_check("hell?o", 'hello') # T l이 1번 반복 
match_check("hell?o", 'helllo') # F {0,1} 과 같다. l이 2번 반복

print("13.=====================")
match_check("hel{,3}o", 'heo') # T 3번 이하 
match_check("hel{,3}o", 'helo') # T
match_check("hel{,3}o", 'hello') # T
match_check("hel{,3}o", 'helllo') # T
match_check("hel{,3}o", 'hellllo') # F
print("14.=====================")
match_check("hel{3,}o", 'hello') # F
match_check("hel{3,}o", 'helllo') # T
match_check("hel{3,}o", 'hellllo') # T
print("15.=====================")
match_check("go{0,}d", 'gd') # T o가 0번 이상이면 트루
match_check("go{1,}d", 'gd') # F o가 1번 이상이면 트루 











