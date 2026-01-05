users = [
    {
        "id": 1,
        "email": "jjgowda76@gmail.com",
        "password": "123456"
    }
]

def find_user(email: str):
    for user in users:
        if user["email"] == email:
            return user
    return None

def add_user(email: str, password: str):
    new_user = {
        "id": len(users) + 1,
        "email": email,
        "password": password
    }
    users.append(new_user)
    return new_user
