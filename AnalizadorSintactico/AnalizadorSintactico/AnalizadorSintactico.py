import sys

def main():
    fileName = "test.txt"

    #Open file and read the whole thing
    with open(fileName,"r") as file:
        for line in file: #for each line in the file
            for word in line.split(): #for each word in the file
                wordList.append(word) #add to a list
    
    if(programa()):
        print("El programa es valido!")
    else:
        print("Programa no valido :C")

def programa():
    print("-- Programa --")

    #Check begin
    word = wordList.pop(0)
    if(word == "begin"):
        print(word, "{") #print word

        #Check declaraciones
        declaraciones()
        #print("Word list after declaraciones", wordList)
        #print("Lista de identificadores", identificadores)
        #check ordenes
        ordenes()

        word = wordList.pop(0)
        if(word == "end"):
            print(word)
            return True
        else: 
            sys.exit('Error, el programa no contiene end')
    else:
        sys.exit('Error, el programa no contiene begin')
        return False

def declaraciones():
    #check declaracion | declaracion; nextdeclaracion
    declaracion() 
    if(wordList[0] == ";"): #check that declaration ends with ;
            print(";")
            wordList.pop(0) #remove ; from the wordlist
            next_declaraciones() #check next declaration
    else:
        sys.exit('Error: declaracion no tiene ; al final')

def next_declaraciones():
    if(tipo()):
        declaracion() 
        if(wordList[0] == ";"):
                print(";")
                wordList.pop(0)
                next_declaraciones()
        else:
            sys.exit('Error, declaracion no tiene ;')
            exit
    else:
        return

def declaracion():
    if(tipo()):
        word = wordList.pop(0)
        print(word, end = ' ') #print word
        lista_variables()
    else:
        raise SystemExit('Error: El tipo de variable no es valida')

def ordenes():
    orden()
    
    word = wordList.pop(0)
    if(word is ";"):
        next_ordenes()
    else:
        sys.exit('Error: La orden debe terminar con ;')

def next_ordenes():
    word = wordList[0]
    
    if("end" in word or "else" in word):
        return
    else:
        orden()
        word = wordList.pop(0)
        #print(wordList)
        if(word is ";"):
            next_ordenes()
        else:
            sys.exit('Error: La orden debe terminar con ;')

def orden():
    word = wordList[0]
    print(word)

    if(word.find("if") != -1):
        word = word.replace('if', '')
        wordList.pop(0)
        if(len(word) > 0):
            wordList.insert(0,word)
        condicion()

    elif(word.find("while") != -1):
        word = word.replace('while', '')
        wordList.pop(0)
        if(len(word) > 0):
            wordList.insert(0,word)
        bucle_while()
    else:
        asignar()

def tipo():
    word = wordList[0]
    if(word == "entero" or word == "real"):
        return True
    else:
        return False

def lista_variables():

    word = wordList.pop(0)

    #check word
    identificador(word)
    if(word.find(",") != -1):
        word = word.replace(',', '')
        identificadores.append(word)
    if(word.find(";") != -1):
        word = word.replace(';', '')
        identificadores.append(word)
    next_lista_variables()

def next_lista_variables():
    if(wordList[0] == ","):
        wordList.pop(0)
        print(", ", end="")
        lista_variables()
    else:
        return

def identificador(word):
    cont = 0
    letra(word[cont])
    cont = cont + 1
    resto_letras(word, cont)

def letra(letter):
    if(letter.isalnum()):
        print(letter, end= '')
        return 
    else:
        sys.exit('Error: el identificador no contiene caracteres validos')
        exit

def resto_letras(word, cont):
    if(word[cont] == ";"):
        newWord = word[cont]
        wordList.insert(0,newWord)
        return
    elif(word[cont] == ","):
        newWord = word[cont]
        wordList.insert(0,newWord)
        return
    elif(cont == len(word)-1):
        return
    else:
        letra(word[cont])
        cont = cont + 1
        resto_letras(word, cont)

def condicion():
    word = wordList.pop(0)

    if(word[0] == '('):
        #if the word is longer than ( divided it
        if(len(word) > 1):
            newWord = word.replace('(', '')
            wordList.insert(0, newWord)
        #check comparacion
        comparacion()

        word = wordList.pop(0)
        if(word == ')'):
            ordenes()
            next_condicion()
            return
        else:
            sys.exit('Error: La comparacion del if no esta entre parentesis')
    else:
        sys.exit('Error: La comparacion del if no esta entre parentesis')

