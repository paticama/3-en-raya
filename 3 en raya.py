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

def jueg_1():
    print ('Estás solo, ja')
    
def jueg_2():
    tablero()
    respuestas = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']  #Sirve para comprobar que las casillas existen
    turno = 0
    jugador = 'X'
    print (f'Empieza {jugador}')
    while turno < 9:                                             #Va cambiando entre X y O
        if victoria() == True:
            break
        if turno % 2 == 0 or turno == 0:
            jugador = 'X'
        else:
            jugador = 'O'
        
        mov = input('Casilla: ')
        if mov[:2] not in respuestas or len(mov) >= 3:
            print ('Has debido escribir la respuesta mal, por favor, usa LetraNúmero, sin espacios, y, con la letra en mayúscula, ejemplo, A1')
#Fila 1           
        elif mov[:2] == 'A1':
            if fila_1[1] == ' ':                         #Comprueba que la casilla esté vacía
                fila_1[1] = jugador
                turno += 1
                tablero()
            else:
                print ('Esa casilla ya ha sido seleccionada')
        elif mov[:2] == 'B1':
            if fila_1[3] == ' ':
                fila_1[3] = jugador
                turno += 1
                tablero()
            else:
                print ('Esa casilla ya ha sido seleccionada')
        elif mov[:2] == 'C1':
            if fila_1[6] == ' ':
                fila_1[6] = jugador
                turno += 1
                tablero()
            else:
                print ('Esa casilla ya ha sido seleccionada')

#Fila 2
        elif mov[:2] == 'A2':
            if fila_2[1] == ' ':
                fila_2[1] = jugador
                turno += 1
                tablero()
            else:
                print ('Esa casilla ya ha sido seleccionada')
        elif mov[:2] == 'B2':
            if fila_2[3] == ' ':
                fila_2[3] = jugador
                turno += 1
                tablero()
            else:
                print ('Esa casilla ya ha sido seleccionada')
        elif mov[:2] == 'C2':
            if fila_2[6] == ' ':
                fila_2[6] = jugador
                turno += 1
                tablero()
            else:
                print ('Esa casilla ya ha sido seleccionada')
            
#Fila 3
        elif mov[:2] == 'A3':
            if fila_3[1] == ' ':
                fila_3[1] = jugador
                turno += 1
                tablero()
            else:
                print ('Esa casilla ya ha sido seleccionada')
        elif mov[:2] == 'B3':
            if fila_3[3] == ' ':
                fila_3[3] = jugador
                turno += 1
                tablero()
            else:
                print ('Esa casilla ya ha sido seleccionada')
        elif mov[:2] == 'C3':
            if fila_3[6] == ' ':
                fila_3[6] = jugador
                turno += 1
                tablero()
            else:
                print ('Esa casilla ya ha sido seleccionada')
    if turno == 9:
        print ('Empate')

i = 0
while i == 0:
    print ('Bienvenido a tres en raya')
    jug = int(input('¿Cuántos jugadores van a participar? '))
    if jug >= 3 or jug <= 0:
        print ('Lo sentimos, el número máximo de jugadores es 2, y, el mínimo 1')
        print ('')
    elif jug == 1:
        print ('Perfecto, iniciando juego')
        print ('')
        i += 1
        jueg_1()
    else:
        print ('Perfecto, iniciando juego')
        print ('')
        i += 1
        jueg_2()
