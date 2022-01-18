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
        flag_play = True
        while flag_play:
            print(f.getFormatedAdventures(adventures))
            id_adv = int(f.getOpt("", "Which Adventure do you want to play? (0 to Go Back) ", [], adventures, [0]))
            if id_adv == 0:
                flag_play = False
            else:
                flag_char = True
                while flag_char:
                    answers_bystep_adventure = f.get_answers_bystep_adventure(id_adv)
                    bystep_adventure = f.get_id_bystep_adventure(id_adv)
                    header = adventures[id_adv]["Name"]
                    print(f.getHeader(header) + "\n" +
                          f.getFormatedBodyColumns(("Adventure: ", adventures[id_adv]["Name"]), (18, 80), 2) + "\n" +
                          f.getFormatedBodyColumns(("Description: ", adventures[id_adv]["Description"]), (18, 80), 2) + "\n\n")
                    print("Characters".center(50,"="))
                    for i in adventures[id_adv]["characters"]:
                        print(str(i).rjust(3) + ") " + characters[i])
                    id_char = int(f.getOpt("", "Choose your character: ", adventures[id_adv]["characters"], {}, [0]))
                    if id_char == 0:
                        flag_char = False
                    else:
                        id_step = f.get_first_step_adventure(id_adv)
                        flag_adv = True
                        while flag_adv:
                            print(f.getHeader(header) + "\n" + f.formatText(bystep_adventure[id_step]["Description"], 100) + "\n")
                            if bystep_adventure[id_step]["Final_Step"] == 1:
                                print(f.fin())
                                f.wait()
                                flag_adv = False
                                flag_char = False
                                flag_play = False
                            else:
                                for i in bystep_adventure[id_step]["answers_in_step"]:
                                    print(f.getFormatedAnswers(i, answers_bystep_adventure[(i, id_step)]["Description"], 95, 5))
                                answer = int(f.getOpt("", " "*5 + "Select option: ", bystep_adventure[id_step]["answers_in_step"]))
                                print(f.formatText(answers_bystep_adventure[(i, id_step)]["Resolution_Answer"]), 100)
                                f.wait()
                                id_step = answers_bystep_adventure[(i, id_step)]["NextStep_Adventure"]







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
        print("User " + user + " created successfuly")
    elif opt == 3:
        print(f.replay())
        replayAdventures = f.getReplayAdventures()

    elif opt == 4:
        print()
    else:
        print()