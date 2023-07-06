from config import dbConfig


def userDashboard():
    myCursor = dbConfig.mydb.cursor()

    print("")
    print("             #-----------------------------------#")
    print("             # Welcome to Election Voting System #")
    print("             #-----------------------------------#")
    print("                     📈 User Dashboard 📈")
    print("----------------------------------------------------------------------")
    print("")
    nic = input("Enter Your NIC : ")

    sql = "SELECT * FROM citizen WHERE nic = %s"

    myCursor.execute(sql, (nic,))
    result = myCursor.fetchall()

    if myCursor.rowcount == 0:
        print(nic, "Not Registered")
        exit()

    # citizen can vote
    for x in result:
        citiState = x[3]
        sqlCandi = "SELECT name, party, nominateNo FROM candidate WHERE state = %s"
        myCursor.execute(sqlCandi, (citiState,))
        relatedResult = myCursor.fetchall()

        if myCursor.rowcount == 0:
            print("")
            print("Not Available")
            exit()

        print("")
        print("--------------------------------")
        print("-- Your Area All Nominations --")
        print("--------------------------------")

        for y in relatedResult:
            print("")
            print("Name   = ", y[0])
            print("party   = ", y[1])
            print("nominate No = ", y[2])

    # check party
    print("")
    selectedParty = input("Enter your Selected Party Name : ")

    sqlSelected = "SELECT name, nominateNo FROM candidate WHERE state = %s AND party = %s"
    values = (citiState, selectedParty)
    myCursor.execute(sqlSelected, values)
    canVote = myCursor.fetchall()

    if myCursor.rowcount == 0:
        print("")
        print("Not Available")
        exit()

    print("")
    print("📦📦📦📦📦📦")
    print("You can Vote")
    print("📦📦📦📦📦📦")

    for candi in canVote:
        print("")
        print("Name   = ", candi[0])
        print("party   = ", candi[1])

    # add vote
    print("")
    print("#-----------------#")
    print("Select Voting Order")
    print("#-----------------#")
    print("")
    # add vote

    vote = input("Enter voting Nominate No : ")
    myCursor = dbConfig.mydb.cursor()
    sql = "UPDATE candidate SET totalVote = totalVote + 1 WHERE party = %s AND state = %s AND nominateNo = %s"
    valueFinal = (selectedParty, citiState, vote)
    myCursor.execute(sql, valueFinal)
    dbConfig.mydb.commit()
    print(myCursor.rowcount, "vote(s) updated")

    conti = input("Do you Use Your Other two Votes - y /n : ")
    if conti == "y":
        for count in range(2):
            print("")
            vote = input("Enter voting Nominate No : ")
            myCursor = dbConfig.mydb.cursor()
            sql = "UPDATE candidate SET totalVote = totalVote + 1 WHERE party = %s AND state = %s AND nominateNo = %s"
            valueFinal = (selectedParty, citiState, vote)
            myCursor.execute(sql, valueFinal)
            dbConfig.mydb.commit()
            print(myCursor.rowcount, "vote(s) updated")
    else:
        print("")
        print("#######################")
        print("# Thank for your Vote # ")
        print("#######################")
        exit()
