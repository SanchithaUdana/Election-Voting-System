import userDashboard as userDashboard
import adminDashboard as adminDashboard


def login():
    print("")
    print("             #-----------------------------------#")
    print("             # Welcome to Election Voting System #")
    print("             #-----------------------------------#")
    print("                       📈 Login Page 📈 ")
    print("----------------------------------------------------------------------")
    print("")
    print("Are you User ?")
    user = input("press y / n : ")
    if user == "y":
        userDashboard.userDashboard()
    else:
        password = input("Enter Admin Password : ")
        if password == "1234":
            adminDashboard.adminDashboard()
        else:
            print("invalid password -  🛑 secure system exit enabled 🛑")
            exit()