def next_condicion():
    word = wordList[0]

    if("end" in word):
        word = wordList.pop(0)
        if(";" in word):
            word = word.replace(";", '')
            wordList.insert(0, ";")
        return
    else:
        if("else" in word):
            word = wordList.pop(0)
            ordenes()

            word = wordList[0]
            if("end" in word):
                word = wordList.pop(0)
                if(";" in word):
                    word = word.replace(";", '')
                    wordList.insert(0, ";")
                    return
                else:
                    sys.exit('Error: El end del if no tiene ;')
            else:
                sys.exit('Error: El if no tiene end')
        else:
            sys.exit('Error: El if no tiene end')

def bucle_while():
    word = wordList.pop(0)

    if(word[0] == '('):
        #if the word is longer than ( divided it
        if(len(word) > 1):
            newWord = word.replace('(', '')
            wordList.insert(0, newWord)
            #print(wordList)
        #check comparacion
        comparacion()

        word = wordList.pop(0)
        if(word == ')'):
            ordenes()
            #print(wordList)
            word = wordList.pop(0)
            if(";" in word):
                word = word.replace(";", '')
                wordList.insert(0, ";")
            if(word == "endwhile"):
                print("endwhile")
                return
            else:
                sys.exit('Error: Falta el endwhile')
        else:
            sys.exit('Error: La comparacion del while no esta entre parentesis')
    else:
        sys.exit('Error: La comparacion del while no esta entre parentesis')

def comparacion():
    operador()
    condicion_op()
    operador()

def operador():
    id = False
    word = wordList.pop(0)

    if(exists_identificadores(word)):
        return
    else:
        if ')' in word:
            word = word.replace(')', '')
            wordList.insert(0, ')')
            #print(wordList)
        numeros(word)

def exists_identificadores(word):
    if word in identificadores:
        return True

    else:
        for i in range(1,len(word)): #CHECK IF ITS AN IDENTIFICADOR
            if word[:i] in identificadores:        
                new = word.replace(word[:i], '')
                wordList.insert(0,new)
                #print(wordList)
                return True
    return False

def condicion_op():
    word = wordList.pop(0)
    if(word[0] == '=' or word[0] == '<=' or word[0] == '>=' or word[0] == '<>' or  word[0] == '<' or word[0] == '>'):
        if(len(word)> 1):
            new = word[1:len(word)]
            #print(new)
            wordList.insert(0,new)
            #print(wordList)
            return
        else:
            return
    else:
         sys.exit('Error: La comparacion no tiene operador condicional')

def asignar(): #FALTA EXPRESION ARITMETICA
    word = wordList.pop(0)
    index_asign = word.find(':=')
    if(index_asign != -1):
        word = word.replace(':=', '')
        wordList.insert(0,":=")
        if(len(word) > index_asign):
            newWord = word[index_asign:len(word)]
            wordList.insert(1,newWord)
            word = word[0:index_asign]
            #print(word)
        #print(wordList)

    if(word in identificadores): #Check if identificador was declared previously
        word = wordList.pop(0)
        #print(wordList)
        if(word == ":="):
            expresion_arit()
        else:
            sys.exit('Error: Se intento asignar valor si el operador correcto :=')
    else:
        sys.exit('Error: Se intento asignar valor a un identificador no declarado')

def expresion_arit():
    word = wordList.pop(0)
    if(";" in word):
        word = word.replace(";", '')
        wordList.insert(0,";")
        #print(wordList)

    if(exists_identificadores(word)): #Starts with identificador
        exp_arit()
    elif(numeros(word)):
        exp_arit()

def exp_arit():
    word = wordList[0]
    if(operador_arit(word[0])):
        wordList.pop(0)
        if(len(word)>1):
            new = word[1:]
            wordList.insert(0,new)
            #print(wordList)
        expresion_arit()
        exp_arit()
    else:
        return

def operador_arit(word):
    if(word == '+' or word == '*' or word == '-' or word == '/'):
        return True
    else:
        return False

def numeros(word):
    num = is_number(word)
    return num

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

wordList = []
identificadores = []
main()
