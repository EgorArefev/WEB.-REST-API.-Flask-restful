from requests import get, post, delete

print(get("http://localhost:5000/api/v2/users").json())
print(get("http://localhost:5000/api/v2/users/4").json())
print(get("http://localhost:5000/api/v2/users/6").json())
# print(get('http://localhost:5000/api/v2/users/q').json())
print(post("http://localhost:5000/api/v2/users").json())
print(post("http://localhost:5000/api/v2/users", json={"surname": "Золовок"}).json())
print(
    post(
        "http://localhost:5000/api/v2/users",
        json={
            "surname": "Первая запись",
            "age": 15,
            "email": "email@example.com",
            "position": "left",
            "speciality": "postman",
            "address": "Lenina 5",
            "hashed_password": "abdjbda",
        },
    ).json()
)
print(
    delete("http://localhost:5000/api/v2/users/999").json()
)  # пользователя с id = 999 нет в базе
# print(delete("http://localhost:5000/api/v2/users/10").json())
