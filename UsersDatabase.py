from User import User


class UserDatabase:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.users = []
        self.load_data()

    def load_data(self):
        with open(self.file_path, 'r') as file:
            for line in file:
                data = line.strip().split()
                user_id, name, surname, role, username, password = data[0], data[1], data[2], data[3], data[4], data[5]
                self.users.append(User(int(user_id), name, surname, role, username, password))

    def user_exists(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return True
        return False

    def get_user(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def add_user(self, name, surname, role, username, password):
        with open(self.file_path, 'a') as file:
            file.write(f"\n{str(len(self.users))} {name} {surname} {role} {username} {password}")
        self.users.append(User(len(self.users), name, surname, role, username, password))

    def delete_user(self, name, surname):
        for user in self.users:
            if user.name == name and user.surname == surname:
                if user.userType == "Doctor":
                    return False
                else:
                    user_to_delete_id = user.id
                    self.users.remove(user)
                    try:
                        with open(self.file_path, 'r') as file:
                            lines = file.readlines()
                        if user_to_delete_id <= 0 or user_to_delete_id > len(lines):
                            return False
                        del lines[user_to_delete_id]
                        with open(self.file_path, 'w') as file:
                            file.writelines(lines)
                    except FileNotFoundError:
                        print("File not found. Please provide a valid file path.")
                    except Exception as e:
                        print(f"An error occurred: {str(e)}")

    def update_user_data(self, change_type, user_id, change):
        for user in self.users:
            if user.id == user_id:
                if change_type == "Name":
                    user.name = change
                elif change_type == "Surname":
                    user.surname = change
                elif change_type == "Username":
                    user.username = change
                elif change_type == "Password":
                    user.password = change
