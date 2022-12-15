from psycopg2 import  connect


def conection():
    nomebanco = "postgres"
    senha = 'admlila'
    usuario = 'postgres'
    return connect(dbname = nomebanco, password = senha, user = usuario)