from config import dbConfig
import adminDashboard as dashboard


def updateCitizen():

    myCursor = dbConfig.mydb.cursor()

    # first view
    print("Search Citizen")
    nic = input(" Enter NIC number : ")
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

    # update citizen

    print("Do you need update citizen ")
    update = input("press y / n  : ")

    if update == "y":
        print("")
        name = input("02. Enter Your Name : ")
        age = input("03. Enter Your Age : ")

        # age checking

        if int(age) <= 18:
            print("")
            print("You can not Register")
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

        sql = "UPDATE citizen SET  name = %s, age = %s, state = %s WHERE nic = %s"
        val = (name, age, state, nic)

        myCursor.execute(sql, val)

        dbConfig.mydb.commit()

        print(myCursor.rowcount, "record(s) updated")

        print("")
        print("## If you need ReDirect to Dashboard ##")
        des = input("press y / n : ")
        if des == "y":
            dashboard.adminDashboard()
        else:
            print("")
            print("Good Bye")
            exit()

