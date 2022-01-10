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


def getFormatedBodyColumns(tupla_texts, tupla_sizes, margins = 0):
    aux = []
    for i in range(len(tupla_texts)):
        aux.append([])
        for j in range((len(tupla_texts[i])//tupla_sizes[i])+1):
            aux.append(auxFuncGetBlankSpace(tupla_texts[i][0*j:tupla_sizes[i]*j]))



print(getFormatedBodyColumns(("Seguro que más de uno recuerda aquellos libros en los que podías elegir cómoseguir con la aventura que estabas viviendo simplemente"), (30)))