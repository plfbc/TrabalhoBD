from DAO import CLASSESMEDICO
import psycopg2

# ID_FUNCIONARIO:int,CARGO:str,SEXO:str,DATA_DE_NASC,
# CPF:str, SALARIO:float,NOME:str,
# CRE:str,CRM:str,MEDIA_Av,TELEFONE1:str,TELEFONE2:str
def mensagem():
    print("Inserido com sucesso!")

def converte_tel(TEL):
    Tele = f'({TEL[0:2]}) {TEL[2:7]}-{TEL[7:]}'

    return Tele

def converte_cpf(CPFF):
    pass

def converte_cnpj(CNPJ):
    pass



#Correção de Erro das Inserções
def correcao_erro_id(ID:str, conn):
    cursor1 = conn.cursor()    
    cursor1.execute(""" SELECT ID_Funcionario from funcionario
    """)
    IDS = cursor1.fetchall()
    cursor1.close()

    while not ID.isnumeric() or (ID  in IDS):
        if not ID.isnumeric():
                print("Valor inválido! ID precisa                                                                                                                                                                                                ser inteiro")
                ID = input("ID DO FUNCIONÁRIO: ")
        elif ID in IDS:
                print("Valor inválido! ID já existe na lista de funcionarios")
                ID = input("ID DO FUNCIONÁRIO: ")
    return ID

def correcao_erro_id_med(ID:str, conn):
    cursor1 = conn.cursor()    
    cursor1.execute(""" SELECT ID_Funcionario, cargo from funcionario where cargo = 'Médico(a)'
    """)
    IDS = cursor1.fetchall()
    cursor1.close()

    while not ID.isnumeric() or (ID  in IDS):
        if not ID.isnumeric():
                print("Valor inválido! ID precisa                                                                                                                                                                                                 ser inteiro")
                ID = input("ID DO MÉDICO: ")
        elif ID in IDS:
                print("Valor inválido! ID já existe na lista de médicos")
                ID = input("ID DO MÉDICOS: ")
    return ID

def correcao_erro_CEP(CEPP):
    while len(CEPP) != 8 or int(CEPP).alpha:
        print("ERRO NA INSERÇÃO DE DADOS, tente novamente: ")
        CEPP = input("CEP do Paciente apenas dígitos: ")
    return CEPP

def correcao_erro_tel(tel:str):
    while len(tel) != 11 or not tel.isnumeric() or not tel in ['']:
        print("Valor inválido!O número de telefone deve ter 11 dígitos e ser número")
        tel = str(input("Número de telefone: "))
    
    return tel

def correcao_erro_data(data:list):
    dia = data[0]
    mes = data[1]
    ano = data[2]
    
    while int(dia) < 1 or int(dia) > 31 or not dia.isnumeric():
        print("Valor do dia inválido!")
        dia = (input("Dia: "))
        data[0] = dia
        
    while int(mes) < 1 or int(mes) > 12 or not mes.isnumeric():
        print("Valor do mês inválido!")
        mes = (input("Mes: "))
        data[1] = mes
        
    while len(ano) != 4 or not ano.isnumeric() or int(ano) < 1925 or int(ano) > 2022:
        print("Valor inválido! ano tem 4 dígitos")
        ano = (input("Ano: "))
        data[2] = ano
    
    return data

def correcao_erro_CPF(CPFF:str):
    while len(CPFF) != 11:
        print("ERRO! O CPF contém 11 digitos")
        CPFF = input("Digite o CPF:")
    return CPFF
     
def pegar_CPF_pac(conn,CPFF):
    cursor1 = conn.cursor()
    cursor1.execute("""
    SELECT NOME, CPF_pac from PACIENTE""")
    
    pacientes = cursor1.fetchall()

    nomesP = []
    for paciente in pacientes:
        nomesP.append(paciente[1].replace('.','').replace('-',''))  

    cursor1.close()
    while CPFF not in nomesP:
       print("CPF não consta no banco, tente novamente: ")
       CPFF = input("Digite o CPF do paciente: ") 
    return CPFF

def correcao_erro_salario(SAL:str):

    efloat = False
    while not efloat:
        try : 
            SAL = float(SAL)
            efloat = True
        except:
            print("ERRO, Sálario inválido! digite novamente: ")
            SAL = input("Salario do funcionario: ")
            efloat= False

    return SAL
        
