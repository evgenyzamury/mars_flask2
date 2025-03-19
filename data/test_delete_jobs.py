from requests import get, delete

print(get('http://127.0.0.1:8080/api/jobs').json())
print(delete('http://127.0.0.1:8080/api/jobs/999').json())
# работы с id = 999 нет в базе
print(delete('http://127.0.0.1:8080/api/jobs/sa').json())
# работы с id = строки, не может быть
print(delete('http://127.0.0.1:8080/api/jobs/1').json())
# удаляем
print(get('http://127.0.0.1:8080/api/jobs').json())  # получаем все
