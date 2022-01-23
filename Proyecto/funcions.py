import pymysql # S'importa la llibreria pymysql, que ens permetrà accedir a la base de dades des de l'arxiu .py

conn = pymysql.connect(host="20.105.176.24", user="etamano", password="Etamano1!", db="PROJECT_1")
# Es connecta de forma remota a la base de dades ubicada a la màquina virtual
db = conn.cursor() # Es configura una variable per a utilitzar-la posteriorment per executar comandes al MySQL i
                   # treballar amb la base de dades


def get_answers_bystep_adventure(id_adventure):
    # Funció que, a partir de la informació de la base de dades, crea el diccionari answers_bystep_adventure, el qual
    # conté totes les respostes possibles a cada pas pertinent a l'aventura escollida
    query = "SELECT o.ID_OPTION, s.ID_STEP, o.description, o.answer, o.next_step from ADVENTURE a " \
            "inner join STEP s on s.ID_ADVENTURE = a.ID_ADVENTURE " \
            "inner join PROJECT_1.OPTION o on o.ID_STEP = s.ID_STEP " \
            "where a.ID_ADVENTURE = " + str(id_adventure)
    # Es concatena id_adventure a la query per a extreure només les respostes relacionades amb l'aventura escollida
    db.execute(query)
    data = db.fetchall()
    dict = {}
    for i in data: # Per a cada fila de la taula resultant de la query es crea una entrada del diccionari
        dict[(i[0], i[1])] = {"Description": i[2], "Resolution_answer": i[3], "Next_Step_Adventure": i[4]}
    return dict

def get_id_bystep_adventure(id_adventure):
    # Funció que, a partir de la informació de la base de dades, crea el diccionari answers_bystep_adventure, el qual
    # conté tots els passos que formen l'aventura que hagi escollit el jugador
    query = "SELECT s.ID_STEP, s.description, s.adventure_end, o.ID_OPTION from ADVENTURE a " \
            "inner join STEP s on a.ID_ADVENTURE = s.ID_ADVENTURE " \
            "inner join PROJECT_1.OPTION o on o.ID_STEP = s.ID_STEP " \
            "where a.ID_ADVENTURE = " + str(id_adventure)
    # Es concatena id_adventure a la query per a extreure només els steps relacionats amb l'aventura escollida
    db.execute(query)
    data = db.fetchall()
    dict = {}
    query = "SELECT s.ID_STEP, s.description, s.adventure_end from ADVENTURE a " \
            "inner join STEP s on a.ID_ADVENTURE = s.ID_ADVENTURE " \
            "where s.adventure_end = 1 and a.ID_ADVENTURE = " + str(id_adventure)
    # Com que els passos finals de les aventures no tenen cap opció relacionada a ells, l'anterior query no els extreu.
    # Per tant, s'ha de fer una query adicional on només s'extreuen els passos de final d'aventura
    db.execute(query)
    data_end = db.fetchall()
    for i in data:
        # Com que la taula resultant de la primera query ens dona vàries línies amb el mateix pas (un per a cada opció
        # enllaçada al pas) es fa un condicional que comprobi que el pas que es vol guardar al diccionari no existeixi
        # encara i dins d'aquest condicional es fa un iteratiu per tal de guardar la tupla amb les opcions relacionades
        # amb el pas
        if i[0] not in dict.keys():
            dict[i[0]] = {"Description": i[1], "Final_Step": 0}
            aux = []
            for j in data:
                if j[0] == i[0]:
                    aux.append(j[3])
            dict[i[0]]["answers_in_step"] = tuple(aux)
    for i in data_end:
        # Els pasos finals es guarden amb una tupla buida a answers_in_step perquè no té cap resposta connectada
        dict[i[0]] = {"Description": i[1], "Final_Step": 1, "answers_in_step": ()}
    return dict


def get_first_step_adventure(id_adventure):
    # Funció que busca el pas inicial de l'aventura que s'estigui jugant
    query = "SELECT min(ID_STEP) from STEP where ID_ADVENTURE = " + str(id_adventure)
    # Es busca el ID_STEP més petit dins de totes les steps relacionades amb l'aventura actual perquè el primer pas
    # sempre tindrà la ID més petita entre els passos d'una mateixa aventura
    db.execute(query)
    data = db.fetchall()
    return data[0][0] # Com que la query ens dona una tupla de tuples amb un sol valor, la funció retorna el valora
                      # en posició [0][0], que seria l'únic valor possible


