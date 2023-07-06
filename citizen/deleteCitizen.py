from config import dbConfig
import adminDashboard as dashboard


def deleteCitizen():

    myCursor = dbConfig.mydb.cursor()

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

    # delete special citizen
    print("")
    print("Do you need delete special citizen ")
    delete = input("press y / n  : ")

    if delete == "y":
        nic = input(" Enter NIC number : ")
        print("---------------------")
        print("Delete Citizen Details ")
        print("")

        sql = "DELETE FROM citizen WHERE nic = %s"

        myCursor.execute(sql, (nic,))

        dbConfig.mydb.commit()

        print(myCursor.rowcount, "record deleted")

    # dashboard loading

    print("")
    print("## If you need ReDirect to Dashboard ##")
    des = input("press y / n : ")
    if des == "y":
        dashboard.adminDashboard()
    else:
        print("")
        print("Good Bye")
        exit()
