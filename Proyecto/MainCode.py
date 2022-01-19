import funcions as f

adventures = f.get_Adventures_with_Characters()
characters = f.getCharacters()


flag_title = True
logged_in = False
while flag_title:
    if logged_in == False:
        print(f.title_screen())
        opt = f.getOpt((" "*45 + "1) Login" + "\n"
                        + " "*45 + "2) Create User" + "\n"
                        + " "*45 + "3) Replay Adventure" + "\n"
                        + " "*45 + "4) Reports" + "\n"
                        + " "*45 + "5) Exit" + "\n"), " "*45 + "Option: ", [1, 2, 3, 4, 5])
    else:
        print(f.title_screen())
        opt = f.getOpt((" " * 45 + "1) Logout" + "\n"
                        + " " * 45 + "2) Create User" + "\n"
                        + " " * 45 + "3) Replay Adventure" + "\n"
                        + " " * 45 + "4) Reports" + "\n"
                        + " " * 45 + "5) Exit" + "\n"), " " * 45 + "Option: ", [1, 2, 3, 4, 5])
    if opt == 1:
        if logged_in == False:
            print("LOGIN".center(50, "="))
            while True:
                user = input("\nUsername: ")
                password = input("Password: ")
                login = f.checkUserbbdd(user, password)
                if login == 1:
                    break
                elif login == 0:
                    print("\nUser doesn't exist")
                else:
                    print("\nPassword is incorrect")
            logged_in = True
        else:
            print("User " + str(user) + " logged out correctly.")
            user = ""
            password = ""
            f.wait()
            logged_in = False
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
                    print(answers_bystep_adventure)
                    print(bystep_adventure)
                    header = adventures[id_adv]["Name"]
                    print(f.getHeader(header) + "\n" +
                          f.getFormatedBodyColumns(("Adventure: ", adventures[id_adv]["Name"]), (18, 80), 2) + "\n" +
                          f.getFormatedBodyColumns(("Description: ", adventures[id_adv]["Description"]), (18, 80), 2) + "\n\n")
                    print("Characters".center(50,"="))
                    for i in adventures[id_adv]["Characters"]:
                        print(str(i).rjust(3) + ") " + characters[i])
                    id_char = int(f.getOpt("", "Choose your character: ", adventures[id_adv]["Characters"], {}, [0]))
                    if id_char == 0:
                        flag_char = False
                    else:
                        id_game = f.setIdGame()
                        userlist = f.getUserIds()
                        for i in len(userlist[0]):
                            if userlist[0][i] == user:
                                f.insertCurrentGame(userlist[0][i], id_char, id_adv)
                        id_step = f.get_first_step_adventure(id_adv)
                        flag_adv = True
                        while flag_adv:
                            print(f.getHeader(header) + "\n" + f.formatText(bystep_adventure[id_step]["Description"], 100) + "\n")
                            if bystep_adventure[id_step]["Final_Step"] == 1:
                                print(f.fin())
                                f.commit()
                                f.wait()
                                flag_adv = False
                                flag_char = False
                                flag_play = False
                            else:
                                for i in bystep_adventure[id_step]["answers_in_step"]:
                                    print(f.getFormatedAnswers(i, answers_bystep_adventure[(i, id_step)]["Description"], 95, 5))
                                answer = int(f.getOpt("", " "*5 + "Select option: ", bystep_adventure[id_step]["answers_in_step"]))
                                f.InsertCurrentChoice(id_game, answer)
                                print(f.formatText(answers_bystep_adventure[(i, id_step)]["Resolution_answer"], 100))
                                f.wait()
                                id_step = answers_bystep_adventure[(i, id_step)]["Next_Step_Adventure"]

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
        f.insertUser(user, password)
        print("User " + user + " created successfuly")
        f.wait()
    elif opt == 3:
        print(f.replay())
        replayAdventures = f.getReplayAdventures()
        if len(replayAdventures) <= 5:
            print(f.getTableFromDict(("Username", "Name", "CharacterName", "date"), (10, 50, 20, 20), replayAdventures))
        else:
            listScroll = list(replayAdventures.keys())
            scrollPage = 1
            while True:
                auxDict = {}
                for i in range((1*scrollPage)-1, (5*scrollPage)):
                    if i >= len(listScroll):
                        break
                    else:
                        auxDict[i] = replayAdventures[i]
                print(f.getTableFromDict(("Username", "Name", "CharacterName", "date"), (10, 50, 20, 20), auxDict))
                id_replay = f.getOpt("\n",
                                     "Which Adventure do you want to replay (0 to Go Back, + to Go to the Next Page, - to Go to the Previous Page) ",
                                     [], auxDict, [0, "+", "-"])
                if id_replay == "+":
                    if (5*scrollPage)-1 >= len(listScroll):
                        scrollPage = 1
                    else:
                        scrollPage += 1
                elif id_replay == "-":
                    if scrollPage == 1:
                        scrollPage = len(listScroll)-5
                    else:
                        scrollPage -= 1
                else:
                    id_replay = int(id_replay)
                    if id_replay == 0:
                        break
                    else:
                        f.replay(f.getChoices(id_replay))





    elif opt == 4:
        while True:
            print(f.reports_dibujo())
            opt = int(f.getOpt(("\n\n" + "1) Most Used Answers".center(100) + "\n" +
                                "2)Players with most games played".center(100) + "\n" +
                                "3) Games Played by User".center(100) +
                                "4) Go Back".center(100)), "\n\n" + "Option: ".center(100), [1, 2, 3, 4]))
            if opt == 1:
                query = "SELECT concat(a.ID_ADVENTURE, ' - '  a.name) as ' ID AVENTURA - NOMBRE, " \
                        "concat(s.ID_STEP, ' - ', s.description) as 'ID PASO - DESCRIPCION', " \
                        "concat(o.ID_OPTION, ' - ' , o.description) as 'ID RESPUESTA - DESCRIPCION', " \
                        "count(r.ID_GAME) as 'NUMERO DE VECES SELECCIONADA" \
                        "from ROUND_OPTION r inner join PROJECT_1.OPTION o on o.ID_OPTION = r.ID_OPTION " \
                        "inner join STEP s on s.ID_STEP = o.ID_STEP " \
                        "inner join ADVENTURE a on a.ID_ADVENTURE = s.ID_ADVENTURE " \
                        "group by r.ID_OPTION limit 5"
                header = "MOST USED ANSWERS"
            elif opt == 2:
                header = "PLAYERS WITH MOST GAMES PLAYED"
                query = "SELECT u.username as 'NOMBRE DE USUARIO', count(r.ID_ROUND) as 'NUMERO DE PARTIDAS' from USER u " \
                        "inner join ROUND r on r.ID_USER = u.ID_USER group by r.ID_USER limit 5"
            elif opt == 3:
                print("Which user do you want to see?")
                while True:
                    user = input()
                    if f.checkUserbbdd(user, " ") == 0:
                        print("User does not exist")
                    else:
                        break
                header = "GAMES PLAYED BY " + str(user).upper()
                query = "SELECT a.ID_ADVENTURE as ID ADVENTURE, a.name as NAME concat(r.date, ' ', r.time) as DATE from " \
                        "ROUND USER u inner join ROUND r on r.ID_USER = u.ID_USER " \
                        "inner join ADVENTURE a on a.ID_ADVENTURE = r.ID_ADVENTURE where u.username = " + str(user)
            elif opt == 4:
                break
            f.getFormatedTable(f.getTable(query), header)
    else:
        flag_title = False