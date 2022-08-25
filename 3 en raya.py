import random

#1, 3 y 6 sustituidos por X/O
fila_1 = [' 1 | ', ' ', ' | ', ' ', ' |', '', ' ', ' |']
fila_2 = [' 2 | ', ' ', ' | ', ' ', ' |', '', ' ', ' |']
fila_3 = [' 3 | ', ' ', ' | ', ' ', ' |', '', ' ', ' |']


def tablero():
    print ('      A     B     C   ')
    print ('   |     |     |     |')
    print (fila_1 [0], fila_1[1], fila_1[2], fila_1[3], fila_1[4], fila_1[5], fila_1[6], fila_1[7])
    print ('   |-----|-----|-----|')
    print ('   |     |     |     |')
    print (fila_2 [0], fila_2[1], fila_2[2], fila_2[3], fila_2[4], fila_2[5], fila_2[6], fila_2[7])
    print ('   |-----|-----|-----|')
    print (fila_3 [0], fila_3[1], fila_3[2], fila_3[3], fila_3[4], fila_3[5], fila_3[6], fila_1[7])
    print ('   |     |     |     |')

def victoria():
    #Comprueba condiciones de victoria
    #Horizontales de X
    if fila_1[1] == 'X' and fila_1[3] == 'X' and fila_1[6] == 'X':
        print ('Gana X, ¡Bien jugado!')
        return True
    if fila_2[1] == 'X' and fila_2[3] == 'X' and fila_2[6] == 'X':
        print ('Gana X, ¡Bien jugado!')
        return True
    if fila_3[1] == 'X' and fila_3[3] == 'X' and fila_3[6] == 'X':
        print ('Gana X, ¡Bien jugado!')
        return True
    #Horizontales de O
    if fila_1[1] == 'O' and fila_1[3] == 'O' and fila_1[6] == 'O':
        print ('Gana O, ¡Bien jugado!')
        return True
    if fila_2[1] == 'O' and fila_2[3] == 'O' and fila_2[6] == 'O':
        print ('Gana O, ¡Bien jugado!')
        return True
    if fila_3[1] == 'O' and fila_3[3] == 'O' and fila_3[6] == 'O':
        print ('Gana O, ¡Bien jugado!')
        return True
    #Verticales de X
    if fila_1[1] == 'X' and fila_2[1] == 'X' and fila_3[1] == 'X':
        print ('Gana X, ¡Bien jugado!')
        return True
    if fila_1[3] == 'X' and fila_2[3] == 'X' and fila_3[3] == 'X':
        print ('Gana X, ¡Bien jugado!')
        return True
    if fila_1[6] == 'X' and fila_2[6] == 'X' and fila_3[6] == 'X':
        print ('Gana X, ¡Bien jugado!')
        return True
    #Verticales de O
    if fila_1[1] == 'O' and fila_2[1] == 'O' and fila_3[1] == 'O':
        print ('Gana O, ¡Bien jugado!')
        return True
    if fila_1[3] == 'O' and fila_2[3] == 'O' and fila_3[3] == 'O':
        print ('Gana O, ¡Bien jugado!')
        return True
    if fila_1[6] == 'O' and fila_2[6] == 'O' and fila_3[6] == 'O':
        print ('Gana O, ¡Bien jugado!')
        return True
    #Diagonales de X
    if fila_1[1] == 'X' and fila_2[3] == 'X' and fila_3[6] == 'X':
        print ('Gana X, ¡Bien jugado!')
        return True
    if fila_1[6] == 'X' and fila_2[3] == 'X' and fila_3[1] == 'X':
        print ('Gana X, ¡Bien jugado!')
        return True
    #Diagonales de O
    if fila_1[1] == 'O' and fila_2[3] == 'O' and fila_3[6] == 'O':
        print ('Gana O, ¡Bien jugado!')
        return True
    if fila_1[6] == 'O' and fila_2[3] == 'O' and fila_3[1] == 'O':
        print ('Gana O, ¡Bien jugado!')
        return True

    
