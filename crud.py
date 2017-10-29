#importaçao da classe Banco do arquivo banco.py
from banco import Banco

# --- Erro ao inserir ---
class Crud():

    def cadastrar(self, dados):
        b = Banco()
        
        d = "'" + dados[0] +"', "+ str(dados[1]) +", '"+ dados[2] + "', " + str(dados[3]) + ", @V_RESPOSTA"
        #print("")
        env = b.c() #tornando env o cursor

        try:
            env.execute("call database.INSERTTAB(" + d +")") #inserindo dados do array
            print("Cadastrado com sucesso!")
        except:
            print("Não foi possível cadastrar funcionário")


    def deletar(self, id):
        b = Banco()
        
        d = str(id)
        env = b.c() #tornando env o cursor

        try:
            env.execute("call database.DELETELINE(" + d +", @resposta)") #inserindo dados do array
            print("Deletado com sucesso!")
        except:
            print("Não foi possível deletar funcionário")

    def listar(self, id):
        b = Banco()
        
        d = str(id)
        env = b.c() #tornando env o cursor

        try:
            env.execute("call database.SELECTTAB_(" + d +", @resposta)") #inserindo dados do array
            print("Deletado com sucesso!")
        except:
            print("Não foi possível deletar funcionário")