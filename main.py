# Início da aplicação

import os
from formularios import Form

class Main():

    f = Form() #instancia de Forms do arquivo formularios.py
    continuar = True #inicializando variável

    while(continuar): # loop para se o usuário quiser continuar executando a aplicação
        print ("\n\n ------------------ CRUD FUNCIONARIO ------------------\n\n")
        print ("#1 -  Inserir Funcionário")
        print ("#2 -  Remover Funcionário")
        print ("#3 -  Listar Funcionário")
        
        op = input("\nEscolha uma opção: ")

        # "switch case"
        if op == "1":
            os.system('cls') #limpa tela
            f.inserir() #chama método na classe Forms
        elif op == "2":
            os.system('cls')
            f.remover()
        elif op == "3":
            os.system('cls')
            f.listar()
        else:
            print ("opção invalida")

        q = input("Deseja continuar? (s/n)")

        if q == "s":
            continuar = True
            os.system('cls')
        else:
            continuar = False
        
