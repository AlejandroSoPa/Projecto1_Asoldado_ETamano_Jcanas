import datetime
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
    return (text.center(100,"="))



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

text = ("Seguro que más de uno recuerda aquellos libros en los que podías elegir cómo seguir con la aventura que estabas viviendo simplemente",
        "Seguro que más de uno recuerda aquellos libros en los que podías elegir cómo seguir con la aventura que estabas viviendo simplemente",
        "Seguro que más de uno recuerda aquellos libros en los que podías elegir cómo seguir con la aventura que estabas viviendo simplemente")
size = (20, 30, 50)
print(getFormatedBodyColumns(text, size, 2))


def getFormatedAdventures(adventures):
    string = getHeader("Adventures") + "\n" + "Id".ljust(10) + "Adventure".ljust(40) + "Description".ljust(50) + "\n" \
             + ("*"*100) + "\n"
    for i in adventures.keys():
        string += getFormatedBodyColumns((i, adventures[i]["Name"], adventures[i]["Description"]), (8, 38, 50), 2)
    return string


adventures = {1: {"Name": "A", "Description": "Seguro que más de uno recuerda aquellos libros en los que podías elegir cómo seguir con la aventura que estabas viviendo simplemente", "Characters":[1, 3]}, 2: {"Name": 2, "Description": "Seguro que más de uno recuerda aquellos libros en los que podías elegir cómo seguir con la aventura que estabas viviendo simplemente", "Characters":[1, 3]}}
print(getFormatedAdventures(adventures))

def getFormatedAnswers(idAnswer, text, lenLine, leftMargin=0):
    if len(text) < lenLine:
        return(" "*leftMargin + str(idAnswer) + ") " + text)
    else:
        text = formatText(text, lenLine).split("\n")
        string = (" "*leftMargin + str(idAnswer) + ") " + text[0])
        for i in text[1:]:
            string += "\n" + " "*(leftMargin+len(str(idAnswer) + ") ")) + i
        return string
print(getFormatedAnswers(1, "Seguro que más de uno recuerda aquellos libros en los que podías elegir cómo seguir con la aventura que estabas viviendo simplemente", 30))

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

dict = {4: {'idUser': 2, 'Username': 'Jordi', 'idAdventure': 1, 'Name': 'Este muerto esta muy vivo', 'idCharacter': 1, 'date': datetime.datetime(2021, 11, 28, 18, 17, 20), 'CharacterName':
'Beowulf'}, 5: {'idUser': 2, 'Username': 'Jordi', 'idAdventure': 1, 'Name': 'Este muerto esta muy vivo', 'idCharacter': 1, 'CharacterName': 'Beowulf', 'date': datetime.datetime(2021, 11, 26, 13, 28, 36)}}
tuple_of_keys = ("Username","Name","CharacterName", "date")
weigth_of_columns = (20, 30, 20, 20)
print(getTableFromDict(tuple_of_keys, weigth_of_columns, dict))

def getOpt(textOpts="",inputOptText="",rangeList=[],dictionary={},exceptions=[]):
    print(textOpts)
    while True:
        opt = input(inputOptText)
        if opt in rangeList or opt in dictionary or opt in exceptions:
            return opt
        else:
            print("Option is not valid")

textOpts="\n1)Login\n2)Create user\n3)Show Adventures\n4)Exit"
inputOptText="\nElige tu opción: "
lista = [1,2,3,4]
exceptions = ["w","e",-1]
opc = getOpt(textOpts,inputOptText,lista,exceptions)


def getFormatedTable(queryTable, title=""):
    list_sizes = []
    for i in range(len(queryTable[0])):
        list_sizes.append(120//len(queryTable[0]))
    tupla_sizes = tuple(list_sizes)
    string = getHeaderForTableFromTuples(queryTable[0], tupla_sizes) + "\n"
    for i in range(1, len(queryTable)):
        string += getFormatedBodyColumns(queryTable[i], tupla_sizes) + "\n"
    return string

queryTable = (('ID AVENTURA - NOMBRE', 'ID PASO - DESCRIPCION', 'ID RESPUESTA -DESCRIPCION', 'NUMERO VECES SELECCIONADA'), ('10 - Todos los h├®roesnecesitan su princesa', '101 - Son las 6 de la ma├▒ana, %personaje% est├í profundamentedormido. Le suena la alarma!', '101 - Apaga la alarma porque quiere dormir, han sido d├¡asmuy duros y %personaje% necesita un descanso.', 7), ('10 - Todos los h├®roes necesitan suprincesa', '103 - Nuestro h├®roe %personaje% se viste r├ípidamente y va an direcci├│n alciber, hay mucho jaleo en la calle, tambi├®n mucha polic├¡a.', '108 - Entra en el ciber arevisar si la princesa Wyoming sigue dentro.', 5))
print(getFormatedTable(queryTable))

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
