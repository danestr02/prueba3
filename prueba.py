import funcion as fn

jugador=[]
juego={1:'Fornite', 2:'Valorant', 3:'FIFA'}
idjugador=''
nombres=''
juegoss=0
puntajeObt=0
nivelJuego=0
opcionMenu=0
opc=0

while opc<4:
    fn.menu()
    opc=fn.validarNum(opcionMenu,"Ingrese una opción ----> ",1,5)
    if opc==1:
        fn.opcion1(jugador,idjugador,nombres,juegoss,puntajeObt,nivelJuego)
        print(jugador)
    elif opc==2:
        for i in jugador:
            print(i)
    elif opc==4:
        print("Saliendo del programa...")


