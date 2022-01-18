import datetime
import pymysql

conn = pymysql.connect(host="20.105.176.24", user="etamano", password="Etamano1!", db="PROJECT_1")
db = conn.cursor()


def get_answers_bystep_adventure(id_adventure):
    query = "SELECT id_option, id_STEP, description, answer, next_step from ADVENTURE where id_adventure = " + id_adventure
    db.execute(query)
    data = db.fetchall()
    dict = {}
    for i in data:
        dict[(i[0], i[1])] = {"Description": i[2], "Resolution_answer": i[3], "Next_Step_Adventure": i[4]}
    return dict

def get_id_bystep_adventure(id_adventure):
    query = "SELECT s.id_step, s.description, s.adventure_end, o.id_option from ADVENTURE a inner join STEP s on " \
            "a.id_adventure = s.ID_ADVENTURE inner join OPTION o on o.ID_STEP = s.id_step where a.adventure_id = " + str(id_adventure)
    db.execute(query)
    data = db.fetchall()
    dict = {}
    for i in data:
        if i[0] not in dict.keys():
            dict[i[0]] = {"Description": i[1], "Final_Step": i[2]}
            aux = []
            for j in data:
                if j[0] == i[0]:
                    aux.append(j[3])
            dict[i[0]]["answers_in_step"] = tuple(aux)
    return dict


def get_Adventures_with_Characters():
    query = "SELECT a.id_adventure, a.name, a.description, c.id_character from ADVENTURE a inner join CHARACTER_ADVENTURE c on a.id_adventure = c.id_adventure"
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
    query = "SELECT id_character, name from PROJECT_1.CHARACTER"
    db.execute(query)
    data = db.fetchall()
    print(data)
    dictCharacters = {}
    for i in range(len(data)):
        dictCharacters[data[i][0]] = data[i][1]
    return dictCharacters


def getChoices(id_adventure):
    return (get_id_bystep_adventure(id_adventure), get_answers_bystep_adventure(id_adventure))



def getIdGames():
    query = "SELECT id_round from ROUND order by id_round desc"
    db.execute(query)
    data = db.fetchall()
    aux = []
    for i in data:
        aux.append(i)
    return tuple(aux)


def insertCurrentGame(idGame, idUser, idChar, idAdventure):
    query = "INSERT INTO ROUND (id_round, ID_USER, ID_CHARACTER, ID_ADVENTURE, date, time, usercreate) VALUES (" + \
            str(idGame) + ", " + str(idUser) + ", " + str(idChar) + ", " + str(idAdventure) + ", " + str(datetime.date) + ", " + str(datetime.time) + ", etamano)"
    db.execute(query)


def getUsers():
    query = "SELECT id_user, username, password from USER"
    db.execute(query)
    data = db.fetchall()
    print(data)
    aux = {}
    for i in range(len(data)):
        aux[data[i][1]] = {"password": data[i][2], "idUser": data[i][0]}
    return aux


def getUserIds():
    dict = getUsers()
    listUsers = list(dict.keys())
    listIds = []
    for i in dict:
        listIds.append(dict[i]["idUser"])
    return [listUsers, listIds]


def insertUser():
    print()


def getTable(query):
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
    tupla = getIdGames()
    return tupla[0] + 1

def auxFuncGetBlankSpace(text):
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


def formatText(text, lenLine, split="\n"):
    aux = []
    auxFormatText(str(text), aux, lenLine)
    string = ""
    if len(str(text)) < lenLine:
        return text
    else:
        for i in aux:
            if aux != aux[len(aux)-1]:
                string += i + str(split)
            else:
                string += i
        return string


def getHeader(text):
    return ("*"*100 + "\n" + text.center(100,"=") + "\n" + "*"*100)



def getFormatedBodyColumns(tupla_texts, tupla_sizes, margins = 0):
    aux = []
    for i in range(len(tupla_texts)):
        aux.append([])
        auxFormatText(str(tupla_texts[i]), aux[i], tupla_sizes[i])
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
    string = ("Adventures").center(100, "=") + "\n" + "Id".ljust(10) + "Adventure".ljust(40) + "Description".ljust(50) \
             + "\n" + ("*"*100) + "\n"
    for i in adventures.keys():
        string += getFormatedBodyColumns((i, adventures[i]["Name"], adventures[i]["Description"]), (8, 38, 50), 2)
    return string


def getFormatedAnswers(idAnswer, text, lenLine, leftMargin=0):
    if len(text) < lenLine:
        return(" "*leftMargin + str(idAnswer) + ") " + text)
    else:
        text = formatText(text, lenLine).split("\n")
        string = (" "*leftMargin + str(idAnswer) + ") " + text[0])
        for i in text[1:]:
            string += "\n" + " "*(leftMargin+len(str(idAnswer) + ") ")) + i
        return string


def getHeaderForTableFromTuples(t_name_columns, t_size_columns, title=""):
    total_size = 0
    for i in t_size_columns:
        total_size += i
    string = (str(title).center(total_size,"=") + "\n")
    for i in range(len(t_size_columns)):
         string += t_name_columns[i].ljust(t_size_columns[i])
    string += ("\n" + "*"*total_size)
    return string


def getTableFromDict(tuple_of_keys, weight_of_columns, dict_of_data):
    keys = dict_of_data.keys()
    string = ""
    for i in keys:
        string += str(i).ljust(5)
        for j in range(len(tuple_of_keys)):
            string += str(dict_of_data[i][tuple_of_keys[j]]).ljust(weight_of_columns[j])
        string += "\n"
    return string


def getOpt(textOpts="",inputOptText="",rangeList=[],dictionary={},exceptions=[]):
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
    list_sizes = []
    for i in range(len(queryTable[0])):
        list_sizes.append(120//len(queryTable[0]))
    tupla_sizes = tuple(list_sizes)
    string = getHeaderForTableFromTuples(queryTable[0], tupla_sizes) + "\n"
    for i in range(1, len(queryTable)):
        string += getFormatedBodyColumns(queryTable[i], tupla_sizes) + "\n"
    return string


def checkPassword(password):
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
    if len(user) < 6:
        print("Password is too short")
        return False
    elif len(user) > 10:
        print("Password is too long")
        return False
    elif user.isalnum() == False:
        print("Password cannot contain special characters")
        return False
    else:
        return True


def UserExists(user):
    check = checkUserbbdd(user)
    if check == 0:
        return False
    else:
        return True


# Altres funcions que no apareixen al document informatiu


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
            "__/\____/\____/\____/\____/\____/\____/\____/\____/\____/\____/\____/\__" +
            "\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /" +
            "/_  _\/_  _\/_  _\/_  _\/_  _\/_  _\/_  _\/_  _\/_  _\/_  _\/_  _\/_  _\ " +
            "  \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/  " + "\n\n")


def reports_dibujo():
    return (estrellas() +
            " ____                        _" +
            "|  _ \ ___  _ __   ___  _ __| |__ __" +
            "| |_) / _ \| '_ \ / _ \| '__| __/ __|" +
            "|  _ <  __/| |_) | (_) | |  | |_\__ \ " +
            "|_| \_\___|| .__/ \___/|_|   \__|___/" +
            "           |_|" + estrellas())