import pymysql # S'importa la llibreria pymysql, que ens permetrà accedir a la base de dades des de l'arxiu .py

conn = pymysql.connect(host="20.105.176.24", user="etamano", password="Etamano1!", db="PROJECT_1")
print(conn)
# Es connecta de forma remota a la base de dades ubicada a la màquina virtual
db = conn.cursor() # Es configura una variable per a utilitzar-la posteriorment per executar comandes al MySQL i
                   # treballar amb la base de dades


def get_answers_bystep_adventure(id_adventure):
    # Funció que, a partir de la informació de la base de dades, crea el diccionari answers_bystep_adventure, el qual
    # conté totes les respostes possibles a cada pas pertinent a l'aventura escollida
    query = "SELECT o.ID_OPTION, s.ID_STEP, o.description, o.answer, o.next_step from ADVENTURE a inner join STEP s on " \
            "s.ID_ADVENTURE = a.ID_ADVENTURE inner join PROJECT_1.OPTION o on o.ID_STEP = s.ID_STEP where a.ID_ADVENTURE = " \
            + str(id_adventure)
    db.execute(query)
    data = db.fetchall()
    dict = {}
    for i in data:
        dict[(i[0], i[1])] = {"Description": i[2], "Resolution_answer": i[3], "Next_Step_Adventure": i[4]}
    return dict

def get_id_bystep_adventure(id_adventure):
    # Funció que, a partir de la informació de la base de dades, crea el diccionari answers_bystep_adventure, el qual
    # conté tots els passos que formen l'aventura que hagi escollit el jugador
    query = "SELECT s.ID_STEP, s.description, s.adventure_end, o.ID_OPTION from ADVENTURE a inner join STEP s on " \
            "a.ID_ADVENTURE = s.ID_ADVENTURE inner join PROJECT_1.OPTION o on o.ID_STEP = s.ID_STEP where a.ID_ADVENTURE = " + str(id_adventure)
    db.execute(query)
    data = db.fetchall()
    dict = {}
    query = "SELECT s.ID_STEP, s.description, s.adventure_end from ADVENTURE a inner join STEP s on " \
            "a.ID_ADVENTURE = s.ID_ADVENTURE where s.adventure_end = 1 and a.ID_ADVENTURE = " + str(id_adventure)
    db.execute(query)
    data_end = db.fetchall()
    for i in data:
        if i[0] not in dict.keys():
            dict[i[0]] = {"Description": i[1], "Final_Step": 0}
            aux = []
            for j in data:
                if j[0] == i[0]:
                    aux.append(j[3])
            dict[i[0]]["answers_in_step"] = tuple(aux)
    for i in data_end:
        dict[i[0]] = {"Description": i[1], "Final_Step": 1, "answers_in_step": ()}
    return dict


def get_first_step_adventure(id_adventure):
    # Funció que busca el pas inicial de l'aventura que s'estigui jugant
    query = "SELECT min(ID_STEP) from STEP where ID_ADVENTURE = " + str(id_adventure)
    db.execute(query)
    data = db.fetchall()
    return data[0][0]


def get_Adventures_with_Characters():
    # Funció que extreu totes les aventures amb les seves descripicons i els personatges que es puguin utilitzar en cada
    # aventura
    query = "SELECT a.ID_ADVENTURE, a.name, a.description, c.ID_CHARACTER from ADVENTURE a inner join " \
            "CHARACTER_ADVENTURE c on a.ID_ADVENTURE = c.ID_ADVENTURE ORDER BY a.ID_ADVENTURE asc"
    db.execute(query)
    data = db.fetchall()
    dict = {}
    for i in data:
        if i[0] not in dict.keys():
            dict[i[0]] = {"Name": i[1], "Description": i[2]}
            aux=[]
            for j in data:
                if j[0] == i[0]:
                    aux.append(j[3])
            dict[i[0]]["Characters"] = aux
    return dict