def jueg_2():
    tablero()
    respuestas = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']  #Sirve para comprobar que las casillas existen
    turno = 0
    jugador = 'X'
    print (f'Empieza {jugador}.')
    while turno < 9:                                             #Va cambiando entre X y O
        if victoria() == True:
            break
        if turno % 2 == 0 or turno == 0:
            jugador = 'X'
        else:
            jugador = 'O'
        
        mov = input('Casilla: ')
        if mov[:2] not in respuestas or len(mov) >= 3:
            print ('Has debido escribir la respuesta mal, por favor, usa LetraNúmero, sin espacios, y, con la letra en mayúscula.')
            print ('Ejemplo: A1')
#Fila 1           
        elif mov[:2] == 'A1':
            if fila_1[1] == ' ':                         #Comprueba que la casilla esté vacía
                fila_1[1] = jugador
                turno += 1
                tablero()
            else:
                print ('Esa casilla ya ha sido seleccionada.')
        elif mov[:2] == 'B1':
            if fila_1[3] == ' ':
                fila_1[3] = jugador
                turno += 1
                tablero()
            else:
                print ('Esa casilla ya ha sido seleccionada.')
        elif mov[:2] == 'C1':
            if fila_1[6] == ' ':
                fila_1[6] = jugador
                turno += 1
                tablero()
            else:
                print ('Esa casilla ya ha sido seleccionada.')

#Fila 2
        elif mov[:2] == 'A2':
            if fila_2[1] == ' ':
                fila_2[1] = jugador
                turno += 1
                tablero()
            else:
                print ('Esa casilla ya ha sido seleccionada.')
        elif mov[:2] == 'B2':
            if fila_2[3] == ' ':
                fila_2[3] = jugador
                turno += 1
                tablero()
            else:
                print ('Esa casilla ya ha sido seleccionada.')
        elif mov[:2] == 'C2':
            if fila_2[6] == ' ':
                fila_2[6] = jugador
                turno += 1
                tablero()
            else:
                print ('Esa casilla ya ha sido seleccionada.')
            
#Fila 3
        elif mov[:2] == 'A3':
            if fila_3[1] == ' ':
                fila_3[1] = jugador
                turno += 1
                tablero()
            else:
                print ('Esa casilla ya ha sido seleccionada.')
        elif mov[:2] == 'B3':
            if fila_3[3] == ' ':
                fila_3[3] = jugador
                turno += 1
                tablero()
            else:
                print ('Esa casilla ya ha sido seleccionada.')
        elif mov[:2] == 'C3':
            if fila_3[6] == ' ':
                fila_3[6] = jugador
                turno += 1
                tablero()
            else:
                print ('Esa casilla ya ha sido seleccionada.')
    if turno == 9 and victoria() == False:
        print ('Empate, ¡Bien jugado!')


def jueg_1():
    tablero()
    respuestas = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']  #Sirve para comprobar que las casillas existen
    turno = 0
    jugador = 'X'
    print (f'Empieza {jugador}.')
    while turno < 9:                                             #Va cambiando entre X y O
        if victoria() == True:
            break
        if turno % 2 == 0 or turno == 0:
            jugador = 'X'
        else:
            jugador = 'O'

        while jugador == 'O':
#Fila 1
            maquina = random.randint(1,9)
            if maquina == 1 and fila_1[1] == ' ':
                fila_1[1] = jugador
                turno += 1
                tablero()
                jugador = 'X'
                if victoria() == True:
                     break
            if maquina == 2 and fila_1[3] == ' ':
                fila_1[3] = jugador
                turno += 1
                tablero()
                jugador = 'X'
                if victoria() == True:
                     break
            if maquina == 3 and fila_1[6] == ' ':
                fila_1[6] = jugador
                turno += 1
                tablero()
                jugador = 'X'
                if victoria() == True:
                     break
#Fila 2
            if maquina == 4 and fila_2[1] == ' ':
                fila_2[1] = jugador
                turno += 1
                tablero()
                jugador = 'X'
                if victoria() == True:
                     break
            if maquina == 5 and fila_2[3] == ' ':
                fila_2[3] = jugador
                turno += 1
                tablero()
                jugador = 'X'
                if victoria() == True:
                     break
            if maquina == 6 and fila_2[6] == ' ':
                fila_2[6] = jugador
                turno += 1
                tablero()
                jugador = 'X'
                if victoria() == True:
                     break
