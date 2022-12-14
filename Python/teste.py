import psycopg2
from DAO.CLASSESMEDICO import funcionario 
nomebanco = "Medico"
senha = 'postgres'
usuario = 'postgres'
conn = psycopg2.connect(dbname = nomebanco, password = senha, user = usuario)


# def correcao_erro_id(ID:str, conn):
#     cursor1 = conn.cursor()    
#     cursor1.execute(""" SELECT ID_Funcionario from funcionario
#     """)
#     IDS = cursor1.fetchall()
#     cursor1.close()

#     while not ID.isnumeric() or (ID  in IDS):
#         if not ID.isnumeric():
#                 print("Valor inválido! ID precisar ser inteiro")
#                 ID = input("ID DO FUNCIONÁRIO: ")
#         elif ID in IDS:
#                 print("Valor inválido! ID já existe na lista de funcionarios")
#                 ID = input("ID DO FUNCIONÁRIO: ")
#     return ID


# ID_FUNCIONARIO = input("ID DO FUNCIONÁRIO: ")
# ID_FUNCIONARIO = correcao_erro_id(ID_FUNCIONARIO)


A = input('teste: ')

print([A,A])