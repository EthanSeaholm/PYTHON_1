#

import sqlite3

try:
    sqliteConnection = sqlite3.connect('ConstructCo.db') # insert the db name of your choice
    cursor = sqliteConnection.cursor()
    print("Database Successfully Connected to SQLite")

    '''sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)
    cursor.close()'''

    def main():
        while True:
            menu()
            answer = input('Enter your choice number: ')
            print()
            if answer == '1':
                employee()
            elif answer =='2':
                job()
            elif answer == '3':
                query()
            elif answer == '4':
                break

    def employee():
        name = input ("Enter employee last name: ")
        query = "SELECT * FROM EMPLOYEE WHERE EMP_LNAME = '" + name + "'"
        cursor.execute(query)
        query_result = cursor.fetchall()
        print ("ID\t\tLast Name\tFirst Name\tMI\t\tHire Date\t\tJob Code\tYears of Employment")
        for row in query_result:
            print (f"{row[0]}\t\t{row[1]}\t\t{row[2]}\t\t{row[3]}\t\t{row[4]}\t\t{row[5]}\t\t{row[6]}")

    def job():
        job = input ("Enter job title: ")
        query = "SELECT * FROM JOB WHERE JOB_DESCRIPTION = '" + job + "'"
        cursor.execute(query)
        query_result = cursor.fetchall()
        print ("ID\t\tDescription\tCharging Per Hour\tLast Update")
        for row in query_result:
            print (f"{row[0]}\t\t{row[1]}\t\t{row[2]}\t\t{row[3]}")

    def query():
        your_query = input("Enter your own query: ")
        query = your_query
        cursor.execute(query)
        query_result = cursor.fetchall()
        
    def menu():
        print()
        print('1- Search Employees by name')
        print('2- Search job by title')
        print('3- Enter your own query')
        print('4- Exit\n')

    main()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")

#