#Fila 3
            if maquina == 7 and fila_3[1] == ' ':
                fila_3[1] = jugador
                turno += 1
                tablero()
                jugador = 'X'
                if victoria() == True:
                     break
            if maquina == 8 and fila_3[3] == ' ':
                fila_3[3] = jugador
                turno += 1
                tablero()
                jugador = 'X'
                if victoria() == True:
                     break
            if maquina == 9 and fila_3[6] == ' ':
                fila_3[6] = jugador
                turno += 1
                tablero()
                jugador = 'X'
                if victoria() == True:
                     break            
        
        mov = input('Casilla: ')
        if mov[:2] not in respuestas or len(mov) >= 3:
            print ('Has debido escribir la respuesta mal, por favor, usa LetraNúmero, sin espacios, y, con la letra en mayúscula.')
            print ('Ejemplo: A1')

#Fila 1           
        elif mov[:2] == 'A1':
            if fila_1[1] == ' ':                         #Comprueba que la casilla esté vacía
                fila_1[1] = jugador
                turno += 1
                tablero()
            else:
                print ('Esa casilla ya ha sido seleccionada.')
        elif mov[:2] == 'B1':
            if fila_1[3] == ' ':
                fila_1[3] = jugador
                turno += 1
                tablero()
            else:
                print ('Esa casilla ya ha sido seleccionada.')
        elif mov[:2] == 'C1':
            if fila_1[6] == ' ':
                fila_1[6] = jugador
                turno += 1
                tablero()
            else:
                print ('Esa casilla ya ha sido seleccionada.')

#Fila 2
        elif mov[:2] == 'A2':
            if fila_2[1] == ' ':
                fila_2[1] = jugador
                turno += 1
                tablero()
            else:
                print ('Esa casilla ya ha sido seleccionada.')
        elif mov[:2] == 'B2':
            if fila_2[3] == ' ':
                fila_2[3] = jugador
                turno += 1
                tablero()
            else:
                print ('Esa casilla ya ha sido seleccionada.')
        elif mov[:2] == 'C2':
            if fila_2[6] == ' ':
                fila_2[6] = jugador
                turno += 1
                tablero()
            else:
                print ('Esa casilla ya ha sido seleccionada.')   
                  
#Fila 3
        elif mov[:2] == 'A3':
            if fila_3[1] == ' ':
                fila_3[1] = jugador
                turno += 1
                tablero()
            else:
                print ('Esa casilla ya ha sido seleccionada.')
        elif mov[:2] == 'B3':
            if fila_3[3] == ' ':
                fila_3[3] = jugador
                turno += 1
                tablero()
            else:
                print ('Esa casilla ya ha sido seleccionada.')
        elif mov[:2] == 'C3':
            if fila_3[6] == ' ':
                fila_3[6] = jugador
                turno += 1
                tablero()
            else:
                print ('Esa casilla ya ha sido seleccionada.')
    if turno == 9 and victoria() == False:
        print ('Empate, ¡Bien jugado!')


def comprobar_victoria():
    #Importante saber que retorna False cuando quien tiene probabilidades de ganar es el rival, es decir, el humano, y True, cuando es la máquina
#Horizontales de X
    #Fila 1
    if fila_1[1] == ' ' and fila_1[3] == 'X' and fila_1[6] == 'X':
        return 1, False
    elif fila_1[1] == 'X' and fila_1[3] == ' ' and fila_1[6] == 'X':
        return 2, False
    elif fila_1[1] == 'X' and fila_1[3] == 'X' and fila_1[6] == ' ':
        return 3, False
    #Fila 2
    elif fila_2[1] == ' ' and fila_2[3] == 'X' and fila_2[6] == 'X':
        return 4, False
    elif fila_2[1] == 'X' and fila_2[3] == ' ' and fila_2[6] == 'X':
        return 5, False
    elif fila_2[1] == 'X' and fila_2[3] == 'X' and fila_2[6] == ' ':
        return 6, False
    #Fila 3
    elif fila_3[1] == ' ' and fila_3[3] == 'X' and fila_3[6] == 'X':
        return 7, False
    elif fila_3[1] == 'X' and fila_3[3] == ' ' and fila_3[6] == 'X':
        return 8, False
    elif fila_3[1] == 'X' and fila_3[3] == 'X' and fila_3[6] == ' ':
        return 9, False