def correcao_erro_Media(Media):

    efloat = False
    taNoIntervalo = False
    while not efloat or not taNoIntervalo:
        try : 
            Media = float(Media)
            efloat = True
        except:
            print("ERRO, Média inválido! digite novamente: ")
            Media = input("Média do atendimento: ")
            efloat= False

        if Media < 0 or Media > 10:
            print("ERRO NA INSERCAO DOS DADOS, tente novamente: ")
            Media = input("Media de avaliação do funcionario: ")
        else:
            taNoIntervalo = True

    return Media

def correcao_erro_COD_MED(COD_MEDICAMENTO, conn):
    cursor1 = conn.cursor()    
    cursor1.execute(""" SELECT COD_MEDICAMENTO from medicamento
    """)
    CODS = cursor1.fetchall()
    cursor1.close()

    while not COD_MEDICAMENTO.isnumeric() or (COD_MEDICAMENTO  in CODS):
        if not COD_MEDICAMENTO.isnumeric():
                print("Valor inválido! código do medicamento precisar ser inteiro")
                COD_MEDICAMENTO = input("COD DO MEDICAMENTO: ")
        elif COD_MEDICAMENTO in CODS:
                print("Valor inválido! código do medicamento já existe na lista de medicamentos")
                COD_MEDICAMENTO = input("COD DO MEDICAMENTO: ")
    return COD_MEDICAMENTO




#Cadastro de Dados:
def cadastrar_funcionario(conn):
    
    ID_FUNCIONARIO = input("ID DO FUNCIONÁRIO: ")
    ID_FUNCIONARIO = correcao_erro_id(ID_FUNCIONARIO,conn)

    print("""
    Enfermeiro(a) [1]
    Medico(a)     [2]
    Outro         [3]
    """
    )

    CARGO = str(input("Cargo do funcionario: "))

   
    print("""
    Feminino  [1]
    Masculino [2]"""
    )
    SEXO = str(input("Sexo do funcionario: "))


    while SEXO not in ['1','2', 'Feminino', 'Masculino']:
            SEXO = str(input("Opção inválida!\nSexo do funcionario: "))

    if SEXO in ['1','Feminino']:
        SEXO = 'Feminino'
    elif SEXO in ['2','Masculino']:
        SEXO = 'Masculino'



    DIA = (input("Dia do nascimento do Funcionário: "))
    MES = (input("Mês do nascimento do Funcionário: "))
    ANO = (input("Ano do nascimento do Funcionário: "))
    
    DATA_DE_NASC = [DIA, MES, ANO ]
    DATA_DE_NASC = correcao_erro_data(DATA_DE_NASC)

    CPF = str(input("CPF do funcionário: "))
    CPF = correcao_erro_CPF(CPF)

    SALARIO = (input("Salario do funcionário: "))
    SALARIO = float(correcao_erro_salario(SALARIO))

    NOME = str(input("Nome do funcionário: "))

    CRE = str(input("CRE do funcionário: "))

    CRM = str(input("CRM do funcionário: "))

    MEDIA_Av = (input("Media de avaliação do funcionário: "))
    MEDIA_Av = float(correcao_erro_Media(MEDIA_Av))

    TELEFONE1 = str(input("Primeiro número de telefone do funcionário: "))
    TELEFONE1 = correcao_erro_tel(TELEFONE1)

    TELEFONE2 = str(input("Segundo número de telefone do funcionário: "))
    TELEFONE2 = correcao_erro_tel(TELEFONE2)
    
    temp = CLASSESMEDICO.funcionario(ID_FUNCIONARIO,CARGO, SEXO, DATA_DE_NASC, CPF, SALARIO, NOME, CRE, CRM, MEDIA_Av, TELEFONE1, TELEFONE2)
    
    cursor = conn.cursor()

    try :
        cursor.execute(f"""
        INSERT INTO FUNCIONARIO(ID_FUNCIONARIO, CARGO, SEXO, DATA_DE_NASC, CPF, SALARIO, NOME, CRE, CRM, MEDIA_Av, TELEFONE1, TELEFONE2) 
        VALUES ({temp.ID_FUNCIONARIO},'{temp.CARGO}',{temp.SEXO},'{temp.DATA_DE_NASC[2]}-{temp.DATA_DE_NASC[1]}-{temp.DATA_DE_NASC[0]}',{temp.CPF},{temp.SALARIO},
        '{temp.NOME}', {temp.CRE},{temp.CRM},{temp.MEDIA_Av},{temp.TELEFONE1},{temp.TELEFONE2})
        """)

        mensagem()
        conn.commit()

    except Exception as Err:
        print(Err)
    
    cursor.close

