import sys
subject = int(sys.stdin.readline())
score = [int(i) for i in sys.stdin.readline().split()]
new_score = [round((i/max(score)*100), 2) for i in score]
print(sum(new_score) / len(new_score))