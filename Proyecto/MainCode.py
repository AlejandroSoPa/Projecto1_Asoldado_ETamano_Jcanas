import funcions as f # S'importen totes les funcions de l'arxiu funcions.py amb l'alias "f"

adventures = f.get_Adventures_with_Characters() # S'extreu el diccionari adventures
characters = f.getCharacters() # S'extreu el diccionari characters


flag_title = True # variable de control per a mostrar el menú principal
logged_in = False # variable per a canviar la opció de login per una de logout després d'haver iniciat sessió
while flag_title:
    # Pantalla principal que es mostra si no hi ha cap usuari en ús en el moment
    if logged_in == False:
        print(f.title_screen())
        opt = f.getOpt(("\n" + " "*45 + "1) Login" + "\n"
                        + " "*45 + "2) Create User" + "\n"
                        + " "*45 + "3) Replay Adventure" + "\n"
                        + " "*45 + "4) Reports" + "\n"
                        + " "*45 + "5) Exit" + "\n"), " "*45 + "Option: ", [1, 2, 3, 4, 5])
    # Pantalla principal que es mostra si hi ha algun usuari en ús en el moment
    else:
        print(f.title_screen())
        opt = f.getOpt((" " * 45 + "1) Logout" + "\n"
                        + " " * 45 + "2) Create User" + "\n"
                        + " " * 45 + "3) Replay Adventure" + "\n"
                        + " " * 45 + "4) Reports" + "\n"
                        + " " * 45 + "5) Exit" + "\n"), " " * 45 + "Option: ", [1, 2, 3, 4, 5])

    # Opció 1: Login/Logout
    if opt == 1:
        # Si la opció és logout, tanca la sessió de l'usuari en ús i mostra un missatge per pantalla per notificar
        # aquesta acció
        if logged_in:
            print("\nUser " + str(user) + " logged out correctly.")
            user = ""
            password = ""
            f.wait()
            logged_in = False
        # Si la opció és login, demana un usuari i contrasenya, comprova que siguin correctes i si ho són, mostra per
        # pantalla el menú de selecció d'aventura
        else:
            print("\n\n" + "LOGIN".center(50, "="))
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
            flag_play = True
            while flag_play:
                print("\n\n" + f.getFormatedAdventures(adventures))
                id_adv = int(f.getOpt("", "\nWhich Adventure do you want to play? (0 to Go Back) ", [], adventures, [0]))
                if id_adv == 0:
                    flag_play = False
                else:
                    flag_char = True
                    # Una vegada s'hagi seleccionat l'aventura, extreu els diccionaris answers_bystep_adventur i
                    # bystep_adventure de l'aventura seleccionada i mostra la llista de personatges seleccionables
                    while flag_char:
                        answers_bystep_adventure = f.get_answers_bystep_adventure(id_adv)
                        bystep_adventure = f.get_id_bystep_adventure(id_adv)
                        header = adventures[id_adv]["Name"]
                        print("\n\n" + f.getHeader(header) + "\n" +
                              f.getFormatedBodyColumns(("Adventure: ", adventures[id_adv]["Name"]), (18, 80), 2) + "\n" +
                              f.getFormatedBodyColumns(("Description: ", adventures[id_adv]["Description"]), (18, 80), 2) + "\n\n")
                        print("Characters".center(50,"="))
                        for i in adventures[id_adv]["Characters"]:
                            print(str(i).rjust(3) + ") " + characters[i])
                        id_char = int(f.getOpt("", "Choose your character (0 to Go Back): ", adventures[id_adv]["Characters"], {}, [0]))
                        if id_char == 0:
                            flag_char = False
                        else:
                            # Una vegada s'hagi seleccionat el personatge, s'inserta la partida a la base de dades
                            id_game = f.setIdGame()
                            userlist = f.getUserIds()
                            for i in range(len(userlist[0])):
                                if userlist[0][i] == user:
                                    f.insertCurrentGame(userlist[1][i], id_char, id_adv)
                            # S'extreu el primer pas de l'aventura i s'inicia el joc
                            id_step = f.get_first_step_adventure(id_adv)
                            flag_adv = True
                            while flag_adv:
                                # Es mostra per pantalla la capçalera amb el títol de l'aventura i la descripció del pas
                                # actual (substituint %personaje% pel nom del personatge seleccionat)
                                print("\n" + f.getHeader(header) + "\n" +
                                      f.formatText(bystep_adventure[id_step]["Description"].replace("%personaje%", characters[id_char]), 100) + "\n")
                                # Si el pas és un final d'aventura, mostra per pantalla el dibuix de fin() i fa un
                                # commit per confirmar la inserció a la base de dades de la partida i de les opcions
                                # que s'han anat seleccionant
                                if bystep_adventure[id_step]["Final_Step"] == 1:
                                    print(f.fin())
                                    f.commit()
                                    f.wait()
                                    flag_adv = False
                                    flag_char = False
                                    flag_play = False
                                # Si no, es mostren les possibles opcions, i es demana a l'usuari quina opció ha
                                # escollit
                                else:
                                    for i in bystep_adventure[id_step]["answers_in_step"]:
                                        print(f.getFormatedAnswers(i, answers_bystep_adventure[(i, id_step)]["Description"].replace("%personaje%", characters[id_char]), 95, 5))
                                    answer = int(f.getOpt("", " "*5 + "Select option: ", bystep_adventure[id_step]["answers_in_step"]))
                                    # Després d'haver escollit una opció, es desa a la base de dades la decisió de
                                    # l'usuari en la partida actual, es mostra per pantalla la resolució de la opció i
                                    # es repeteix tot el procés per al següent pas en l'aventura
                                    f.InsertCurrentChoice(id_game, answer)
                                    print("\n" + f.formatText(answers_bystep_adventure[(answer, id_step)]["Resolution_answer"], 100))
                                    f.wait()
                                    id_step = answers_bystep_adventure[(answer, id_step)]["Next_Step_Adventure"]

    # Opció 2: Crear Usuari
    elif opt == 2:
        # Demana un usuari i una contrasenya, comprova que els dos siguin correctes i que l'usuari no existeixi a la
        # bbdd, inserta l'usuari amb la seva contrasenya a la bbdd i mostra un missatge per confirmar la inserció
        while True:
            user = input("Username: ")
            if f.UserExists(user):
                print("User already exists")
            elif f.checkUser(user):
                break
        while True:
            password = input("Password: ")
            if f.checkPassword(password):
                break
        f.insertUser(user, password)
        print("User " + user + " created successfuly")
        f.wait()

    # Opció 3: Repetir aventures
    elif opt == 3:
        flag_replay = True
        while flag_replay:
            # Es mostra per pantalla una taula amb totes les partides anteriors. Si s'han enregistrat més de 5 partides,
            # la taula es mostra amb un scroll en el que al insertar "+" o "-" canvia de pàgina.

            # Una vegada s'ha seleccionat la partida a repetir, s'executen la funció getChoices() per extreure la tupla
            # amb les opcions seleccionades d'aquella partida i la funció replay() per recrear la partida en si
            print(f.replay_screen())
            replayAdventures = f.getReplayAdventures()
            if len(replayAdventures) <= 5:
                print("\n" + f.getHeaderForTableFromTuples(("ID", "User", "Adventure", "Character", "Date"), (5, 10, 50, 20, 20), "Adventures"))
                print(f.getTableFromDict(("Username", "Name", "CharacterName", "date"), (10, 50, 20, 20), replayAdventures))
                id_replay = int(f.getOpt("\n",
                                     f.formatText("Which Adventure do you want to replay?\n(0 to Go Back)\n", 120),
                                     [], replayAdventures, [0]))
                if id_replay == 0:
                    flag_replay = False
                else:
                    f.replay(f.getChoices(id_replay), id_replay)
                    flag_replay = False
                    break
            else:
                listScroll = list(replayAdventures.keys())
                scrollPage = 0
                while True:
                    auxDict = {}
                    for i in range((5*(scrollPage+1)-5), (5*(scrollPage+1))):
                        if i >= len(listScroll):
                            break
                        else:
                            auxDict[listScroll[i]] = replayAdventures[listScroll[i]]
                    print("\n" + f.getHeaderForTableFromTuples(("ID", "User", "Adventure", "Character", "Date"), (5, 10, 50, 20, 20), "Adventures"))
                    print(f.getTableFromDict(("Username", "Name", "CharacterName", "date"), (10, 50, 20, 20), auxDict))
                    id_replay = f.getOpt("\n",
                                         f.formatText("Which Adventure do you want to replay?\n(0 to Go Back, + to Go to the Next Page, - to Go to the Previous Page)\n", 100),
                                         [], auxDict, [0, "+", "-"])
                    if id_replay == "+":
                        # Si s'està mostrant l'última pàgina, l'scroll fa que es mostri la primera
                        if (5*(scrollPage+1)) >= len(listScroll):
                            scrollPage = 0
                        else:
                            scrollPage += 1
                    elif id_replay == "-":
                        # Si s'està mostrant la primera pàgina, l'scroll fa que es mostri l'última
                        if scrollPage == 0:
                            scrollPage = len(listScroll)-5
                        else:
                            scrollPage -= 1
                    else:
                        id_replay = int(id_replay)
                        if id_replay == 0:
                            flag_replay = False
                            break
                        else:
                            f.replay(f.getChoices(id_replay), id_replay)
                            flag_replay = False
                            break

    # Opció 4: Reports
    elif opt == 4:
        while True:
            # Es mostra el dibuix de reports i el menú amb les opcions disponibles
            print(f.reports_dibujo())
            opt = int(f.getOpt(("\n\n" + " "*45 + "1) Most Used Answers" + "\n" +
                                " "*45 + "2) Players with most games played" + "\n" +
                                " "*45 + "3) Games Played by User" + "\n" +
                                " "*45 + "4) Go Back"), "\n\n" + "Option: ".rjust(55), [1, 2, 3, 4]))
            if opt == 1:
                # Es defineixen una query que seleccioni les dades de les 5 respostes més utilitzades i la capçalera
                # corresponent
                query = "SELECT concat(a.ID_ADVENTURE, ' - ', a.name) as 'ID AVENTURA - NOMBRE'" \
                        ", concat(s.ID_STEP, ' - ', s.description) as 'ID PASO - DESCRIPCION', " \
                        "concat(o.ID_OPTION, ' - ' , o.description) as 'ID RESPUESTA - DESCRIPCION'" \
                        ", count(r.ID_ROUND) as 'NUMERO DE VECES SELECCIONADA' from ROUND_OPTION r " \
                        "inner join PROJECT_1.OPTION o on o.ID_OPTION = r.ID_OPTION " \
                        "inner join STEP s on s.ID_STEP = o.ID_STEP " \
                        "inner join ADVENTURE a on a.ID_ADVENTURE = s.ID_ADVENTURE " \
                        "group by r.ID_OPTION order by count(r.ID_ROUND) desc limit 5"
                header = "TOP 5 MOST USED ANSWERS"
            elif opt == 2:
                # Es defineixen una query que seleccioni les dades dels 5 usuaris que més han jugat i la capçalera
                # corresponent
                header = "TOP 5 PLAYERS WITH MOST GAMES PLAYED"
                query = "SELECT u.username as 'NOMBRE DE USUARIO', count(r.ID_ROUND) as 'NUMERO DE PARTIDAS' from USER u " \
                        "inner join ROUND r on r.ID_USER = u.ID_USER group by r.ID_USER limit 5"
            elif opt == 3:
                # Es demana un usuari, es comprova que existeixi a la bbdd i si existeix, es defineixen una query que
                # seleccioni les 5 partides més recents de l'usuari i la capçalera corresponent
                print("Which user do you want to see?")
                while True:
                    user = input()
                    if not f.UserExists(user):
                        print("User does not exist")
                    else:
                        break
                header = "LAST 5 GAMES PLAYED BY " + str(user).upper()
                query = "SELECT a.ID_ADVENTURE as ID_ADVENTURE, a.name as NAME, concat(r.date, ' ', r.time) as DATE from " \
                        "USER u inner join ROUND r on r.ID_USER = u.ID_USER " \
                        "inner join ADVENTURE a on a.ID_ADVENTURE = r.ID_ADVENTURE " \
                        "where u.username = '" + str(user) + "' order by r.ID_ROUND desc limit 5"
            elif opt == 4:
                break
            # S'executa la query de l'opció que s'hagi seleccionat i es mostra en forma de taula
            print("\n" + f.getFormatedTable(f.getTable(query), header))
            f.wait()
    else:
        flag_title = False