import time 
import os

usuarios = [
    {
    "Nombre y Apellido":"Nicolas Vaylet",
    "contrasenia":111111
    },
    {"Nombre y Apellido":"Joaquin Allende",
     "contrasenia":111112
    },
    {"Nombre y Apellido":"Javier Balmaceda",
     "contrasenia":111113
    },
    {"Nombre y Apellido":"Martin Troilo",
     "contrasenia":111114
    },
    {"Nombre y Apellido":"Marco Urtarroz",
     "contrasenia":111115
    },
    {"Nombre y Apellido":"Carlos Berger",
     "contrasenia":111116
    },
    {"Nombre y Apellido":"Mauro Torre",
     "contrasenia":111117
    },
    {"Nombre y Apellido":"Camila Iniguez",
     "contrasenia":111118
    },
    {"Nombre y Apellido":"Constanza Gonzalez",
     "contrasenia":111119
    },
    {"Nombre y Apellido":"Micaela Perez",
     "contrasenia":211111
    },
    {"Nombre y Apellido":"Simona Garcia",
     "contrasenia":211112
    },
    {"Nombre y Apellido":"Genaro Fernandez",
     "contrasenia":211113
    },
    {"Nombre y Apellido":"Cristina Aguilera",
     "contrasenia":211114
    },
    {"Nombre y Apellido":"Alberto Comodoro", 
    "contrasenia":211115
    }                   
]

#################### MENU INICIO SESION #####################################    
def menu_usuarios():
    while(True):
        print('+--------------------------+')
        print('|                          |')
        print('|1)   Inicie sesion        |')
        print('|2)   Modo libre           |')
        print('|                          |')
        print('+--------------------------+')
        try:
            in_menu = int(input())
            if (in_menu != 1) and (in_menu !=2):
                print('Error... Ingrese 1 o 2')
                time.sleep(1)
                os.system('cls')
            elif (in_menu == 1 or in_menu == 2):
                return in_menu
        except:
            print('Error... Ingrese 1 o 2')
            time.sleep(1)
            os.system('cls')
                
#################### MENU PRINCIPAL #####################################    
def imprimir_menu():
    print('\033[0;31m' +'+--------------------------------------------------------------+'+'\033[0;m')
    print('\033[0;31m' +'|                                                              |'+'\033[0;m')
    print('\033[0;31m' +'|       N    N  NNNNN  NNNNN  NNNNN  N      NNNNN  N   N       |'+'\033[0;m')
    print('\033[0;31m' +'|       NN   N  N        N    N      N      N   N   N N        |'+'\033[0;m')
    print('\033[0;31m' +'|       N N  N  NNN      N    NNN    N      N   N    N         |'+'\033[0;m')
    print('\033[0;31m' +'|       N  N N  N        N    N      N      N   N   N N        |'+'\033[0;m')
    print('\033[0;31m' +'|       N   NN  NNNNN    N    N      NNNNN  NNNNN  N   N       |'+'\033[0;m')
    print('\033[0;31m' +'|                                                              |'+'\033[0;m')
    print('\033[0;31m' +'+--------------------------------------------------------------+'+'\033[0;m')
    time.sleep(2 )
    os.system('cls')      
    return

#########################INICIAR SESION##################################
def iniciar_sesion():
    while (True):
        flag = False
        usuario = input('Ingrese Nombre y Apellido: ')
        contraseña = int(input('Ingrese Contraseña: '))
        for us in usuarios:
            if us['Nombre y Apellido'] == usuario:
                if us['contrasenia'] == contraseña:
                    print('Has iniciado sesion')
                    return
                else:
                    print('Contrasenia incorrecta')
                    flag = True
                    continue
        if flag == False:            
            print('Usuario inxistente')
        print('1) Para Menu de inicio')
        print('2) Para modo libre')
        print('3) Para volver a intentar')
        print('4) Para cerrar')
        opcion = int(input('Como desea continuar: '))
        if opcion == 1:
            os.system('cls')      
            return
        if opcion == 2:
        #modo_libre()
            print('modo libre')
            exit(1)
        if opcion == 3:
            os.system('cls')
            continue
        if opcion == 4:
            exit(1)
        
                
            
        
    
        
########### MAIN #####################################################
imprimir_menu()
while(True):
    in_menu = menu_usuarios()
    # Solo puede salir del menu con un 1 o 2. No hay posibilidad de que tome otro valor
    try:
        if in_menu == 1:
            iniciar_sesion()
            print('Saliste bien')
        elif in_menu == 2:
            print('modo_libre()')
    except:
        print('Error')