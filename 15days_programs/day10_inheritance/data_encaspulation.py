class User:

    def __init__(self, username, password):
        self.username = username  # public
        self.__password = password  # private

    # Getter (optional, usually not used for password)
    def get_password(self):
        return "Access Denied"  # do not expose real password

    # Setter
    def set_password(self, new_password):
        if len(new_password) >= 6:
            self.__password = new_password
            print("Password updated successfully")
        else:
            print("Password must be at least 6 characters")

    # Method to validate login
    def login(self, password):
        if password == self.__password:
            print("Login successful")
        else:
            print("Invalid password")


# Example usage
user1 = User("venkatesh", "123456")

user1.login("123456")  # correct
user1.login("wrong")  # incorrect

user1.set_password("newpass")
user1.login("newpass")