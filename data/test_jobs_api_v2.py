from requests import get, delete, post, put

print(get('http://127.0.0.1:8080/api/v2/jobs').json())
print(get('http://127.0.0.1:8080/api/v2/jobs/1').json())
print(get('http://127.0.0.1:8080/api/v2/jobs/1000').json())
print(get('http://127.0.0.1:8080/api/v2/jobs/q').json())

print(post('http://127.0.0.1:8080/api/v2/jobs', json={}).json())
print(post('http://127.0.0.1:8080/api/v2/jobs', json={'job': 'Make all'}).json())
print(post('http://127.0.0.1:8080/api/v2/jobs', json={
    'job': 'make all',
    'team_leader': 1,
    'work_size': 'q',
    'collaborators': '1, 2, 3'
}).json())
print(post('http://127.0.0.1:8080/api/v2/jobs', json={
    'job': 'make all',
    'team_leader': 1,
    'work_size': 10,
    'collaborators': '1, 2, 3'
}).json())

print(get('http://127.0.0.1:8080/api/v2/jobs').json())

print(delete('http://127.0.0.1:8080/api/v2/jobs/3').json())
print(delete('http://127.0.0.1:8080/api/v2/jobs/3213').json())
print(delete('http://127.0.0.1:8080/api/v2/jobs/q').json())
print(get('http://127.0.0.1:8080/api/v2/jobs').json())

print(put('http://127.0.0.1:8080/api/v2/jobs/1', json={'job': 'Put job'}).json())
print(put('http://127.0.0.1:8080/api/v2/jobs/1', json={'work_size': 'Put job'}).json())

print(get('http://127.0.0.1:8080/api/v2/jobs').json())
