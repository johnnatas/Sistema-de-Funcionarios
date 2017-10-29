import os
from crud import Crud

class Form():

    #Instancia global
    c = Crud()

# --------------------------------- Fomulário de inserir --------------------------------------
    def inserir(self):
        confere = False
        while(not confere): # se não conferir os dados retorna daqui
            print ("\n\n ------------------ INSERIR FUNCIONARIO ------------------\n\n")
            print ("Insira os seguintes dados\n")

            dados = []

            dados.append(input("Nome: "))
            dados.append(float(input("Salário: ")))
            dados.append(input("Sexo (F/M): "))
            dados.append(int(input("CPF: ")))

            print("\nVocê cadastrou:\n")

            for d in dados:
                print(d) #exibição dos dados inseridos
            
            confere = input("\nConfere os dados? (s/n)") #confirmação dos dados

            if confere == "s" or confere == "S":
                confere = True
                self.c.cadastrar(dados) #injeta o array de dados no método de cadastrar da Classe Crud do arquivo crud.py
            else:
                confere = False
                os.system('cls')

# --------------------------------- Fomulário de Remover --------------------------------------

    def remover(self):
        confere = False
        while(not confere):
            print ("\n\n ------------------ DELETAR FUNCIONARIO ------------------\n\n")
            
            id = int(input("Digite o ID do funcionario que deseja deletar: "))

            print("\n\nVocê digitou:\n")
            print(id)

            confere = input("\nConfere os dados? (s/n)")

            if confere == "s" or confere == "S":
                confere = True
                self.c.deletar(id)
            else:
                confere = False
                os.system('cls')


# --------------------------------- Fomulário de Listar --------------------------------------
    
    def listar(self):
        continuar = True
        while(continuar):
            print ("\n\n ------------------ LISTAR FUNCIONARIO ------------------\n\n")
            
            #listando todos os funcionarios cadastrados
            ## self.c.list-all()

            nome = int(input("Digite o npme do funcionario que deseja pesquisar: "))

            print("\nVocê cadastrou:\n")
            print(nome)

            continuar = input("\nGostaria de listar mais funcionarios? (s/n)")

            if continuar == "s" or continuar == "S":
                continuar = True
                #lista somente os funcionarios com o nome digitado
                self.c.list-one(nome)
                os.system('cls')
            else:
                continuar = False