def getCharacters():
    # Funció que extreu tots els personatges registrats a la base de dades
    query = "SELECT ID_CHARACTER, name from PROJECT_1.CHARACTER"
    db.execute(query)
    data = db.fetchall()
    dictCharacters = {}
    for i in range(len(data)):
        dictCharacters[data[i][0]] = data[i][1]
    return dictCharacters


def getReplayAdventures():
    # Funció que obté totes les partides que s'han jugat anteriorment
    query = "SELECT r.ID_ROUND, u.ID_USER, u.username, a.ID_ADVENTURE, a.name, r.date, r.time" \
            ", c.ID_CHARACTER, c.name from ROUND r inner join USER u on u.ID_USER = r.ID_USER inner join ADVENTURE a on " \
            "a.ID_ADVENTURE = r.ID_ADVENTURE inner join PROJECT_1.CHARACTER c on c.ID_CHARACTER = r.ID_CHARACTER order " \
            "by r.date desc, r.time desc"
    db.execute(query)
    data = db.fetchall()
    dict = {}
    for i in data:
        dict[i[0]] = {"idUser": i[1], "Username": i[2], "idAdventure": i[3], "Name": i[4], "date": str(i[5]) + " " + str(i[6]), "idCharacter": i[7], "CharacterName": i[8]}
    return dict



def getChoices(id_round):
    # Funció que, una vegada s'ha escollit quina partida repetir, extreu una tupla de tuples amb els passos que s'han
    # recorregut i les respostes que ha escollit el jugador en cada moment
    query = "SELECT s.ID_STEP, o.ID_OPTION from ROUND r inner join ROUND_OPTION e on r.ID_ROUND = e.ID_ROUND inner" \
            "join PROJECT_1.OPTION o on o.ID_OPTION = e.ID_OPTION inner join STEP s on s.ID_STEP = o.ID_STEP where r.ID_ROUND = " \
            + str(id_round)
    db.execute(query)
    data = db.fetchall()
    choices = []
    for i in data:
        choices.append(tuple([i[0], i[1]]))
    return tuple(choices)



def getIdGames():
    # Funció que obté una tupla amb les IDs de les partides jugades anteriorment en ordre descendent per després
    # utilitzar aquesta tupla per obtenir la ID de la partida a insertar en la base de dades
    query = "SELECT ID_ROUND from ROUND order by ID_ROUND desc"
    db.execute(query)
    data = db.fetchall()
    aux = []
    for i in data:
        aux.append(i[0])
    return tuple(aux)


def insertCurrentGame(idUser, idChar, idAdventure):
    # Funció que inserta la partida que s'està jugant en el moment a la base de dades. En comptes d'utilitzar les
    # funcions getIdGames() i setIdGame() per obtenir la ID de la partida, la base de dades està configurada de forma
    # que les IDs s'insertin de forma automàtica
    query = "select count(ID_ROUND) + 1 from ROUND"
    db.execute(query)
    data = db.fetchall()
    auto_inc = data[0][0]
    query = "ALTER TABLE ROUND auto_increment = " + str(auto_inc)
    db.execute(query)
    query = "INSERT INTO ROUND (ID_USER, ID_CHARACTER, ID_ADVENTURE, date, time, usercreate, datecreated) VALUES (" + \
            str(idUser) + ", " + str(idChar) + ", " + str(idAdventure) + ", current_date(), current_time(), current_user(), current_timestamp())"
    db.execute(query)



def getUsers():
    # Funció que crea un diccionari contenent tots els usuaris registrats amb les seves respectives contrasenyes i IDs
    query = "SELECT ID_USER, username, password from USER"
    db.execute(query)
    data = db.fetchall()
    aux = {}
    for i in range(len(data)):
        aux[data[i][1]] = {"password": data[i][2], "idUser": data[i][0]}
    return aux


def getUserIds():
    # Funció que, a partir de la funció getUsers(), obté una llista de llistes contenint els usuaris registrats i les
    # seves respectives IDs
    dict = getUsers()
    listUsers = list(dict.keys())
    listIds = []
    for i in dict:
        listIds.append(dict[i]["idUser"])
    return [listUsers, listIds]


