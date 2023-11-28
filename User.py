from enum import Enum


class Usertype(Enum):
    PATIENT = 1
    DOCTOR = 2


class User:
    def __init__(self, user_id: int, name: str, surname: str, user_type: Usertype):
        self.id = user_id
        self.name = name
        self.surname = surname
        self.UserType = user_type
