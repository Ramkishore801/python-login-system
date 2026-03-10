
username = "admin"
password = "1234"

attempts = 3

while attempts > 0:
    user = input("Enter username: ")
    pwd = input("Enter password: ")

    if user == username and pwd == password:
        print("Login successful")
        break
    else:
        attempts -= 1
        print("Wrong credentials")
        print("Remaining attempts:", attempts)

if attempts == 0:
    print("Account locked due to too many failed attempts.")
