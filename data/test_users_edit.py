from requests import get, put

print(get('http://127.0.0.1:8080/api/users').json())  # получаем все запросы
print(put('http://127.0.0.1:8080/api/users/1', json={}).json())
print(put('http://127.0.0.1:8080/api/users/1222', json={}).json())
print(put('http://127.0.0.1:8080/api/users/1', json={'na': 1}).json())
print(put('http://127.0.0.1:8080/api/users/1', json={'address': 'module_2'}).json())
print(get('http://127.0.0.1:8080/api/users').json())