#Horizontales de O
    #Fila 1
    elif fila_1[1] == ' ' and fila_1[3] == 'O' and fila_1[6] == 'O':
        return 1, True
    elif fila_1[1] == 'O' and fila_1[3] == ' ' and fila_1[6] == 'O':
        return 2, True
    elif fila_1[1] == 'O' and fila_1[3] == 'O' and fila_1[6] == ' ':
        return 3, True
    #Fila 2
    elif fila_2[1] == ' ' and fila_2[3] == 'O' and fila_2[6] == 'O':
        return 4, True
    elif fila_2[1] == 'O' and fila_2[3] == ' ' and fila_2[6] == 'O':
        return 5, True
    elif fila_2[1] == 'O' and fila_2[3] == 'O' and fila_2[6] == ' ':
        return 6, True
    #Fila 3
    elif fila_3[1] == ' ' and fila_3[3] == 'O' and fila_3[6] == 'O':
        return 7, True
    elif fila_3[1] == 'O' and fila_3[3] == ' ' and fila_3[6] == 'O':
        return 8, True
    elif fila_3[1] == 'O' and fila_3[3] == 'O' and fila_3[6] == ' ':
        return 9, True
#Verticales de X
    #Columna 1
    elif fila_1[1] == ' ' and fila_2[1] == 'X' and fila_3[1] == 'X':
        return 1, False
    elif fila_1[1] == 'X' and fila_2[1] == ' ' and fila_3[1] == 'X':
        return 4, False
    elif fila_1[1] == 'X' and fila_2[1] == 'X' and fila_3[1] == ' ':
        return 7, False

    #Columna 2
    elif fila_1[3] == ' ' and fila_2[3] == 'X' and fila_3[3] == 'X':
        return 2, False
    elif fila_1[3] == 'X' and fila_2[3] == ' ' and fila_3[3] == 'X':
        return 5, False
    elif fila_1[3] == 'X' and fila_2[3] == 'X' and fila_3[3] == ' ':
        return 8, False
    #Columna 3
    elif fila_1[6] == ' ' and fila_2[6] == 'X' and fila_3[6] == 'X':
        return 3, False
    elif fila_1[6] == 'X' and fila_2[6] == ' ' and fila_3[6] == 'X':
        return 6, False
    elif fila_1[6] == 'X' and fila_2[6] == 'X' and fila_3[6] == ' ':
        return 9, False
#Verticales de O
    elif fila_1[1] == ' ' and fila_2[1] == 'O' and fila_3[1] == 'O':
        return 1, True
    elif fila_1[1] == 'O' and fila_2[1] == ' ' and fila_3[1] == 'O':
        return 4, True
    elif fila_1[1] == 'O' and fila_2[1] == 'O' and fila_3[1] == ' ':
        return 7, True
 
    #Columna 2
    elif fila_1[3] == ' ' and fila_2[3] == 'O' and fila_3[3] == 'O':
        return 2, True
    elif fila_1[3] == 'O' and fila_2[3] == ' ' and fila_3[3] == 'O':
        return 5, True
    elif fila_1[3] == 'O' and fila_2[3] == 'O' and fila_3[3] == ' ':
        return 8, True
    #Columna 3
    elif fila_1[6] == ' ' and fila_2[6] == 'O' and fila_3[6] == 'O':
        return 3, True
    elif fila_1[6] == 'O' and fila_2[6] == ' ' and fila_3[6] == 'O':
        return 6, True
    elif fila_1[6] == 'O' and fila_2[6] == 'O' and fila_3[6] == ' ':
        return 9, True
        return None

#Diagonales de X
    #Diagonal 1
    elif fila_1[1] == ' ' and fila_2[3] == 'X' and fila_3[6] == 'X':
        return 1, False
    elif fila_1[1] == 'X' and fila_2[3] == ' ' and fila_3[6] == 'X':
        return 5, False
    elif fila_1[1] == 'X' and fila_2[3] == 'X' and fila_3[6] == ' ':
        return 9, False
    #Diagonal 2
    elif fila_1[6] == ' ' and fila_2[3] == 'X' and fila_3[1] == 'X':
        return 7, False
    elif fila_1[6] == 'X' and fila_2[3] == ' ' and fila_3[1] == 'X':
        return 5, False
    elif fila_1[6] == 'X' and fila_2[3] == 'X' and fila_3[1] == ' ':
        return 3, False

