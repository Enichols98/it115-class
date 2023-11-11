import json


data = {

    'name': 'Elizabeth Nichols',
    'age': 25,
    'city': 'Liberia, Monrovia',
    'interests': ['Read','Exercise','Rest'],
    'is student': True

}

with open('data.json', 'w') as json_file:
    json.dump(data,json)