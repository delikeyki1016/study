# 숫자 여러개를 입력받고, 찾으려는 숫자를 입력받아 해당하는 숫자가 있다면 그 숫자의 index를 리스트로 반환 
import sys 

def find_num_index(num_list, value):
    result_list = []
    for i in range(len(num_list)):
        if value == num_list[i]:
            result_list.append(i)
    return result_list

num_list = [int(i) for i in sys.stdin.readline().split()]
value = int(sys.stdin.readline())

print(find_num_index(num_list, value))