class User:
    def __init__(self, user_id: int, name: str, surname: str, user_type: str, username: str, password: str):
        self.id = user_id
        self.name = name
        self.surname = surname
        self.userType = user_type
        self.username = username
        self.password = password
