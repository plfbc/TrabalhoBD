import psycopg2

def excluir_funcionario(conn):
    cursor = conn.cursor()
    
    cursor.execute(f"""
                   select id_funcionario, nome, cargo from funcionario
                   """)
    
    ids_funcs = cursor.fetchall()
    
    ids_funcs = [ids_funcs[i] for i in range(len(ids_funcs))]
    print("------------------------------------------------------------")
    
    for item in ids_funcs:
        print(f"ID: {item[0]} - Funcionário: {item[1]} - Cargo: {item[2]}")
    
    print("------------------------------------------------------------")
    
    id_func = input("\nDigite o ID do Funcionário que deseja excluir: ")
    
    try:
        cursor.execute(f"""
            delete from funcionario where id_funcionario = {id_func}
            """)
    except:
        print("Funcionário não encontrado")
    
    print("Funcionário Excluído com Sucesso")
    conn.commit()



def excluir_paciente(conn):
    cursor = conn.cursor()
    
    cursor.execute(f"""
                   select cpf_pac, nome from paciente
                   """)
    
    cpfs_paciente = cursor.fetchall()
    
    cpfs_paciente = [cpfs_paciente[i] for i in range(len(cpfs_paciente))]
    print("------------------------------------------------------------")
    
    for item in cpfs_paciente:
        print(f"CPF: {item[0]} - Paciente: {item[1]}")
    
    print("------------------------------------------------------------")
    
    cpf_func = input("\nDigite o CPF do Funcionário que deseja excluir (Apenas dígitos): ")
    
    cpf_func = f"{cpf_func[:3]}.{cpf_func[3:6]}.{cpf_func[6:9]}-{cpf_func[9:]}"
    
    try:
        cursor.execute(f"""
            delete from paciente where cpf_pac = '{cpf_func}'
            """)
    except:
        print("Paciente não encontrado")
    
    print("Paciente Excluído com Sucesso")
    conn.commit()



def excluir_consulta(conn):
    cursor = conn.cursor()
    
    cursor.execute(f"""
                   select cod_cons, paciente.nome, funcionario.nome, data
                   from consulta, paciente, funcionario
                   where consulta.cpf_pac = paciente.cpf_pac and
                   consulta.id_med = funcionario.id_funcionario
                   """)
    
    consultas = cursor.fetchall()
    
    consultas = [consultas[i] for i in range(len(consultas))]
    print("------------------------------------------------------------")
    
    for item in consultas:
        print(f"Código Consulta: {item[0]} - Médico: {item[1]} - Paciente: {item[2]} - Data: {item[3].year}/{item[3].month}/{item[3].day}")
    
    print("------------------------------------------------------------")
    
    cod_consu = input("\nDigite o Código da Consulta que deseja excluir: ")
    
    try:
        cursor.execute(f"""
            delete from consulta where cod_cons = '{cod_consu}'
            """)
    except:
        print("Código não encontrado")
    
    print("Consulta Excluída com Sucesso")
    conn.commit()



def excluir_medicamento(conn):
    cursor = conn.cursor()
    
    cursor.execute(f"""
                   select cod_medicamento, nome, tipo from medicamento
                   """)
    
    medicamentos = cursor.fetchall()
    
    medicamentos = [medicamentos[i] for i in range(len(medicamentos))]
    print("------------------------------------------------------------")
    
    for item in medicamentos:
        print(f"Código Medicamento: {item[0]} - Nome: {item[1]} - Tipo: {item[2]}")
    
    print("------------------------------------------------------------")
    
    cod_med = input("\nDigite o Código do Medicamento que deseja excluir: ")
    
    try:
        cursor.execute(f"""
            delete from medicamento where cod_medicamento = {cod_med}
            """)
    except:
        print("Medicamento não encontrado")
    
    print("Medicamento Excluído com Sucesso")
    conn.commit()