def insertUser(user, password):
    # Funció que inserta a la base de dades l'usuari creat amb l'opció de Create User
    query = "select count(ID_USER) + 1 from USER"
    db.execute(query)
    data = db.fetchall()
    auto_inc = data[0][0]
    query = "ALTER TABLE USER auto_increment = " + str(auto_inc)
    db.execute(query)
    query = "INSERT INTO USER (username, password, usercreate, datecreated) VALUES ('" + str(user) + "', '" + \
            str(password) + "', current_user(), current_timestamp())"
    db.execute(query)
    db.execute("commit")


def getTable(query):
    # Funció que, donada una query, crea una tupla de tuples amb el nom de les columnes i les dades d'aquestes per tal
    # de després mostrar-la com a una taula
    db.execute(query)
    colname = db.description
    data = db.fetchall()
    list = []
    aux = []
    for i in colname:
        aux.append(i[0])
    list.append(tuple(aux))
    for i in data:
        list.append(i)
    return tuple(list)


def checkUserbbdd(user, password):
    # Funció que comprova que l'usuari donat existeixi a la base de dades i que la contrasenya insertada sigui correcta
    query = "SELECT username, password from USER"
    db.execute(query)
    usuaris = db.fetchall()
    for i in usuaris:
        if i[0] == user and i[1] == password:
            return 1
        elif i[0] == user and i[1] != password:
            return -1
    return 0



# Funcions Auxiliars


def setIdGame():
    # Funció que retorna la ID d'una partida nova per a poder insertar-la a la base de dades
    tupla = getIdGames()
    if len(tupla) == 0:
        return 1
    else:
        return tupla[0] + 1


def InsertCurrentChoice(idGame, answer):
    # Funció que inserta a la base de dades la opció que ha escollit el jugador en una determinada partida
    query = "INSERT INTO ROUND_OPTION (ID_ROUND, ID_OPTION, usercreate, datecreated) VALUES (" + str(idGame) + ", " \
            + str(answer) + ", current_user(), current_timestamp())"
    db.execute(query)


def formatText(text, lenLine, split="\n"):
    # Funció que modifica una cadena de texte per a que tingui com a màxim una longitud de línia determinada
    text = text.split("\n")
    string = ""
    for i in text:
        aux = []
        auxFormatText(str(i), aux, lenLine)
        if len(str(i)) > lenLine:
            for i in aux:
                if aux != aux[len(aux) - 1]:
                    string += i + str(split)
        else:
            string += i
        string += "\n"
    return string


def getHeader(text):
    # Funció que crea una capçalera a partir del text a insert dins d'aquesta
    return ("*"*100 + "\n" + text.center(100,"=") + "\n" + "*"*100)



def getFormatedBodyColumns(tupla_texts, tupla_sizes, margins = 0):
    # Funció que, utilitzant FormatText, modifica un nombre de paràgrafs per a que es puguin mostrar amb un format de
    # columnes
    aux = []
    for i in range(len(tupla_texts)):
        aux.append(formatText(str(tupla_texts[i]), tupla_sizes[i]))
    maxfiles = 0
    for i in range(len(aux)):
        if len(aux[i]) > len(aux[maxfiles]):
            maxfiles = i
    string = ""
    for i in range(len(aux[maxfiles])):
        for j in range(len(aux)):
            if len(aux[j])-1 < i:
                string += " "*(tupla_sizes[j]+margins)
            else:
                string += aux[j][i].ljust(tupla_sizes[j]) + " "*margins
        string += "\n"
    return string



def getFormatedAdventures(adventures):
    # Funció que, a partir del diccionari adventures, crea una taula per poder mostrar les diferents aventures amb les
    # seves descripcions
    string = ("Adventures").center(100, "=") + "\n" + "Id".ljust(10) + "Adventure".ljust(40) + "Description".ljust(50) \
             + "\n" + ("*"*100) + "\n"
    for i in adventures.keys():
        string += getFormatedBodyColumns((i, adventures[i]["Name"], adventures[i]["Description"]), (8, 38, 50), 2)
    return string


