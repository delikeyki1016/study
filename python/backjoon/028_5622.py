phone = {
    2: ['A','B','C'],
    3: ['D','E','F'],
    4: ['G','H','I'],
    5: ['J','K','L'],
    6: ['M','N','O'],
    7: ['P','Q','R','S'],
    8: ['T','U','V'],
    9: ['W','X','Y','Z'],
}

import sys
al = sys.stdin.readline().rstrip()
result = 0
for i in al:
    # print(i)
    for key, value in phone.items():
        # print(key, value)
        if i in value:
            result += key+1

print(result)

