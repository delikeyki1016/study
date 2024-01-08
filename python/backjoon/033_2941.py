croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
words = input()
for i in croatia:
    words = words.replace(i, "0")
print(len(words))
    
    
