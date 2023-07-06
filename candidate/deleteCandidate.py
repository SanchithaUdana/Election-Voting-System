from config import dbConfig
import adminDashboard as dashboard


def deleteCandidate():

    myCursor = dbConfig.mydb.cursor()

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

    # delete special candidate
    print("")
    print("Do you need delete special candidate ")
    delete = input("press y / n  : ")

    if delete == "y":
        nic = input(" Enter NIC number : ")
        print("---------------------")
        print("Delete Candidate Details ")
        print("")

        sql = "DELETE FROM candidate WHERE nic = %s"

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