#Diagonales de O
    elif fila_1[1] == ' ' and fila_2[3] == 'O' and fila_3[6] == 'O':
        return 1, True
    elif fila_1[1] == 'O' and fila_2[3] == ' ' and fila_3[6] == 'O':
        return 5, True
    elif fila_1[1] == 'O' and fila_2[3] == 'O' and fila_3[6] == ' ':
        return 9, True
    #Diagonal 2
    elif fila_1[6] == ' ' and fila_2[3] == 'O' and fila_3[1] == 'O':
        return 7, True
    elif fila_1[6] == 'O' and fila_2[3] == ' ' and fila_3[1] == 'O':
        return 5, True
    elif fila_1[6] == 'O' and fila_2[3] == 'O' and fila_3[1] == ' ':
        return 3, True  
    else:
        return None

def jueg_1_facil():
    tablero()
    respuestas = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']  #Sirve para comprobar que las casillas existen
    turno = 0
    jugador = 'X'
    print (f'Empieza {jugador}.')
    while turno < 9:                                             #Va cambiando entre X y O
        if victoria() == True:
            break
        if turno % 2 == 0 or turno == 0:
            jugador = 'X'
        else:
            jugador = 'O'

        while jugador == 'O':
            j = 0
            while j == 0:
                compr = comprobar_victoria()
                if compr == None:
                    j += 1
                elif compr[0] == 1 and fila_1[1] == ' ':
                    fila_1[1] = jugador
                    turno += 1
                    tablero()
                    jugador = 'X'
                    if victoria() == True:
                        break
                elif compr[0] == 2 and fila_1[3] == ' ':
                    fila_1[3] = jugador
                    turno += 1
                    tablero()
                    jugador = 'X'
                    if victoria() == True:
                        break
                elif compr[0] == 3 and fila_1[6] == ' ':
                    fila_1[6] = jugador
                    turno += 1
                    tablero()
                    jugador = 'X'
                    if victoria() == True:
                        break
                elif compr[0] == 4 and fila_2[1] == ' ':
                    fila_2[1] = jugador
                    turno += 1
                    tablero()
                    jugador = 'X'
                    if victoria() == True:
                        break
                elif compr[0] == 5 and fila_2[3] == ' ':
                    fila_2[3] = jugador
                    turno += 1
                    tablero()
                    jugador = 'X'
                    if victoria() == True:
                        break
                elif compr[0] == 3 and fila_2[6] == ' ':
                    fila_2[6] = jugador
                    turno += 1
                    tablero()
                    jugador = 'X'
                    if victoria() == True:
                        break
                elif compr[0] == 4 and fila_3[1] == ' ':
                    fila_3[1] = jugador
                    turno += 1
                    tablero()
                    jugador = 'X'
                    if victoria() == True:
                        break
                elif compr[0] == 5 and fila_3[3] == ' ':
                    fila_3[3] = jugador
                    turno += 1
                    tablero()
                    jugador = 'X'
                    if victoria() == True:
                        break
                elif compr[0] == 3 and fila_3[6] == ' ':
                    fila_3[6] = jugador
                    turno += 1
                    tablero()
                    jugador = 'X'
                    if victoria() == True:
                        break
        #Fila 1
            maquina = random.randint(1,9)
            if maquina == 1 and fila_1[1] == ' ':
                fila_1[1] = jugador
                turno += 1
                tablero()
                jugador = 'X'
                if victoria() == True:
                    break
            if maquina == 2 and fila_1[3] == ' ':
                fila_1[3] = jugador
                turno += 1
                tablero()
                jugador = 'X'
                if victoria() == True:
                    break
            if maquina == 3 and fila_1[6] == ' ':
                fila_1[6] = jugador
                turno += 1
                tablero()
                jugador = 'X'
                if victoria() == True:
                    break
        #Fila 2
            if maquina == 4 and fila_2[1] == ' ':
                fila_2[1] = jugador
                turno += 1
                tablero()
                jugador = 'X'
                if victoria() == True:
                    break
            if maquina == 5 and fila_2[3] == ' ':
                fila_2[3] = jugador
                turno += 1
                tablero()
                jugador = 'X'
                if victoria() == True:
                        break
            if maquina == 6 and fila_2[6] == ' ':
                fila_2[6] = jugador
                turno += 1
                tablero()
                jugador = 'X'
                if victoria() == True:
                    break
        #Fila 3
            if maquina == 7 and fila_3[1] == ' ':
                fila_3[1] = jugador
                turno += 1
                tablero()
                jugador = 'X'
                if victoria() == True:
                    break
            if maquina == 8 and fila_3[3] == ' ':
                fila_3[3] = jugador
                turno += 1
                tablero()
                jugador = 'X'
                if victoria() == True:
                    break
            if maquina == 9 and fila_3[6] == ' ':
                fila_3[6] = jugador
                turno += 1
                tablero()
                jugador = 'X'
                if victoria() == True:
                    break            
        
        mov = input('Casilla: ')
        if mov[:2] not in respuestas or len(mov) >= 3:
            print ('Has debido escribir la respuesta mal, por favor, usa LetraNúmero, sin espacios, y, con la letra en mayúscula.')
            print ('Ejemplo: A1')

