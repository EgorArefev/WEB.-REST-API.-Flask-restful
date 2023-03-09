from requests import get, post, delete


print(get('http://localhost:8080/api/v2/users').json())
print(get('http://localhost:8080/api/v2/users/3').json())
print(get('http://localhost:8080/api/v2/users/48').json())  # нет пользователя
# print(get('http://localhost:8080/api/v2/users/q').json())  # не число

print(post('http://localhost:8080/api/v2/users').json())  # нет словаря
print(post('http://localhost:8080/api/v2/users', json={'name': 'Ivan'}).json())  # не все поля
print(post('http://localhost:8080/api/v2/users', json={'name': 'Ivan', 'position': 'senior programmer',
                                                       'surname': 'Bear', 'age': 23, 'address': 'module_2',
                                                       'speciality': 'computer sciences',
                                                       'hashed_password': 'bear', 'email': 'bear@mars.org'}).json())

print(delete('http://localhost:8080/api/v2/users/999').json())  # id = 999 нет в базе
print(delete('http://localhost:8080/api/v2/users/10').json())  # id = 10 нет в базе