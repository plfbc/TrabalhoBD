from psycopg2 import  connect


def conection():
    nomebanco = "Medico"
    senha = 'postgres'
    usuario = 'postgres'
    return connect(dbname = nomebanco, password = senha, user = usuario)
