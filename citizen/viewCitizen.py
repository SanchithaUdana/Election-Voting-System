from config import dbConfig
import adminDashboard as dashboard


def viewCitizen():
    myCursor = dbConfig.mydb.cursor()

    print("Do you need view special citizen ")
    search = input("press y / n  : ")

    if search == "y":
        nic = input("01. Enter NIC number : ")
        print("---------------------")
        print("View Citizen Details ")
        print("---------------------")
        print("")

        sql = "SELECT * FROM citizen WHERE nic = %s"

        myCursor.execute(sql, (nic,))

        result = myCursor.fetchall()

        if myCursor.rowcount == 0:
            print("not available")

        for x in result:
            print("-------------")
            print("NIC   = ", x[0])
            print("Name  = ", x[1])
            print("Age   = ", x[2])
            print("State = ", x[3])

        print("")
        print("## If you need ReDirect to Dashboard ##")
        des = input("press y / n : ")
        if des == "y":
            dashboard.adminDashboard()
        else:
            print("")
            print("Good Bye")
            exit()

    # view all details

    print("---------------------")
    print("View Citizen Details ")
    print("---------------------")
    print("")

    myCursor.execute("SELECT * FROM citizen")

    result = myCursor.fetchall()

    if myCursor.rowcount == 0:
        print("Empty table")

    for x in result:
        print("-------------")
        print("NIC   = ", x[0])
        print("Name  = ", x[1])
        print("Age   = ", x[2])
        print("State = ", x[3])

    print("")
    print("## If you need ReDirect to Dashboard ##")
    des = input("press y / n : ")
    if des == "y":
        dashboard.adminDashboard()
    else:
        print("")
        print("Good Bye")
        exit()
