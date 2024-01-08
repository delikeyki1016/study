from module import rrn  # module 폴더의 rrn 모듈을 불러온다.

data = '931120-1234567'
print(rrn.birth(data))
print(__name__) # __main__
print(rrn.__name__) # module.rrn

# import module.rrn as r 
# print(r.birth(data))

# from module.rrn import birth
# print(birth(data))

# import module.experiment # 여러번 불러도 캐시를 통해 시간을 절약함

# 패키지 : 모듈을 모아놓은 폴더  

# site-package 기본 제공되는 패키지 
# https://pypi.org/ 에서 검색해서 사용할 수 있다.