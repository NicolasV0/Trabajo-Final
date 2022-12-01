import time 
import os

dic_usuarios = {'Usuario001': {'Nombre y Apellido':'Nicolas Vaylet', 'Contraseña':111111},
                'Usuario002': {'Nombre y Apellido':'Joaquin Allende', 'Contraseña':111112},
                'Usuario003': {'Nombre y Apellido':'Javier Balmaceda', 'Contraseña':111113},
                'Usuario004': {'Nombre y Apellido':'Martin Troilo', 'Contraseña':111114},
                'Usuario005': {'Nombre y Apellido':'Marco Urtarroz', 'Contraseña':111115},
                'Usuario006': {'Nombre y Apellido':'Carlos Berger', 'Contraseña':111116},
                'Usuario007': {'Nombre y Apellido':'Mauro Torre', 'Contraseña':111117},
                'Usuario008': {'Nombre y Apellido':'Camila Iniguez', 'Contraseña':111118},
                'Usuario009': {'Nombre y Apellido':'Constanza Gonzalez', 'Contraseña':111119},
                'Usuario010': {'Nombre y Apellido':'Micaela Perez', 'Contraseña':211111},
                'Usuario011': {'Nombre y Apellido':'Simona Garcia', 'Contraseña':211112},
                'Usuario012': {'Nombre y Apellido':'Genaro Fernandez', 'Contraseña':211113},
                'Usuario013': {'Nombre y Apellido':'Cristina Aguilera', 'Contraseña':211114},
                'Usuario014': {'Nombre y Apellido':'Alberto Comodoro', 'Contraseña':211115}}


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
            menu_usuarios()
        return in_menu
    except:
        print('Error... Ingrese 1 o 2')
        time.sleep(1)
        os.system('cls')
        menu_usuarios()
                
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
        try:
            contraseña = int(input('Ingrese Contraseña: '))
        except:
            print('Error de dato, vuelva a intentarlo')
            flag = True    
        for us in dic_usuarios['usuarios']:    
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
in_menu = imprimir_menu()
# Solo puede salir del menu con un 1 o 2. No hay posibilidad de que tome otro valor
if in_menu == 1:
    iniciar_sesion()
else:
    modo_libre() 