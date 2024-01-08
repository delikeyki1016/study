import sys
origin_pieces = [1, 1, 2, 2, 2, 8]
find_pieces = [int(i) for i in sys.stdin.readline().split()]
for i in range(len(origin_pieces)):
    print(origin_pieces[i] - find_pieces[i], end=' ')