#Fila 1           
        elif mov[:2] == 'A1':
            if fila_1[1] == ' ':                         #Comprueba que la casilla esté vacía
                fila_1[1] = jugador
                turno += 1
                tablero()
            else:
                print ('Esa casilla ya ha sido seleccionada.')
        elif mov[:2] == 'B1':
            if fila_1[3] == ' ':
                fila_1[3] = jugador
                turno += 1
                tablero()
            else:
                print ('Esa casilla ya ha sido seleccionada.')
        elif mov[:2] == 'C1':
            if fila_1[6] == ' ':
                fila_1[6] = jugador
                turno += 1
                tablero()
            else:
                print ('Esa casilla ya ha sido seleccionada.')

#Fila 2
        elif mov[:2] == 'A2':
            if fila_2[1] == ' ':
                fila_2[1] = jugador
                turno += 1
                tablero()
            else:
                print ('Esa casilla ya ha sido seleccionada.')
        elif mov[:2] == 'B2':
            if fila_2[3] == ' ':
                fila_2[3] = jugador
                turno += 1
                tablero()
            else:
                print ('Esa casilla ya ha sido seleccionada.')
        elif mov[:2] == 'C2':
            if fila_2[6] == ' ':
                fila_2[6] = jugador
                turno += 1
                tablero()
            else:
                print ('Esa casilla ya ha sido seleccionada.')   
                  
#Fila 3
        elif mov[:2] == 'A3':
            if fila_3[1] == ' ':
                fila_3[1] = jugador
                turno += 1
                tablero()
            else:
                print ('Esa casilla ya ha sido seleccionada.')
        elif mov[:2] == 'B3':
            if fila_3[3] == ' ':
                fila_3[3] = jugador
                turno += 1
                tablero()
            else:
                print ('Esa casilla ya ha sido seleccionada.')
        elif mov[:2] == 'C3':
            if fila_3[6] == ' ':
                fila_3[6] = jugador
                turno += 1
                tablero()
            else:
                print ('Esa casilla ya ha sido seleccionada.')
    if turno == 9 and victoria() == False:
        print ('Empate, ¡Bien jugado!')



i = 0
while i == 0:
    print ('Bienvenido a tres en raya')
    jug = int(input('¿Cuántos jugadores van a participar? '))
    if jug >= 3 or jug <= 0:
        print ('Lo sentimos, el número máximo de jugadores es 2, y, el mínimo 1.')
        print ('')
    elif jug == 1:
        difi = int(input('Seleccione dificultad de 1 a 3 '))
        print ('')
        if difi == 1:
            i += 1
            jueg_1()
        elif difi == 2:
            i += 1
            jueg_1_facil()
        elif difi == 3:
            print ('Modo por implementar')
        else:
            print ('De UNO a TRES')  
    else:
        print ('Perfecto, iniciando juego.')
        print ('')
        i += 1
        jueg_2()