def get_Adventures_with_Characters():
    # Funció que extreu totes les aventures amb les seves descripicons i els personatges que es puguin utilitzar en cada
    # aventura
    query = "SELECT a.ID_ADVENTURE, a.name, a.description, c.ID_CHARACTER from ADVENTURE a inner join " \
            "CHARACTER_ADVENTURE c on a.ID_ADVENTURE = c.ID_ADVENTURE ORDER BY a.ID_ADVENTURE asc"
    db.execute(query)
    data = db.fetchall()
    dict = {}
    for i in data:
        # Com que la taula resultant de la query ens dona vàries línies amb la mateixa aventura (una per a cada
        # personatge que es pot utilitzar en l'aventura) es fa un condicional que comprobi que l'aventura que es vol
        # guardar al diccionari no existeixi encara i dins d'aquest condicional es fa un iteratiu per tal de guardar
        # la llista amb els personatge jugables
        if i[0] not in dict.keys():
            dict[i[0]] = {"Name": i[1], "Description": i[2]}
            aux=[]
            for j in data:
                if j[0] == i[0]:
                    aux.append(j[3])
            dict[i[0]]["Characters"] = aux
    return dict


def getCharacters():
    # Funció que extreu tots els personatges registrats a la base de dades i els inserta en un diccionari
    query = "SELECT ID_CHARACTER, name from PROJECT_1.CHARACTER"
    db.execute(query)
    data = db.fetchall()
    dictCharacters = {}
    for i in range(len(data)):
        dictCharacters[data[i][0]] = data[i][1]
    return dictCharacters


def getReplayAdventures():
    # Funció que obté totes les partides que s'han jugat anteriorment i inserta les dades d'aquestes partides a un
    # diccionari
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
    query = "SELECT s.ID_STEP, o.ID_OPTION from ROUND r inner join ROUND_OPTION e on r.ID_ROUND = e.ID_ROUND inner " \
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
    # La query extreu totes les ID_ROUND en ordre descendent perque després, en la funció que utilitza aquesta per
    # crear una nova ID_ROUND, s'utilitzarà el valor màxim registrat, que en aquest cas serà sempre el que es troba en
    # posició 0
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

    # Les IDs s'inserten de forma automàtica, però si es dona el cas en el que no es completa la inserció d'una partida,
    # el valor de la ID_ROUND canvia (per exemple, si es vol insertar la tercera partida però el joc es tanca abans
    # d'acabar la partida, es cancel·la aquesta inserció, però la següent partida, encara que seria també la tercera
    # partida en la base de dades, tindrà la ID_ROUND 4).
    # Per tant, s'ha d'alterar la configuració de la taula per tal de que s'inserti la ID correcta
    query = "select count(ID_ROUND) + 1 from ROUND"
    db.execute(query)
    data = db.fetchall()
    auto_inc = data[0][0]
    # Aquesta query altera l'auto_increment de la taula, és a dir, configura la taula per a que la següent ID tingi un
    # valor de (quantitat d'IDs insertades) + 1
    query = "ALTER TABLE ROUND auto_increment = " + str(auto_inc)
    db.execute(query)
    query = "INSERT INTO ROUND (ID_USER, ID_CHARACTER, ID_ADVENTURE, date, time, usercreate, datecreated) " \
            "VALUES (" + str(idUser) + ", " + str(idChar) + ", " + str(idAdventure) + \
            ", current_date(), current_time(), current_user(), current_timestamp())"
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
    # Com que els noms d'usuari són les claus del diccionari Users i les IDs es troben dins dels valors d'aquestes
    # claus, es crea la llista de usernames i després es recorre aquesta llista per extreure del diccionari les IDs i
    # insertar-les a una llista
    listUsers = list(dict.keys())
    listIds = []
    for i in dict:
        listIds.append(dict[i]["idUser"])
    return [listUsers, listIds]


def insertUser(user, password):
    # Funció que inserta a la base de dades l'usuari creat amb l'opció de Create User
    # A l'igual que amb la funció insertCurrentGame(), en cas de que no es completi la inserció a causa d'algun error o
    # alguna altra raó, les IDs no s'inserten correctament. Per tant, s'altera la taula per tornar a configurar
    # l'increment automàtic de les IDs
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
    colname = db.description # Extreu les dades de les columnes de la taula en una tupla de tuples, sent el valor en
                             # posició 0 de cada tupla el nom de cada columna
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
    # Com que els returns dins dels condicionals tallen l'execució de la funció, aquest últim return no s'executarà fins
    # a haver recorregut totes les dades extretes de la query, és a dir, si es dona el cas de que no existeix l'usuari
    # donat, independentment de si la contrasenya és correcta o no
    return 0



