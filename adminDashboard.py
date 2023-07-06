from citizen import addCitizen as addCitizen, viewCitizen as viewCitizen
from citizen import updateCitizen as updateCitizen, deleteCitizen as deleteCitizen

from candidate import addCandidate as addCandidate, viewCandidate as viewCandidate
from candidate import updateCandidate as updateCandidate, deleteCandidate as deleteCandidate

from totalVote import viewTotalVotes as viewTotalVotes

from reports import barChart as barChart


def adminDashboard():
    # dashboard view
    print("")
    print("             #-----------------------------------#")
    print("             # Welcome to Election Voting System #")
    print("             #-----------------------------------#")
    print("                     📈 Admin Dashboard 📈 ")
    print("----------------------------------------------------------------------")
    print("")
    print("1  : Add Citizen Details            2  : View Citizen Details  ")
    print("3  : Update Citizen Details         4  : Delete Citizen Details")
    print("")
    print("5  : Add Candidates                 6  : View Candidates")
    print("7  : Update Candidates              8  : Delete Candidates")
    print("")
    print("9 : View Voting Result              10 : Generate Report")
    print("")
    print("                      11 : System Exit")
    print("----------------------------------------------------------------------")
    print("")

    # choice selector

    choice = input("Enter Your Selection : ")

    if choice == "1":
        addCitizen.addCitizen()
    elif choice == "2":
        viewCitizen.viewCitizen()
    elif choice == "3":
        updateCitizen.updateCitizen()
    elif choice == "4":
        deleteCitizen.deleteCitizen()
    elif choice == "5":
        addCandidate.addCandidate()
    elif choice == "6":
        viewCandidate.viewCandidate()
    elif choice == "7":
        updateCandidate.updateCandidate()
    elif choice == "8":
        deleteCandidate.deleteCandidate()
    elif choice == "9":
        viewTotalVotes.viewTotalVotes()
    elif choice == "10":
        barChart.barChart()

    elif choice == "11":
        print("")
        print("Good Bye")
        exit()
    else:
        print("")
        print("                                                      -- Warning --")
        print("                                                 please enter valid input")
        print("                                                      -- Warning --")
        print("")
        adminDashboard()
