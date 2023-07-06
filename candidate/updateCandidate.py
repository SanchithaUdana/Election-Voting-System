from config import dbConfig
import adminDashboard as dashboard


def updateCandidate():

    myCursor = dbConfig.mydb.cursor()

    # first view
    print("Search Candidate")
    nic = input(" Enter NIC number : ")
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

    # update candidate

    print("Do you need update candidate ")
    update = input("press y / n  : ")

    if update == "y":
        print("")
        name = input("01. Enter candidate Name : ")
        age = input("02. Enter candidate Age : ")
        state = input("03. Enter candidate state : ")
        education = input("04. Enter candidate Education : ")
        party = input("05. Enter candidate Party : ")
        nominateNo = input("06. Enter candidate Nominate No : ")

        sql = "UPDATE candidate SET nname = %s, age = %s, state = %s, education = %s, party = %s, nominateNo = %s " \
              "WHERE nic = %s"
        val = (name, age, state, education, party, nominateNo, nic)

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

