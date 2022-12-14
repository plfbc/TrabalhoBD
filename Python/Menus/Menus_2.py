from DAO import *
from datetime import date
import psycopg2

#Função auxiliar:
def continuar():

    escolha = input(print('Digite Enter para continuar\n'))
    return ''


def ver_planos_conv(cnpj_conv, conn):
    cursor_2 = conn.cursor()


    print("        Planos ofertados: ")
    cursor_2.execute(f"""
    Select Nome from plano_ofertado
    where cnpj_conv = '{cnpj_conv}'
    """)
    
    planos = cursor_2.fetchall()

    return planos   

def verif_conv_pac(cnpj_conv, conn):
    cursor_1 = conn.cursor()
    cursor_1.execute(f"""
    Select nome_conv
    from Convenio
    where cnpj_conv = '{cnpj_conv}'""")
    
    Conv = cursor_1.fetchall()

    
    cursor_1.close()

    return Conv[0][0]
#Formula Query
def form_consulta(Cod_cons):

    query1 = (f""" 
        Select cons.cod_cons, pac.nome, med.nome, cons.data
        from consulta as cons, funcionario as med, paciente as pac

        where cons.cod_cons = '{Cod_cons}'
        and med.id_funcionario = cons.id_med
        and pac.cpf_pac = cons.cpf_pac

    """)

    query2 = (f"""
            Select tipo from exame 
            where cod_cons = '{Cod_cons}'
            
    """)

    query3 = (f"""
                Select descricao from prescreve 
                where cod_cons = '{Cod_cons}'
                
                """)
    
    lista_querys = [query1, query2, query3]
    return lista_querys
    

def form_paciente():

    query = (f""" 
        select * from paciente

    """)

    return query

def form_medicamentos():
    query = (""" 
        select * from medicamento

    """)

    return query

def form_funcionarios():
    query = (""" 
        select * from funcionario
    """)

    return query

#Funções de Consulta:

def verif_consulta(conn):

    print("""
     ---------------------------------- 4US--------------------------------
     |                             **OLA ADMIN**                           |
     |                                                                     |
     |                                                                     |
     |         Digite o nome do Médico para verificar suas consultas:      |
     |                                                                     |
     -----------------------------------------------------------------------
     \n""")
     
    #Consultas disponíveis:
    cursor1 = conn.cursor()
    lista_cons = []
    cursor1.execute("""
    SELECT COD_CONS from CONSULTA""")
    
    consultas = cursor1.fetchall()
    print("Lista de Cod´s de consulta:\n")
    for cods in consultas:
        print(f"""
        Cod_Consulta:{cods[0]}\n
        """)
        lista_cons.append(cods[0])
    cursor1.close()

    cod_cons = None
    while cod_cons not in lista_cons:
        cod_cons = int(input('Digite a consulta que deseja verificar:'))
        
    consulta = form_consulta(cod_cons)

    #Procurando dados da consulta:
    cursor_1 = conn.cursor()
    cursor_2 = conn.cursor()
    cursor_3 = conn.cursor()
    resultados_1 = None
    resultados_2 = None
    resultados_3 = None

    try:
        cursor_1.execute(consulta[0])
        resultados_1 = cursor_1.fetchall()

        cursor_2.execute(consulta[1])
        resultados_2 = cursor_2.fetchall()

        cursor_3.execute(consulta[2])
        resultados_3 = cursor_3.fetchall()
        
    except Exception as Err:
        print(Err)

    #Expondo resultados:
    for resul_1 in resultados_1:
        exames = []
        medicamentos = []
        
        for resul_2 in resultados_2:
            exames.append(resul_2[0])
        
        for resul_3 in resultados_3:
            medicamentos.append(resul_3[0])
        
        print(f"""-------------------------------------------------------
Cod_Cons: {resul_1[0]}
        Nome Paciente: {resul_1[1]} 
        Nome Do Médico: {resul_1[2]}
        Data da consulta: {resul_1[3].year}-{resul_1[3].month}-{resul_1[3].day}
        Exames: {exames}
        Medicamentos:{medicamentos}
        """)
            
    cursor_1.close()
    cursor_2.close()
    cursor_3.close()
    continuar()

def verif_paciente(conn):

    print("""
     ---------------------------------- 4US--------------------------------
     |                             **OLA ADMIN**                           |
     |                                                                     |
     |                                                                     |
     |                Pacientes cadastrados em sua clínica:                |
     |                                                                     |
     -----------------------------------------------------------------------
     """)

    consulta = form_paciente()

    cursor = conn.cursor()
    resultados = None

    try:
        cursor.execute(consulta)
        resultados = cursor.fetchall()
        
    except Exception as Err:
        print(Err)

    for resultado in resultados:
        print(f"""-------------------------------------------------------
        CPF do Paciente: {resultado[0]}
        Sexo do Paciente: {resultado[1]}
        Nome do Paciente: {resultado[2]}
        Data de Nascimento do paciente: {resultado[3].year}-{resultado[3].month}-{resultado[3].day}
        telefone de contato: {resultado[10]}
        Convenio do Paciente: {verif_conv_pac(resultado[4], conn)}    
        """)
        planos = ver_planos_conv(resultado[4],conn)
        for plano in planos:
            print(f'        {plano[0]}')
        
    cursor.close()
    continuar()

def verif_medicamento(conn):

    print("""
     ---------------------------------- 4US--------------------------------
     |                             **OLA ADMIN**                           |
     |                                                                     |
     |                                                                     |
     |                Medicamentos disponíveis em sua clínica:             |
     |                                                                     |
     -----------------------------------------------------------------------
     """)

    consulta = form_medicamentos()

    cursor = conn.cursor()
    resultados = None

    try:
        cursor.execute(consulta)
        resultados = cursor.fetchall()
        

    except Exception as Err:
        print(Err)

    for resultado in resultados:
        print(f"""-------------------------------------------------------
        Codigo do Medicamento: {resultado[0]}
        Quantidade Disponível: {resultado[1]}
        Nome do Medicamento: {resultado[2]}
        Tipo do Medicamento: {resultado[3]}""")
    
    cursor.close()
    continuar()

def verif_funcionario(conn):
    
    print("""
     ---------------------------------- 4US--------------------------------
     |                             **OLA ADMIN**                           |
     |                                                                     |
     |                                                                     |
     |                Funcionários cadastros em sua clínica:               |
     |                                                                     |
     -----------------------------------------------------------------------
     """)

    consulta = form_funcionarios()

    
    cursor = conn.cursor()
    resultados = None

    try:
        cursor.execute(consulta)
        resultados = cursor.fetchall()
 
 
    except Exception as Err:
        print(Err)
   
   
    for resultado in resultados:
        print(f"""-------------------------------------------------------
Id do Funcionário:{resultado[0]}
        Cargo do funcionário: {resultado[1]}
        Sexo do funcionário:{resultado[2]}
        Data de nascimento do funcionário: {resultado[3].year}-{resultado[3].month}-{resultado[3].day}
        CPF do Funcionário:{resultado[4]}
        Salario do funcionário:{resultado[5]}
        Nome do paciente:{resultado[6]}
        CRE do funcionário:{resultado[7]}
        CRM do funcionário:{resultado[8]}
        Média de Avaliação:{resultado[9]}
        Telefone 1 do funcionário: {resultado[10]}
        Telefone 2 do funcionário: {resultado[11]}\n""")
    
    cursor.close()
    continuar()

