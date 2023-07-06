import matplotlib.pyplot as plt
from config import dbConfig
import adminDashboard as dashboard


def barChart():
    myCursor = dbConfig.mydb.cursor()

    # Fetching Data From mysql to python program
    myCursor.execute("SELECT name, totalVote from candidate")
    result = myCursor.fetchall

    names = []
    votes = []

    for i in myCursor:
        names.append(i[0])
        votes.append(i[1])

    print("")
    print("You can get Details Using")
    print("1. Bar Chart")
    print("2. Pie Chart")
    print("")
    cc = input("Enter Your Choice : ")

    if cc == "1":
        plt.bar(names, votes)
        plt.ylim(0, 5)
        plt.xlabel("Name of Candidates")
        plt.ylabel("Total Votes")
        plt.title("Election Voting Result")
        plt.show()

    if cc == "2":
        plt.pie(votes, labels=names)
        plt.show()

    # ending selection

    print("")
    print("## If you need ReDirect to Dashboard ##")
    des = input("press y / n : ")
    if des == "y":
        dashboard.adminDashboard()
    else:
        print("")
        print("Good Bye")
        exit()
