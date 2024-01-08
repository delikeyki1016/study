rainbow = ['빨강','주황','노랑','초록','파랑','남','보라']

rainbow_color = [i + '색' for i in rainbow]
print(rainbow_color)

rainbow_dict = {i : i + '색' for i in rainbow}
print(rainbow_dict)

rainbow_dict_enumerate = {i + 1 : v + '색' for i, v in enumerate(rainbow)}
print(rainbow_dict_enumerate)