# Funcions Auxiliars


def setIdGame():
    # Funció que retorna la ID d'una partida nova per a poder insertar-la a la base de dades
    tupla = getIdGames()
    # Utilitza la funció getIdGames() per rebre totes les IDs de partida registrades.
    # En cas de que no hi hagi partides, getIdGames retorna una tupla buida. Per tant, aquesta funció ha de retornar 1
    if len(tupla) == 0:
        return 1
    # En cas de que sí n'hi hagi partides, agafa el valor de la tupla en posició 0 (el nombre d'ID màxim) i retorna
    # aquest valor + 1
    else:
        return tupla[0] + 1


def InsertCurrentChoice(idGame, answer):
    # Funció que inserta a la base de dades la opció que ha escollit el jugador en una determinada partida
    query = "INSERT INTO ROUND_OPTION (ID_ROUND, ID_OPTION, usercreate, datecreated) VALUES (" + str(idGame) + ", " \
            + str(answer) + ", current_user(), current_timestamp())"
    db.execute(query)


def formatText(text, lenLine, split="\n"):
    # Funció que modifica una cadena de texte per a que tingui com a màxim una longitud de línia determinada
    # Es separa el text per si n'hi han salts de línia des d'abans de formatar el texte
    text = text.split("\n")
    string = ""
    for i in text:
        # Utilitza una funció auxiliar per separar cada porció del text en línies i després les concatena amb el valor
        # insertat a split
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
    # Funció que crea una capçalera a partir del text a insertar dins d'aquesta
    return ("*"*100 + "\n" + text.center(100,"=") + "\n" + "*"*100)



def getFormatedBodyColumns(tupla_texts, tupla_sizes, margins = 0):
    # Funció que, utilitzant FormatText, modifica un nombre de paràgrafs per a que es puguin mostrar amb un format de
    # columnes
    aux = []
    for i in range(len(tupla_texts)):
        # Es formata cada paràgraf per separat amb la funció formatText però, en comptes de retornar una sola string,
        # s'utilitza un split per separar cada fila del texte, insertar-la en una llista, i finalment insertar aquesta
        # llista en la llista aux
        aux.append(formatText(str(tupla_texts[i]), tupla_sizes[i]).split("\n"))
    maxfiles = 0
    # Es comparen les llistes dins d'aux per buscar quin paràgraf té més línies i, per tant, saber quantes línies s'han
    # d'imprimir
    for i in range(len(aux)):
        if len(aux[i]) > len(aux[maxfiles]):
            maxfiles = i
    string = ""
    # Es concatenen els marges i les files de cada paràgraf en ordre (primer es recorre cada llista i s'agafa la cadena
    # de text que hi hagi en la posició 0, després es repeteix per a la posició 1, i successivament)
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

    # Primerament es crea la capçalera de la taula i després es recorre el diccionari Adventures per formatar les dades
    # mitjançat la funció getFormatedBodyColumns()
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
        # Es formata la descripció amb la funció formatText però, en comptes de retornar una sola string,
        # s'utilitza un split per separar cada fila del texte i insertar-les en una llista
        text = formatText(text, lenLine).split("\n")
        # Es crea la variable string amb el format "ID) primera fila de la descripció" i després es concatenen les
        # següents files (si hi ha) amb els seus respectius salts de línia
        string = (" "*leftMargin + str(idAnswer) + ") " + text[0])
        if len(text) > 1:
            for i in text[1:]:
                string += "\n" + " "*(leftMargin+len(str(idAnswer) + ") ")) + i
        return string


def getHeaderForTableFromTuples(t_name_columns, t_size_columns, title=""):
    # Funció que obté la capçalera d'una taula, amb un títol (si té) i els noms de les columnes
    total_size = 0
    # Es calcul·la la amplada total de la taula sumant els valors de la tupla t_size_columns
    for i in t_size_columns:
        total_size += i
    string = (str(title).center(total_size,"=") + "\n")
    for i in range(len(t_size_columns)):
         string += t_name_columns[i].ljust(t_size_columns[i])
    string += ("\n" + "*"*total_size)
    return string


