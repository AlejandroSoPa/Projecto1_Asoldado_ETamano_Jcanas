import mysql.connector
import datetime

db = mysql.connector.connect(
    host="localhost",
    user="ErikTamaño",
    password="admin123",
    database="hr"
)


def get_answers_bystep_adventure():
    data = db.cursor()
    data.execute("SELECT idAnswers_ByStep_Adventure from ")
    # {(idAnswers_ByStep_Adventure, idByStep_Adventure): {'Description': 'descripció daquest pas','Resolution_Anwer':
    # 'Texte al camp resolution answer de la taula a la BBDD', 'NextStep_Adventure': id delseguent pas}, (2,
    # 1): {'Description': 'Escoge el camino del centro, del que parecen provenir ruidos de ramas alromperse y
    # astillarse ...', 'Resolution_Anwer': 'Piensas que para ser digno de la espada de las valkirias,
    # debesde afrontar tus miedos y peligros que acechan', 'NextStep_Adventure': 3}....}


def checkUserbbdd(user, password):
    data = db.cursor()
    data.execute("SELECT * from employees")
    listusuaris = data.fetchall()
    for i in listusuaris:
        if i[0] == user and i[1] == password:
            return 1
        elif i[0] == user and i[1] != password:
            return -1
    return 0


def InsertUser(id, user, password):
    print()


def getHeader(text):
    return (text.center(50,"="))


def auxFuncGetBlankSpace(text):
    if text[len(text)-1] != " ":
        return auxFuncGetBlankSpace(text[:len(text)-1])
    else:
        return text


def auxFormatBodyColumn(text, list, size, start = 0):
    if start + size >= len(text):
        list.append(text[start:])
        return list
    else:
        section = auxFuncGetBlankSpace(text[start:start+size])
        list.append(section[:len(section)-1])
        auxFormatBodyColumn(text, list, size, start + len(section))



def getFormatedBodyColumns(tupla_texts, tupla_sizes, margins = 0):
    aux = []
    for i in range(len(tupla_texts)):
        aux.append([])
        auxFormatBodyColumn(str(tupla_texts[i]), aux[i], tupla_sizes[i])
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

text = ("Seguro que más de uno recuerda aquellos libros en los que podías elegir cómo seguir con la aventura que estabas viviendo simplemente",
        "Seguro que más de uno recuerda aquellos libros en los que podías elegir cómo seguir con la aventura que estabas viviendo simplemente",
        "Seguro que más de uno recuerda aquellos libros en los que podías elegir cómo seguir con la aventura que estabas viviendo simplemente")
size = (20, 30, 50)
print(getFormatedBodyColumns(text, size, 2))


def getFormatedAdventures(adventures):
    string = getHeader("Adventures") + "\n" + "Id".ljust(5) + "Adventure".ljust(15) + "Description".ljust(30) + "\n" \
             + ("*"*50)
    for i in adventures.keys():
        string += getFormatedBodyColumns((i, adventures[i]["Name"], adventures[i]["Description"]), (3, 12, 30), 2)
    return string


adventures = {1: {"Name": "A", "Description":1, "Characters":[1, 3]}, 2: {"Name": 2, "Description":"a", "Characters":[1, 3]}}
print(getFormatedAdventures(adventures))

def getFormatedAnswers(idAnswer, text, lenLine, leftMargin):
    aux = []
    if len(text) < lenLine:
        aux.append(text)
    else:
        print()

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
    print(textOpts + "\n" + inputOptText)
    print(rangeList)
    print(dictionary)
    print(exceptions)
"""
textOpts="\n1)Login\n2)Create user\n3)Show Adventures\n4)Exit"
inputOptText="\nElige tu opción:"
lista = [1,2,3,4]
exceptions = ["w","e",-1]
opc = getOpt(textOpts,inputOptText,lista,exceptions)
"""

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