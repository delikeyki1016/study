import sys
student_list = [int(i) for i in range(1, 31)]

for _ in range(28):
    num = int(sys.stdin.readline())
    student_list.remove(num)
        
print(*student_list, sep="\n")
