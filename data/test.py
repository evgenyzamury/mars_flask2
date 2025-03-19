from requests import get, post, delete

print(get('http://127.0.0.1:8080/api/jobs').json())
print(get('http://127.0.0.1:8080/api/jobs/1').json())
print(get('http://127.0.0.1:8080/api/jobs/20').json())
print(get('http://127.0.0.1:8080/api/jobs/q').json())
print(post('http://127.0.0.1:8080/api/jobs', json={}).json())  # тестируем пустой запрос
print(post('http://127.0.0.1:8080/api/jobs', json={'job': 'make job 1',
                                                   'team_leader': 1,
                                                   'collaborators': '1, 2'}).json())  # запрос с неверными параметрами
print(post('http://127.0.0.1:8080/api/jobs', json={'job': 'make job 2'}).json())  # запрос с неверными параметрами
print(post('http://127.0.0.1:8080/api/jobs', json={'job': 'make job 3',
                                                   'team_leader': 1,
                                                   'work_size': 15,
                                                   'collaborators': '1, 2'}).json())  # верный запрос
print(get('http://127.0.0.1:8080/api/jobs').json())  # получаем все запросы обратно

print(delete('http://127.0.0.1:8080/api/jobs/999').json())
# работы с id = 999 нет в базе

print(delete('http://127.0.0.1:8080/api/jobs/10').json())
