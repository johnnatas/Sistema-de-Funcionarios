from banco import Banco

b = Banco()
b.__del__()

'''
cursor = cnx.cursor() #criando cursor

dados = "call `database`.INSERTTAB('Jonatas', 1200, 'M', 44485312879, @V_RESPOSTA)"

try:
    cursor.execute(dados)
    cnx.commit()
    print("Inserido com sucesso")
except:
    print("Falhou :( ")

cnx.close()
'''
