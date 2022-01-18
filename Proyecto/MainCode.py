import funcions as f

adventures = f.get_Adventures_with_Characters()
characters = f.getCharacters()



flag_title = True

while flag_title:
    print(f.title_screen())
    opt = f.getOpt((" "*45 + "1) Login" + "\n"
                    + " "*45 + "2) Create User" + "\n"
                    + " "*45 + "3) Replay Adventure" + "\n"
                    + " "*45 + "4) Reports" + "\n"
                    + " "*45 + "5) Exit" + "\n"), " "*45 + "Option: ", [1, 2, 3, 4, 5])
    if opt == 1:
        print("LOGIN".center(100, "="))
        while True:
            user = input("Username: ")
            password = input("Password: ")
            login = f.checkUserbbdd(user, password)
            if login == 1:
                break
            elif login == 0:
                print("User doesn't exist")
            else:
                print("Password is incorrect")
        while True:
            print(f.getFormatedAdventures(adventures))
            opt = int(f.getOpt("", "Which Adventure do you want to play? (0 to Go Back) ", [], adventures, [0]))
            if opt == 0:
                break
            else:
                answers_bystep_adventure = f.get_answers_bystep_adventure(opt)
                bystep_adventure = f.get_id_bystep_adventure(opt)


    elif opt == 2:
        while True:
            user = input("Username: ")
            if f.checkUser(user) and not f.UserExists(user):
                break
            elif f.UserExists(user):
                print("User already exists")
        while True:
            password = input("Password: ")
            if f.checkPassword(password):
                break
        print("User " + user + " signed up successfuly")
    elif opt == 3:
        print()
    elif opt == 4:
        print()
    else:
        print()