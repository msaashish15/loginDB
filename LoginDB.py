#Program to create a database of user name and pswd and verfiy user log in 
def pwd_check(pwd):
    return 1


def login(loginDB,user):
    if user not in loginDB:
        print("You are a new user")
        pwd=input("Enter your password")
        res=pwd_check(pwd)
        if res==1:
            loginDB[user]=pwd
            print("Registration successful")
    else:
        pwd=input("Enter your password")
        if loginDB[user] == pwd:
            print("Login successful")
        else:
            print("Wrong password")

print("Customer Login Screen")

loginDB={"user1":"pswd1","admin":"cse1","user2":"csebms"}
while True:
    ch=int(input("Press 1 for login, 2 for register,3 to quit"))
    if ch==1: 
        user=input("Enter your username")
        login(loginDB,user)
    elif ch==2:
            user=input("Enter your user name")
            login(loginDB,user)
    elif ch==3:
            break
