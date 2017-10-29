import mysql.connector #importando o conector mysql

class Banco(object):

    #variavel global que permite acesso ao cursor em outras classes
    global c

    #conexão iniciada ao instanciar esta classe
    def __init__(self):
        try:
            cnx = mysql.connector.connect(host='localhost',
                                   database='database',
                                   user='root',
                                   password='')
            self.c = cnx.cursor

        except:
             print ("Erro ao se conectar a base de dados!")
    
    
    #finaliza assim que terminar o uso da classe
    def __del__(self):
        print ("Conexão finalizada!")
        del(self)
