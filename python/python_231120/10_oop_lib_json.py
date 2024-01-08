import json

son_dict = {
    'name': 'SON',
    'age': 29,
    'address': ['KOR','ENG','GER']
}

son_json = json.dumps(son_dict)  # dict를 json으로 변환
print(son_json)
print(type(son_json))

lee_json = '{"name": "SON", "age": 29, "address": ["KOR", "ENG", "GER"]}'
lee_dict = json.loads(lee_json) # json을 dict로 변환
print(lee_dict)
print(type(lee_dict))