def getFormatedAnswers(idAnswer, text, lenLine, leftMargin=0):
    # Funció per a poder mostrar les opcions de l'aventura amb el format "ID d'opció) descripció de l'opció" sense que
    # aquestes es surtin dels límits de la pantalla
    if len(text) < lenLine:
        return(" "*leftMargin + str(idAnswer) + ") " + text)
    else:
        text = formatText(text, lenLine).split("\n")
        string = (" "*leftMargin + str(idAnswer) + ") " + text[0])
        for i in text[1:]:
            string += "\n" + " "*(leftMargin+len(str(idAnswer) + ") ")) + i
        return string


def getHeaderForTableFromTuples(t_name_columns, t_size_columns, title=""):
    # Funció que obté la capçalera d'una taula, amb un títol (si té) i els noms de les columnes
    total_size = 0
    for i in t_size_columns:
        total_size += i
    string = (str(title).center(total_size,"=") + "\n")
    for i in range(len(t_size_columns)):
         string += t_name_columns[i].ljust(t_size_columns[i])
    string += ("\n" + "*"*total_size)
    return string


def getTableFromDict(tuple_of_keys, weight_of_columns, dict_of_data):
    # Funció que obté les dades d'un diccionari i les retorna amb un format per poder mostrar-les en una taula
    keys = dict_of_data.keys()
    string = ""
    for i in keys:
        string += str(i).ljust(5)
        for j in range(len(tuple_of_keys)):
            string += str(dict_of_data[i][tuple_of_keys[j]]).ljust(weight_of_columns[j])
        string += "\n"
    return string


def getOpt(textOpts="",inputOptText="",rangeList=[],dictionary={},exceptions=[]):
    # Funció per a mostrar les opcions dels menus i les seleccions i demanar la opció escollida
    print(textOpts)
    while True:
        opt = input(inputOptText)
        if opt.isdigit():
            opt = int(opt)
        if opt in rangeList or opt in dictionary or opt in exceptions:
            return opt
        else:
            print("Option is not valid")



