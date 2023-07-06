from config import dbConfig
import adminDashboard as dashboard


def viewTotalVotes():

    print("")
    print("Do you need Calculate Total Votes ?")
    choice = input("press y / n : ")
    print("")

    if choice == "y":
        myCursor = dbConfig.mydb.cursor()
        sql = "SELECT * FROM candidate ORDER BY totalVote DESC, name ASC"

        myCursor.execute(sql)
        result = myCursor.fetchall()

        if myCursor.rowcount == 0:
            print("not available")

        print("")
        print("---------------------")
        print("     Votes Result    ")
        print("---------------------")

        for x in result:
            print("")
            print("Name        = ", x[1])
            print("State       = ", x[3])
            print("Party       = ", x[5])
            print("Total Votes = ", x[7])

        print("")
        print("## If you need ReDirect to Dashboard ##")
        des = input("press y / n : ")
        if des == "y":
            dashboard.adminDashboard()
        else:
            print("")
            print("Good Bye")
            exit()
    else:
        print("")
        print("## If you need ReDirect to Dashboard ##")
        des = input("press y / n : ")
        if des == "y":
            dashboard.adminDashboard()
        else:
            print("")
            print("Good Bye")
            exit()