def getTableFromDict(tuple_of_keys, weight_of_columns, dict_of_data):
    # Funció que obté les dades d'un diccionari i les retorna amb un format per poder mostrar-les en una taula

    # S'extreuen totes les
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
        # Si l'input està dins de les opcions possibles o les excepcions, retorna el valor insertat. Si no, dona un
        # missatge per notificar de que la opció no és vàlida
        if opt in rangeList or opt in dictionary or opt in exceptions:
            return opt
        else:
            print("Option is not valid")



def getFormatedTable(queryTable, title=""):
    # Funció que utilitza una tupla de tuples obtinguda amb la funció getTable() o similar i crea una taula que es pugui
    # mostrar per pantalla
    list_sizes = []
    # Es crea la tupla de mides dividint 120 (l'amplada de pantalla en els reports) entre el nombre de columnes
    for i in range(len(queryTable[0])):
        list_sizes.append((120//len(queryTable[0])))
    tupla_sizes = tuple(list_sizes)
    # Es crea la capçalera per a la taula
    string = getHeaderForTableFromTuples(queryTable[0], tupla_sizes, title) + "\n"
    # Es formaten i s'inserten a la taula les dades obtingudes
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
            # Comprova si hi ha espais en blanc en la contrasenya
            if i == " ":
                blank = True
                break
            # Comprova si hi ha minúscules en la contrasenya
            elif i.islower():
                lcase = True
            # Comprova si hi ha majúscules en la contrasenya
            elif i.isupper():
                ucase = True
            # Comprova si hi ha digits en la contrasenya
            elif i.isdigit():
                num = True
            # Comprova si hi ha caràcters especials en la contrasenya
            elif i.isalnum() == False:
                special = True
        # Condicionals per comprovar que la contrasenya és correcta i per a cada cas en el que no ho és
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
        # Recorre els caràcters del username un per un i comprova que no hi hagi cap accent ni ñ ni ç
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
    # Funció que comprova si un usuari creat ja existeix a la base de dades utilitzant la funció checkUserbbdd amb
    # l'usuari en questió i una contrasenya buida, ja que si l'usuari no existeix, independentment de quina sigui la
    # contrasenya, la funció retornarà 0
    check = checkUserbbdd(user, "")
    if check == 0:
        return False
    else:
        return True


def replay(choices, id_replay):
    # Funció que, a partir de la tupla choices, repeteix una partida jugada anteriorment

    # query que extreu el nom de l'aventura
    query = "SELECT a.name from ADVENTURE a " \
            "inner join STEP s on s.ID_ADVENTURE = a.ID_ADVENTURE " \
            "where s.ID_STEP = " + str(choices[0][0])
    db.execute(query)
    data = db.fetchall()
    title = data[0][0]

    # query que extreu el nom del personatge utilitzat
    query = "SELECT c.name from PROJECT_1.CHARACTER c " \
            "inner join ROUND r on c.ID_CHARACTER = r.ID_CHARACTER " \
            "where r.ID_ROUND = " + str(id_replay)
    db.execute(query)
    data = db.fetchall()
    char = data[0][0]

    # Recorre la tupla choices i se simula una partida en la que s'escull una opció determinada
    for i in choices:
        # query que extreu la descripció del pas actual
        query = "SELECT description from STEP where ID_STEP = " + str(i[0])
        db.execute(query)
        data = db.fetchall()
        text = data[0][0]
        # Es mostra per pantalla la capçalera amb el títol de l'aventura i la descripció del pas, substituint els
        # "placeholders" per al nom de personatge amb el nom del personatge seleccionat
        print("\n\n" + getHeader(title) + "\n" + formatText(text, 100).replace("%personaje%", char) + "\n")
        # query que extreu les possibles opcions per al pas actual
        query = "SELECT ID_OPTION, description from PROJECT_1.OPTION where ID_STEP = " + str(i[0])
        db.execute(query)
        data = db.fetchall()
        # Es mostren per pantalla les opcions formatades
        for j in data:
            print(getFormatedAnswers(j[0], j[1], 95, 5))
        print("\n")
        wait()
        # Es mostra quina opció s'ha escollit i la resolució d'aquesta
        print("\n" + "Option " + str(i[1]) + " selected.")
        query = "SELECT answer from PROJECT_1.OPTION where ID_OPTION = " + str(i[1])
        db.execute(query)
        data = db.fetchall()
        answer = data[0][0]
        print("\n" + formatText(answer, 100))
        wait()
        # Si la resposta actual es troba al final de la tupla, es mostra per pantalla el pas al que porta ja que els
        # passos finals no es guarden a la tupla choices perquè no tenen cap opció per escollir
        if i == choices[len(choices)-1]:
            query = "SELECT s.description from STEP s inner join PROJECT_1.OPTION o on s.ID_STEP = o.next_step " \
                    "where o.ID_OPTION = " + str(i[1])
            db.execute(query)
            data = db.fetchall()
            print("\n" + formatText(data[0][0], 100) + "\n" + fin())
            wait()


# Altres funcions que no apareixen al document informatiu


def auxFuncGetBlankSpace(text):
    # Funció auxiliar recursiva que busca l'espai en blanc més proper al final d'una string

    # Es va tallant la string pel final fins a que troba un espai en blanc
    if text[len(text)-1] != " ":
        return auxFuncGetBlankSpace(text[:len(text)-1])
    else:
        return text


def auxFormatText(text, list, size, start = 0):
    # Funció auxiliar recursiva que separa una string en files i les inserta en una llista

    # Si s'arriba a l'última fila del text, s'afegeix aquesta a la llista i es retorna la llista
    if start + size >= len(text):
        list.append(text[start:])
        return list
    # Si no, s'utilitza auxFuncGetBlankSpace() per evitar tallar cap paraula, s'afegeix la fila resultant a la llista
    # i la funció es crida a si mateixa pero començant la línia per on ha acabat l'anterior
    else:
        section = auxFuncGetBlankSpace(text[start:start+size])
        list.append(section[:len(section)-1])
        auxFormatText(text, list, size, start + len(section))


def title_screen():
    # Funció que retorna el dibuix de la pantalla de títol
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
    # Funció auxiliar que retorna una fila d'estrelles per a altres funcions de dibuixos
    return ("\n\n" +
            " __/\____/\____/\____/\____/\____/\____/\____/\____/\____/\____/\____/\__ ".center(100) + "\n" +
            " \    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    / ".center(100) + "\n" +
            " /_  _\/_  _\/_  _\/_  _\/_  _\/_  _\/_  _\/_  _\/_  _\/_  _\/_  _\/_  _\ ".center(100) + "\n" +
            "   \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/   ".center(100) + "\n\n")


def reports_dibujo():
    # Funció que retorna un dibuix per a la pantalla de reports
    return (estrellas() +
            " ____                        _        ".center(100) + "\n" +
            "|  _ \ ___  _ __   ___  _ __| |__ __  ".center(100) + "\n" +
            "| |_) / _ \| '_ \ / _ \| '__| __/ __| ".center(100) + "\n" +
            "|  _ <  __/| |_) | (_) | |  | |_\__ \ ".center(100) + "\n" +
            "|_| \_\___|| .__/ \___/|_|   \__|___/ ".center(100) + "\n" +
            "           |_|                        ".center(100) + "\n" +
            estrellas())


def replay_screen():
    # Funció que retorna un dibuix per a la pantalla de replay
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
    # Funció que retorna un dibuix per indicar que la aventura a finalitzat
    return ("                                _____ ___ _   _                                 ".center(100) + "\n" +
            "__/\____/\____/\____/\____/\__ |  ___|_ _| \ | | __/\____/\____/\____/\____/\__ ".center(100) + "\n" +
            "\    /\    /\    /\    /\    / | |_   | ||  \| | \    /\    /\    /\    /\    / ".center(100) + "\n" +
            "/_  _\/_  _\/_  _\/_  _\/_  _\ |  _|  | || |\  | /_  _\/_  _\/_  _\/_  _\/_  _\ ".center(100) + "\n" +
            "  \/    \/    \/    \/    \/   |_|   |___|_| \_|   \/    \/    \/    \/    \/   ".center(100))


def commit():
    # Funció per a executar un commit a la bbdd després de cada partida i d'aquesta manera enregistrar les partides i
    # les opcions escollides en cadascuna sense que hi hagi possibles problemes per tancar el joc abans de finalitzar
    # la partida
    db.execute("commit")


def wait():
    # Funció per a pausar l'execució fins que l'usuari premi intro
    wait = input("\nPress ENTER to continue: ")