def getFormatedTable(queryTable, title=""):
    # Funció que utilitza una tupla de tuples obtinguda amb la funció getTable() o similar i crea una taula que es pugui
    # mostrar per pantalla
    list_sizes = []
    for i in range(len(queryTable[0])):
        list_sizes.append(120//len(queryTable[0]))
    tupla_sizes = tuple(list_sizes)
    string = getHeaderForTableFromTuples(queryTable[0], tupla_sizes) + "\n"
    for i in range(1, len(queryTable)):
        string += getFormatedBodyColumns(queryTable[i], tupla_sizes) + "\n"
    return string


def checkPassword(password):
    # Funció que comprova que la contrasenya creada compleixi les restriccions
    if len(password) < 8:
        print("Password is too short")
        return False
    else:
        blank = False
        ucase = False
        lcase = False
        num = False
        special = False
        for i in password:
            if i == " ":
                blank = True
                break
            elif i.islower():
                lcase = True
            elif i.isupper():
                ucase = True
            elif i.isdigit():
                num = True
            elif i.isalnum() == False:
                special = True

        if blank == True:
            print("Password cannot contain blank spaces")
            return False
        elif lcase == False:
            print("Password must contain at least one lowercase letter")
            return False
        elif ucase == False:
            print("Password must contain at least one uppercase letter")
            return False
        elif num == False:
            print("Password must contain at least one number")
            return False
        elif special == False:
            print("Password must contain at least one special character")
            return False
        else:
            return True


def checkUser(user):
    # Funció que comprova que el nom d'usuari compleixi les restriccions
    if len(user) < 6:
        print("Username is too short")
        return False
    elif len(user) > 10:
        print("Username is too long")
        return False
    else:
        accent = False
        for i in user:
            if str(i).lower() == "é" or str(i).lower() == "è" or str(i).lower() == "à" or str(i).lower() == "á" or \
                    str(i).lower() == "í" or str(i).lower() == "ì" or str(i).lower() == "ó" or str(i).lower() == "ò" or \
                    str(i).lower() == "ú" or str(i).lower() == "ù" or str(i).lower() == "ñ" or str(i).lower() == "ç":
                print("a")
                accent = True
                break
        if accent or user.isalnum() == False:
            print("Username cannot contain special characters or accents")
            return False
        else:
            return True


def UserExists(user):
    # Funció que comprova si un usuari creat ja existeix a la base de dades
    check = checkUserbbdd(user, " ")
    if check == 0:
        return False
    else:
        return True


def replay(choices):
    # Funció que, a partir de la tupla choices, repeteix una partida jugada anteriorment
    query = "SELECT a.name from ADVENTURE a inner join STEP s on s.ID_ADVENTURE = a.ID_ADVENTURE where s.ID_STEP = " + \
            str(choices[0][0])
    db.execute(query)
    data = db.fetchall()
    title = data[0][0]
    for i in choices:
        query = "SELECT description from STEP where ID_STEP = " + str(i[0])
        db.execute(query)
        data = db.fetchall()
        text = data[0][0]
        print(getHeader(title) + "\n" + formatText(text, 100) + "\n")
        query = "SELECT ID_OPTION, description from PROJECT1_OPTION where ID_STEP = " + str(i[0])
        db.execute(query)
        data = db.fetchall()
        for j in data:
            print(getFormatedAnswers(j[0], j[1], 95, 5))
        print("\n")
        wait()
        print("\n" + "Option " + str(i[1]) + " selected.")
        query = "SELECT answer from PROJECT_1.OPTION where ID_OPTION = " + str(i[1])
        db.execute(query)
        data = db.fetchall()
        answer = data[0][0]
        print(formatText(answer, 100))


# Altres funcions que no apareixen al document informatiu


def auxFuncGetBlankSpace(text):
    # Funció que bus
    if text[len(text)-1] != " ":
        return auxFuncGetBlankSpace(text[:len(text)-1])
    else:
        return text


def auxFormatText(text, list, size, start = 0):
    if start + size >= len(text):
        list.append(text[start:])
        return list
    else:
        section = auxFuncGetBlankSpace(text[start:start+size])
        list.append(section[:len(section)-1])
        auxFormatText(text, list, size, start + len(section))


def title_screen():
    return ("\n" + "*"*100 + "\n" +
          "*" + "  _____ _                           __     __                 _____ _                   ".center(98) + "*" + "\n" +
          "*" + " / ____| |                          \ \   / /                / ____| |                  ".center(98) + "*" +"\n" +
          "*" + "| |    | |__   ___   ___  ___  ___   \ \_/ /__  _   _ _ __  | (___ | |_ ___  _ __ _   _ ".center(98) + "*" + "\n" +
          "*" + "| |    | '_ \ / _ \ / _ \/ __|/ _ \   \   / _ \| | | | '__|  \___ \| __/ _ \| '__| | | |".center(98) + "*" + "\n" +
          "*" + "| |____| | | | (_) | (_) \__ \  __/    | | (_) | |_| | |     ____) | || (_) | |  | |_| |".center(98) + "*" + "\n" +
          "*" + " \_____|_| |_|\___/ \___/|___/\___|    |_|\___/ \__,_|_|    |_____/ \__\___/|_|   \__, |".center(98) + "*" + "\n" +
          "*" + "                                                                                   __/ |".center(98) + "*" + "\n" +
          "*" + "                                                                                  |___/ ".center(98) + "*" + "\n" +
          "*" + " "*98 + "*" + "\n" +
          "*" + "=" * 98 + "*" + "\n" +
          "*" + " " * 98 + "*" + "\n" +
          "*" + "              _   _                               ".center(98) + "*" + "\n" +
          "*" + "             | | | |                              ".center(98) + "*" + "\n" +
          "*" + "   __ _  __ _| |_| |_ ___    _ __   ___ _ __ ___  ".center(98) + "*" + "\n" +
          "*" + "  / _` |/ _` | __| __/ _ \  | '_ \ / _ \ '__/ _ \ ".center(98) + "*" + "\n" +
          "*" + " | (_| | (_| | |_| || (_) | | | | |  __/ | | (_) |".center(98) + "*" + "\n" +
          "*" + "  \__, |\__,_|\__|\__\___/  |_| |_|\___|_|  \___/ ".center(98) + "*" + "\n" +
          "*" + "   __/ |                                          ".center(98) + "*" + "\n" +
          "*" + "  |___/                                           ".center(98) + "*" + "\n" +
          "*"*100 + "\n")

def estrellas():
    return ("\n\n" +
            " __/\____/\____/\____/\____/\____/\____/\____/\____/\____/\____/\____/\__ ".center(100) + "\n" +
            " \    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    / ".center(100) + "\n" +
            " /_  _\/_  _\/_  _\/_  _\/_  _\/_  _\/_  _\/_  _\/_  _\/_  _\/_  _\/_  _\ ".center(100) + "\n" +
            "   \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/   ".center(100) + "\n\n")


def reports_dibujo():
    return (estrellas() +
            " ____                        _        ".center(100) + "\n" +
            "|  _ \ ___  _ __   ___  _ __| |__ __  ".center(100) + "\n" +
            "| |_) / _ \| '_ \ / _ \| '__| __/ __| ".center(100) + "\n" +
            "|  _ <  __/| |_) | (_) | |  | |_\__ \ ".center(100) + "\n" +
            "|_| \_\___|| .__/ \___/|_|   \__|___/ ".center(100) + "\n" +
            "           |_|                        ".center(100) + "\n" +
            estrellas())


def replay():
    return (estrellas()+ "\n" +
            " _____      _              __     __               ".center(100) + "\n" +
            "|  __ \    | (_)           \ \   / /               ".center(100) + "\n" +
            "| |__) |___| |___   _____   \ \_/ /__  _   _ _ __  ".center(100) + "\n" +
            "|  _  // _ \ | \ \ / / _ \   \   / _ \| | | | '__| ".center(100) + "\n" +
            "| | \ \  __/ | |\ V /  __/    | | (_) | |_| | |    ".center(100) + "\n" +
            "|_|  \_\___|_|_| \_/ \___|    |_|\___/ \__,_|_|    ".center(100) + "\n" +
            "             _                 _                   ".center(100) + "\n" +
            "    /\      | |               | |                  ".center(100) + "\n" +
            "   /  \   __| |_   _____ _ __ | |_ _   _ _ __ ___  ".center(100) + "\n" +
            "  / /\ \ / _` \ \ / / _ \ '_ \| __| | | | '__/ _ \ ".center(100) + "\n" +
            " / ____ \ (_| |\ V /  __/ | | | |_| |_| | | |  __/ ".center(100) + "\n" +
            "/_/    \_\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___| ".center(100) + "\n" +
            estrellas())

def fin():
    return ("                                _____ ___ _   _                                 ".center(100) + "\n" +
            "__/\____/\____/\____/\____/\__ |  ___|_ _| \ | | __/\____/\____/\____/\____/\__ ".center(100) + "\n" +
            "\    /\    /\    /\    /\    / | |_   | ||  \| | \    /\    /\    /\    /\    / ".center(100) + "\n" +
            "/_  _\/_  _\/_  _\/_  _\/_  _\ |  _|  | || |\  | /_  _\/_  _\/_  _\/_  _\/_  _\ ".center(100) + "\n" +
            "  \/    \/    \/    \/    \/   |_|   |___|_| \_|   \/    \/    \/    \/    \/   ".center(100))


def commit():
    db.execute("commit")


def wait():
    wait = input("\nPress ENTER to continue: ")

