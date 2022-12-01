import time 
import os
import json
from flask import Flask, jsonify, Response, request



app = Flask(__name__)

with open("dic_usuarios.json") as file:
    usuarios = json.load(file) 



#################### MENU INICIO SESION #####################################    

def menu_usuarios():
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
            menu_usuarios()
        return in_menu
    except:
        print('Error... Ingrese 1 o 2')
        time.sleep(1)
        os.system('cls')
        menu_usuarios()
        
def iniciar_sesion(dic_usuarios):
    usuario_1=input("ingrese usuario: ")
    contrasenia_1=input(int("ingrese contrasenia: "))
    for usuario_1 in dic_usuarios:
        if usuario_1 in dic_usuarios["nombre y apellido"]:  
            return menu_principal 
        else:
            return "usuario o contrasenia incorrecta"

            

                
    
                
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
    in_menu = menu_usuarios()      
    return in_menu
        
########### MAIN #####################################################
in_menu = imprimir_menu()
# Solo puede salir del menu con un 1 o 2. No hay posibilidad de que tome otro valor
"""if in_menu == 1:
    iniciar_sesion()
else:
    modo_libre() """