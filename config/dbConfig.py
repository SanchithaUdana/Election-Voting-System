import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="electionVotingSystem",
    port=8889
)

if mydb.is_connected():
    print("🛜 DataBase Connected 🛜")
    print("")
else:
    print("🚫 DB error 🚫")
    print("")
