correct_user = "admin"
correct_pass = "1234"

attempts = 3

while attempts > 0:
    user = input("Username: ")
    pwd = input("Password: ")

    if user == correct_user and pwd == correct_pass:
        print("Login successful")
        break
    else:
        attempts -= 1
        print("Wrong credentials. Attempts left:", attempts)

if attempts == 0:
    print("Account locked")