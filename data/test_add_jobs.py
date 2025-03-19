from requests import post, get

print(get('http://127.0.0.1:8080/api/jobs').json())  # получаем все запросы
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
