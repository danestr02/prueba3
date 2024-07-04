def menu():
    print('*'*30)
    print('Bienvenido a eSports eShirlitos!')
    print('*'*30)
    print('''Ingrese una opción:
        1.- Registrar puntaje torneo
        2.- Listar los todos puntajes
        3.- Imprimir por Tipo
        4.- Salir del programa''')
    
def validarNum(ingreso,mensajeIngreso,numMin,numMax):
    while ingreso < numMin or ingreso > numMax:
        try:
            ingreso=int(input(mensajeIngreso))
            if ingreso < numMin or ingreso > numMax:
                print("El numero ingresado esta fuera de rango, reintente...")
        except:
            print("El valor ingresado no es válido, reitente...")
    return ingreso

def opcion1(lista,var1,var2,var3,var4,var5):
    var1=input("Ingrese su ID de jugador: ")
    lista.append(var1)
    var2=input("ingrese su nombre y apellido: ")
    lista.append(var2)
    validarNum(var3,"Indique el juego en el que NO participó 1)Fornite 2)Valorant 3)FIFA: ",1,3)
    juego1='Fornite'
    juego2='Valorant'
    juego3='FIFA'
    if var3==1:
        lista.append(juego2)
        lista.append(juego3)
    elif var3==2:
        lista.append(juego1)
        lista.append(juego3)
    else:
        lista.append(juego1)
        lista.append(juego2)
    var4=int(input("Ingrese el puntaje obtenido en los juegos:"))
    lista.append(var4)
    var5=int(input("Ingrese su nivel: 1)Principiante 2)Intermedio 3)Avanzado: "))
    if var5==1:
        nivel='Principiante'
    elif var5==2:
        nivel='Intermedio'
    else:
        nivel='Avanzado'
        lista.append(nivel)
    return lista,var1,var2,var3,var4,var5,nivel,juego1,juego2,juego3


