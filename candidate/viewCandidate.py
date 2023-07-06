from config import dbConfig
import adminDashboard as dashboard


def viewCandidate():
    myCursor = dbConfig.mydb.cursor()

    print("Do you need view special candidate ")
    search = input("press y / n  : ")

    if search == "y":
        nic = input("01. Enter NIC number : ")
        print("---------------------")
        print("View Candidate Details ")
        print("---------------------")
        print("")

        sql = "SELECT * FROM candidate WHERE nic = %s"

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
            print("Education = ", x[4])
            print("Party = ", x[5])
            print("Nomination No = ", x[6])

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
    print("View Candidate Details ")
    print("---------------------")
    print("")

    myCursor.execute("SELECT * FROM candidate")

    result = myCursor.fetchall()

    if myCursor.rowcount == 0:
        print("Empty table")

    for x in result:
        print("-------------")
        print("NIC   = ", x[0])
        print("Name  = ", x[1])
        print("Age   = ", x[2])
        print("State = ", x[3])
        print("Education = ", x[4])
        print("Party = ", x[5])
        print("Nomination No = ", x[6])

    print("")
    print("## If you need ReDirect to Dashboard ##")
    des = input("press y / n : ")
    if des == "y":
        dashboard.adminDashboard()
    else:
        print("")
        print("Good Bye")
        exit()