def cadastrar_paciente(conn):

    #CPF_PAC, SEXO, NOME, DATA_DE_NASC, CNPJ_CONV, CEP, RUA, BAIRRO, COMPLEMENTO, NUMERO, TELEFONE1, TELEFONE2

    CPF_PAC = str(input("CPF do paciente, apenas dígitos: "))
    CPF_PAC = correcao_erro_CPF(CPF_PAC)

    NOME = str(input("Nome do Paciente: "))

    print("""
    Feminino  [1]
    Masculino [2]"""
    )
    SEXO = str(input("Sexo do paciente: "))


    while SEXO not in ['1','2', 'Feminino', 'Masculino']:
            SEXO = str(input("Opção inválida!\nSexo do paciente: "))

    if SEXO in ['1','Feminino']:
        SEXO = 'Feminino'
    elif SEXO in ['2','Masculino']:
        SEXO = 'Masculino'
    

    DIA = (input("Dia do nascimento do Paciente: "))
    MES = (input("Mês do nascimento do Paciente: "))
    ANO =(input("Ano do nascimento do Paciente: "))
    
    DATA_DE_NASC = [DIA, MES, ANO ]
    DATA_DE_NASC = correcao_erro_data(DATA_DE_NASC)

    CNPJ_CONV = str(input("CNPJ do convênio do Paciente: "))

    CEP = str(input("CEP do Paciente apenas dígitos: "))
    CEP = correcao_erro_CEP(CEP)

    RUA = str(input("Rua do Paciente: "))

    BAIRRO = str(input("Bairro do Paciente: "))

    COMPLEMENTO = str(input("Complemento do endereço do Paciente: "))

    NUMERO = str(input("NÚMERO do Paciente: "))

    TELEFONE1 = str(input("Primeiro número de telefone do Paciente: "))
    TELEFONE1 = correcao_erro_tel(TELEFONE1)

    if TELEFONE1 in '':
        TELEFONE1 = None
    else : TELEFONE1 = converte_tel(TELEFONE1)

    TELEFONE2 = str(input("Segundo número de telefone do Paciente: "))
    TELEFONE2 = correcao_erro_tel(TELEFONE2)
    

    if TELEFONE2 in '':
        TELEFONE2 = None   
    else: TELEFONE2 = converte_tel(TELEFONE2)


    temp = CLASSESMEDICO.PACIENTE(CPF_PAC,NOME, SEXO, DATA_DE_NASC, CNPJ_CONV, CEP, RUA, BAIRRO, COMPLEMENTO, NUMERO, TELEFONE1, TELEFONE2)
    
    cursor = conn.cursor()

    try :
        cursor.execute(f"""
        INSERT INTO PACIENTE(CPF_PAC, NOME, SEXO, DATA_DE_NASC, CPF, CEP, RUA, BAIRRO, COMPLEMENTO, NUMERO, TELEFONE1, TELEFONE2) 
        VALUES ({temp.CPF_PAC},{temp.NOME},{temp.SEXO},'{temp.DATA_DE_NASC[2]}-{temp.DATA_DE_NASC[1]}-{temp.DATA_DE_NASC[0]}',{temp.CNPJ_CONV},{temp.CEP},
        '{temp.RUA}', '{temp.BAIRRO}','{temp.COMPLEMENTO}',{temp.NUMERO},{temp.TELEFONE1},{temp.TELEFONE2})
        """)

        mensagem()
        conn.commit()
        
    except Exception as Err:
        print(Err + '\n')

    cursor.close
    
def cadastrar_medicamento(conn):
    
    COD_MEDICAMENTO = (input("Código do medicamento: "))
    COD_MEDICAMENTO = correcao_erro_COD_MED(COD_MEDICAMENTO, conn)

    QTD_DISPONIVEL = (input("Quantidade disponível do medicamento: "))

    NOME = input("Nome do medicamento: ")

    TIPO = input("Tipo do medicamento: ")


    temp = CLASSESMEDICO.medicamento(COD_MEDICAMENTO, QTD_DISPONIVEL, NOME, TIPO)
    
    cursor = conn.cursor()
    
    try: 
        cursor.execute(f"""
            INSERT INTO MEDICAMENTO ( COD_MEDICAMENTO, QTD_DISPONIVEL, NOME, TIPO) 
            VALUES ({temp.COD_MEDICAMENTO},{temp.QTD_DISPONIVEL},'{temp.NOME}','{temp.TIPO}')
        """)
        conn.commit() 
        mensagem()
        
    except Exception as Error:
        print(Error)

       
    cursor.close()
    
