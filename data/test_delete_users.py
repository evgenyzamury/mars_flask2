from requests import get, delete

print(get('http://127.0.0.1:8080/api/users').json())
print(delete('http://127.0.0.1:8080/api/users/999').json())
print(delete('http://127.0.0.1:8080/api/users/sa').json())
print(delete('http://127.0.0.1:8080/api/users/3').json())
print(get('http://127.0.0.1:8080/api/users').json())  # получаем все
