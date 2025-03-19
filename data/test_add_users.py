from requests import get, post

print(get('http://127.0.0.1:8080/api/users').json())  # получаем все запросы
print(post('http://127.0.0.1:8080/api/users', json={}).json())
print(post('http://127.0.0.1:8080/api/users', json={'surname': 'Evgeny'}).json())
print(post('http://127.0.0.1:8080/api/users', json={'surname': 'Zamury',
                                                    'name': 'evgeny',
                                                    'age': 19,
                                                    'position': 'Lead',
                                                    'speciality': 'programmer',
                                                    'address': 'module_1',
                                                    'email': 'zamuryevgny@yandex.ru',
                                                    'password': 'qwerty'}).json())
print(get('http://127.0.0.1:8080/api/users').json())  # получаем все запросы
