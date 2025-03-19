from requests import get, put

print(get('http://127.0.0.1:8080/api/jobs').json())  # получаем все запросы

print(put('http://127.0.0.1:8080/api/jobs/1', json={}).json())  # пустой запрос
print(put('http://127.0.0.1:8080/api/jobs/1', json={'def': 123}).json())  # запрос с неверными параметрами
print(put('http://127.0.0.1:8080/api/jobs/111', json={'job': 'IMPORTANT New job'}).json())  # не существующая работа
print(put('http://127.0.0.1:8080/api/jobs/1', json={'is_finished': True}).json())  # меняем is_finished у id = 1
print(get('http://127.0.0.1:8080/api/jobs').json())  # получаем все запросы
