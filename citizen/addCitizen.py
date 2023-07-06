from config import dbConfig
import adminDashboard as dashboard


def addCitizen():

    myCursor = dbConfig.mydb.cursor()

    print("---------------------")
    print("Enter Citizen Details ")
    print("---------------------")
    print("")
    nic = input("01. Enter Your NIC : ")
    name = input("02. Enter Your Name : ")
    age = input("03. Enter Your Age : ")

    # age checking

    if int(age) <= 18:
        print("")
        print("You can not Register")
        print("")
        print("## Do you need add more ##")
        addMore = input("press y / n : ")

        if addMore == "y":
            addCitizen()

        print("")
        print("## If you need ReDirect to Dashboard ##")
        des = input("press y / n : ")
        if des == "y":
            dashboard.adminDashboard()
        else:
            print("")
            print("Good Bye")
            exit()

    state = input("04. Enter your state : ")

    sql = "INSERT INTO citizen (nic, name, age, state) VALUES (%s, %s, %s, %s)"
    val = (nic, name, age, state)
    myCursor.execute(sql, val)

    dbConfig.mydb.commit()

    print("")
    print(myCursor.rowcount, "record inserted.")

    print("## Do you need add more ##")
    addMore = input("press y / n : ")

    if addMore == "y":
        addCitizen()

    print("")
    print("## If you need ReDirect to Dashboard ##")
    des = input("press y / n : ")
    if des == "y":
        dashboard.adminDashboard()
    else:
        print("")
        print("Good Bye")
        exit()
