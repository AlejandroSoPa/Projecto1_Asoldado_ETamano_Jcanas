
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
    string= str(title).center(120, "=") + "\n"
    for i in range(len(queryTable)):
        if i == 0:
            aux = []
            for j in queryTable[i]:
                text = formatText(j, 120//len(queryTable[i]) + )
    return string


queryTable = (('ID AVENTURA - NOMBRE', 'ID PASO - DESCRIPCION', 'ID RESPUESTA -DESCRIPCION', 'NUMERO VECES SELECCIONADA'), ('10 - Todos los héroes necesitan su princesa', '101 - Son las 6 de la mañana, %personaje% está profundamente dormido. Le suena la alarma!', '101 - Apaga la alarma porque quiere dormir, han sido días muy duros y %personaje% necesita un descanso.', 7), ('10 - Todos los héroes necesitan su princesa', '103 - Nuestro héroe %personaje% se viste rápidamente y va an dirección al ciber, hay mucho jaleo en la calle, también mucha policía.', '108 - Entra en el ciber a revisar si la princesa Wyoming sigue dentro.', 5))
print(getFormatedTable(queryTable))