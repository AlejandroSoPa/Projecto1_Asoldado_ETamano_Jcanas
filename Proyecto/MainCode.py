from funcions import *
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="ErikTamaño",
    password="admin123",
    database="hr"
)

flag_0 = True
#Username 6 y 10 caracteres
while flag_0:
    print("*"*100 + "\n" +
          "*" + "  _____ _                           __     __                 _____ _                   ".center(98) + "*" + "\n" +
          "*" + " / ____| |                          \ \   / /                / ____| |                  ".center(98) + "*" +"\n" +
          "*" + "| |    | |__   ___   ___  ___  ___   \ \_/ /__  _   _ _ __  | (___ | |_ ___  _ __ _   _ ".center(98) + "*" + "\n" +
          "*" + "| |    | '_ \ / _ \ / _ \/ __|/ _ \   \   / _ \| | | | '__|  \___ \| __/ _ \| '__| | | |".center(98) + "*" + "\n" +
          "*" + "| |____| | | | (_) | (_) \__ \  __/    | | (_) | |_| | |     ____) | || (_) | |  | |_| |".center(98) + "*" + "\n" +
          "*" + " \_____|_| |_|\___/ \___/|___/\___|    |_|\___/ \__,_|_|    |_____/ \__\___/|_|   \__, |".center(98) + "*" + "\n" +
          "*" + "                                                                                   __/ |".center(98) + "*" + "\n" +
          "*" + "                                                                                  |___/ ".center(98) + "*" + "\n" +
          "*"*100
          + "\n\n"
          + " "*45 + "1) Login" + "\n"
          + " "*45 + "2) Create User" + "\n"
          + " "*45 + "3) Replay Adventure" + "\n"
          + " "*45 + "4) Reports" + "\n"
          + " "*45 + "5) Exit" + "\n")


    option = input(" "*45 + "Option: ")
    try:
        option = int(option)
        if option < 1 or option > 5:
            raise
    except:
        print("Option isn't valid".center(100))
        wait = input("Press ENTER to continue".center(100))

    if option == 1:
        print("ª")
    elif option == 2:
        print(getHeader("CREATE USER"))
        while True:
            username = input("\n" + "Username: ")
            if len(username) < 6:
                print("Username is too short")
            elif len(username) > 10:
                print("Username is too long")
            elif username.isalnum() == False:
                print("Username cannot contain special characters")
            else:
                break



        if checkUserbbdd(username, password) != 0:
            print("User already exists")
        else:
            InsertUser(0, username, password)
            print("User created")