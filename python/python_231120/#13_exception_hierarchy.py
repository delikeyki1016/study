def get_hierarchy(exception_class, indent = 0):
    # print(indent)
    # 들여쓰기를 적용하여 예외클래스 이름 출력
    print(" " * indent + exception_class.__name__, "indent:", indent)
    #  하위 클래스 목록
    subclasses = exception_class.__subclasses__()
    # 각 하위 클래스에 대해 재귀적으로 출력 
    for i in subclasses:
        get_hierarchy(i, indent = indent+2)

# BaseException 부터 시작하여 예외클래스 계층 구조 출력
get_hierarchy(BaseException)
