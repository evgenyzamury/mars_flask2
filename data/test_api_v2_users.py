from requests import post, get, delete

print(get('http://127.0.0.1:8080/api/v2/users').json())

print(get('http://127.0.0.1:8080/api/v2/users/1').json())
print(get('http://127.0.0.1:8080/api/v2/users/23').json())
print(get('http://127.0.0.1:8080/api/v2/users/q').json())

print(post('http://127.0.0.1:8080/api/v2/users', json={
    'name': '123',
    'surname': ' 1231',
    'age': 123,
    'address': '123',
    'email': 'aev223332214322@ama.ru',
    'position': 'fda',
    'speciality': '1231',
    "hashed_password": 'qwerty'
}).json())

print(post('http://127.0.0.1:8080/api/v2/users', json={
    'name': '123',
    'surname': ' 1231',
    'age': 123,
    'address': '123',
    'email': 'aevge12ny@ama.ru',
    'speciality': '1231',
    "hashed_password": 'qwerty'
}).json())

print(delete('http://127.0.0.1:8080/api/v2/users/123').json())
print(delete('http://127.0.0.1:8080/api/v2/users/3').json())

print(post('http://127.0.0.1:8080/api/v2/users', json={}).json())


print(get('http://127.0.0.1:8080/api/v2/users').json())

print(get('http://127.0.0.1:8080/api/v2/users').json())
