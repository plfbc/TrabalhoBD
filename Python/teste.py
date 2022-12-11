import psycopg2
from DAO.CLASSESMEDICO import funcionario 


nomebanco = "Medico"
senha = 'postgres'
usuario = 'postgres'

conn = psycopg2.connect(dbname = nomebanco, password = senha, user = usuario)
cursor = conn.cursor()

cursor.execute("""
SELECT * from Funcionario

""")


A = cursor.fetchall()

teste = funcionario(A[0],A[1],A[2],A[3],A[4],A[5],A[6],A[7],A[8],A[9],A[10],A[11])

print(teste)
cursor.close()