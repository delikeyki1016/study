def is_even(num: int) -> bool: # 리턴값은 bool인데, 
    if num % 2 == 0:
        return True
    else:
        return False # type hint가 틀려도 오류는 안난다

print(is_even(1))
print(is_even(2))

# 파이썬 명령에서 mypy로 실행하면(mypy 04_type_hint.py) 타입힌트 관련 에러도 체크한다. 