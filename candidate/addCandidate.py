from config import dbConfig
import adminDashboard as dashboard


def addCandidate():

    myCursor = dbConfig.mydb.cursor()

    print("---------------------")
    print("Add Candidate Details ")
    print("---------------------")
    print("")
    nic = input("01. Enter candidate NIC : ")
    name = input("02. Enter candidate Name : ")
    age = input("03. Enter candidate Age : ")
    state = input("04. Enter candidate state : ")
    education = input("05. Enter candidate Education : ")
    party = input("06. Enter candidate Party : ")
    nominateNo = input("07. Enter candidate Nominate No : ")
    defaultVote = 0
    sql = "INSERT INTO candidate VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (nic, name, age, state, education, party, nominateNo, defaultVote)
    myCursor.execute(sql, val)

    dbConfig.mydb.commit()

    print("")
    print(myCursor.rowcount, "record inserted.")

    print("## Do you need add more ##")
    addMore = input("press y / n : ")

    if addMore == "y":
        addCandidate()

    print("")
    print("## If you need ReDirect to Dashboard ##")
    des = input("press y / n : ")
    if des == "y":
        dashboard.adminDashboard()
    else:
        print("")
        print("Good Bye")
        exit()