def marcar_consulta(conn):
    cursor1 = conn.cursor()
    cursor1.execute("""
    SELECT NOME, CPF_pac from PACIENTE""")
    
    pacientes = cursor1.fetchall()
    print("lista de pacientes: ")
    for paciente in pacientes:
        print(f"""
        Nome do Paciente:{paciente[0]}
        CPF do Paciente: {paciente[1]}
        """)
    cursor1.close()

    CPF_PAC = str(input("CPF do paciente apenas dígitos: "))
    CPF_PAC = pegar_CPF_pac(CPF_PAC)

    COD_CONS = int(input("Código da consulta do Paciente: "))

    cursor2 = conn.cursor()
    cursor2.execute("""
    SELECT NOME, id_funcionario from FUNCIONARIO where cargo = 'Medico(a)' """)
    
    Medicos = cursor2.fetchall()
    print("lista de Medicos: ")
    for medico in Medicos:
        print(f"""
        Nome do Paciente:{medico[0]}
        ID do Paciente: {medico[1]}
        """)
    cursor2.close()

    ID_MED = int(input("ID do médico que atendeu o paciente: "))
    ID_MED = correcao_erro_id_med(ID_MED)

    DIA = (input("Dia da consulta: "))
    MES = (input("Mês da Consulta: "))
    ANO =(input("Ano da Consulta: "))
    
    DATA = [DIA, MES, ANO ]
    DATA = correcao_erro_data(DATA)

    HORA = [int(input("Hora da consulta: ")), int(input("Minuto da consulta: ")), int(input("Segundo da consulta: "))]

    TIPO_RECEITA = str(input("Receita do Paciente: "))

    temp = CLASSESMEDICO.CONSULTA(CPF_PAC,COD_CONS, ID_MED, DATA, HORA, TIPO_RECEITA)
    
    cursor = conn.cursor()

    try :
        cursor.execute(f"""
        INSERT INTO CONSULTA(CPF_PAC, COD_CONS, ID_MED, DATA, CPF, TIPO_RECEITA) 
        VALUES ({temp.CPF_PAC},{temp.COD_CONS},{temp.ID_MED},'{temp.DATA[2]}-{temp.DATA[1]}-{temp.DATA[0]}',
        '{temp.HORA[0]}-{temp.HORA[1]}-{temp.HORA[2]}',{temp.TIPO_RECEITA})
        """)

        print("Consulta Registrada")
        conn.commit()
        
    except Exception as Err:
        print(Err)

    cursor.close()
    
def marcar_exame(conn):
    cursor1 = conn.cursor()
    cursor1.execute("""
    SELECT NOME, CPF_pac from PACIENTE""")
    
    pacientes = cursor1.fetchall()
    print("lista de pacientes: ")
    for paciente in pacientes:
        print(f"""
        Nome do Paciente:{paciente[0]}
        CPF do Paciente: {paciente[1]}
        """)
    cursor1.close()

    CPF_PAC = str(input("CPF do paciente, apenas dígitos: "))
    CPF_PAC = pegar_CPF_pac(CPF_PAC)

    COD_CONS = str(input("Código da consulta do Paciente: "))

    TIPO = str(input("Tipo de exame do paciente: "))

    DIA = (input("Dia da Exame: "))
    MES = (input("Mês da Exame: "))
    ANO = (input("Ano da Exame: "))
    
    DATA = [DIA, MES, ANO ]
    DATA = correcao_erro_data(DATA)

    HORA = [int(input("Hora da consulta: ")), int(input("Minuto da consulta: "))]

    DIAGNOSTICO = str(input("Diagnóstico do paciente: "))

    temp = CLASSESMEDICO.CONSULTA(CPF_PAC,COD_CONS, TIPO, DATA, HORA, DIAGNOSTICO)
    
    cursor = conn.cursor()

    try :
        cursor.execute(f"""
        INSERT INTO EXAME(CPF_PAC, COD_CONS, TIPO, DATA, HORA, DIAGNOSTICO) 
        VALUES ({temp.CPF_PAC},{temp.COD_CONS},{temp.TIPO},'{temp.DATA[2]}-{temp.DATA[1]}-{temp.DATA[0]}',
        '{temp.HORA[0]}:{temp.HORA[1]}',{temp.DIAGNOSTICO})
        """)

        print("Exame Registrado")
        conn.commit()

    except Exception as Err:
        print(Err)

    cursor.close
