from DAO import CLASSESMEDICO
import psycopg2

# ID_FUNCIONARIO:int,CARGO:str,SEXO:str,DATA_DE_NASC,
# CPF:str, SALARIO:float,NOME:str,
# CRE:str,CRM:str,MEDIA_Av,TELEFONE1:str,TELEFONE2:str

#Formatação de dados:
def mensagem():
    print("Inserido com sucesso!")

def converte_tel(TEL):
    Tele = f"'({TEL[0:2]}) {TEL[2:7]}-{TEL[7:]}'"

    return Tele

def converte_cpf(CPFF):
    CPFF = f"'{CPFF[0:3]}.{CPFF[3:6]}.{CPFF[6:9]}-{CPFF[9:]}'"

    return CPFF

def converte_cnpj(CNPJ):
    CNPJ = f"'{CNPJ[0:2]}.{CNPJ[2:5]}.{CNPJ[5:8]}/{CNPJ[8:12]}-{CNPJ[12:]}'"

    return CNPJ

def escolha_cargo():
    escolha = ''
    while escolha not in('1','2','3', 'Enfermeiro(a)', 'Médico(a)'):
        escolha = input('Qual das opções se encaixa o funcionario?: ')
    
        if escolha in ('1', 'Enfermeiro(a)'):
            escolha = 'Enfermeiro(a)'
        elif escolha in ('2', 'Médico(a)'):
            escolha = 'Médico(a)'
        elif escolha in ('3'):
            escolha = input("Qual cargo do funcionario: ")

        else: print("Opção invalida!")
    return escolha

def ver_planos_conv(cnpj_conv, conn):
    cursor_2 = conn.cursor()

    cursor_2.execute(f"""
    Select Nome from plano_ofertado
    where cnpj_conv = '{cnpj_conv}'
    """)
    
    planos = cursor_2.fetchall()

    planos = [planos[i][0] for i in range(len(planos))]

    cursor_2.close()
    return planos  

#Correção de Erro das Inserções
def correcao_erro_id(ID:str, conn):
    cursor1 = conn.cursor()    
    cursor1.execute(""" SELECT ID_Funcionario from funcionario
    """)
    IDS = cursor1.fetchall()
    cursor1.close()
    
    IDSL = []

    for id in IDS:
        IDSL.append(f'{id[0]}')

    print(ID)
    print(IDSL)

    while not ID.isnumeric() or (ID  in IDSL):
        if not ID.isnumeric():
                print("Valor inválido! ID precisa ser inteiro")
                ID = input("ID DO FUNCIONÁRIO: ")
        elif ID in IDSL:
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
        elif ID not in IDS:
                print("Valor inválido! ID não existe na lista de médicos")
                ID = input("ID DO MÉDICO: ")
    return ID

def correcao_erro_CEP(CEPP):
    while len(CEPP) != 8 or CEPP.isalpha():
        print("ERRO NA INSERÇÃO DE DADOS, tente novamente: ")
        CEPP = input("CEP do Paciente apenas dígitos: ")

    CEPP = f"'{CEPP[0:6]}-{CEPP[6:]}'"
    return CEPP 

def correcao_erro_tel(tel:str):
    if tel == '':
        return tel

    while len(tel) != 11 or not tel.isnumeric():
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
        print("!!Valor inválido! ano tem 4 dígitos e estar no intervado de 1925 e 2022!!")
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
    lista_cod = []
    
    for cod in CODS:
        lista_cod.append(cod[0])
        
    cursor1.close()
    print(lista_cod)

    while not COD_MEDICAMENTO.isnumeric() or int(COD_MEDICAMENTO)  in lista_cod:
        if not COD_MEDICAMENTO.isnumeric():
                print("Valor inválido! código do medicamento precisar ser inteiro")
                COD_MEDICAMENTO = input("COD DO MEDICAMENTO: ")
        elif int(COD_MEDICAMENTO) in lista_cod:
                print("Valor inválido! código do medicamento já existe na lista de medicamentos")
                COD_MEDICAMENTO = input("COD DO MEDICAMENTO: ")
    return COD_MEDICAMENTO

def correcao_erro_COD_CONS(CPF_PAC, conn):

    
    
    cursor1 = conn.cursor()    
    cursor1.execute(f""" SELECT COD_CONS from CONSULTA WHERE CPF_PAC = {CPF_PAC}
    """)
    CODS = cursor1.fetchall()
    cursor1.close()
    list_cods = []

    print("lista de consultas do paciente: ")
    for cod in CODS:
        print(f"""
        Código da consulta:{cod[0]}\n
        """)
        list_cods.append(cod[0])
    
    COD_CONS = str(input("Código da consulta do Paciente: "))

    while not COD_CONS.isnumeric() or (int(COD_CONS) not in list_cods):
        if not COD_CONS.isnumeric():
                print("Valor inválido! código da consulta precisa ser inteiro")
                COD_CONS = input("COD DA CONSULTA: ")
        elif int(COD_CONS) not in list_cods:
                print("Valor inválido! código da consulta deve ser das consultas do paciente escolhido")
                COD_CONS = input("COD DA CONSULTA: ")
    return COD_CONS

def correcao_chave_COD_CONS(COD_CONS, conn):
    cursor1 = conn.cursor()    
    cursor1.execute(""" SELECT COD_CONS from consulta
    """)
    conS = cursor1.fetchall()
    cursor1.close()
    
    conL = []

    for id in conS:
        conL.append(f'{id[0]}')


    while not COD_CONS.isnumeric() or (COD_CONS  in conL):
        if not COD_CONS.isnumeric():
                print("Valor inválido! COD precisa ser inteiro")
                COD_CONS = input("CODIGO DA CONSULTA: ")
        elif COD_CONS in conL:
                print("Valor inválido! Codigo da consulta já esta cadastrada")
                COD_CONS = input("CODIGO DA CONSULTA: ")
    return COD_CONS


def correcao_referencia_CNPJ(conn):
    cursor1 = conn.cursor()

    cursor1.execute("SELECT DISTINCT cnpj_conv from plano_ofertado")
    
    cnpjs = cursor1.fetchall()
    
    for i in range(len(cnpjs)):
        print(f"[{i}] CNPJ: {cnpjs[i][0]}, Planos Oferecidos: {ver_planos_conv(cnpjs[i][0], conn)}")
    
    escolhido = int(input("Selecione o CNPJ relacionado ao plano que possui: "))

    while(escolhido >= len(cnpjs) or escolhido < 0):
        print("\nERRO: O índice escolhido não está relacionado com nenhum dos convênios disponíveis, tente novamente.")
        escolhido = int(input("Selecione o número relacionado ao convênio que possui: "))
    
    escolhido = cnpjs[escolhido][0]
    
    return f"'{escolhido}'"


def correcao_chave_pac(conn):
    cursor = conn.cursor()

    cursor.execute('SELECT cpf_pac from paciente')

    Lista = cursor.fetchall()

    pacientes = []

    for paciente in Lista:
        pacientes.append(paciente[0])

    CPF_PAC = ''
    while True:
    
        CPF_PAC = str(input("CPF do paciente, apenas dígitos: "))  
        CPF_PAC = correcao_erro_CPF(CPF_PAC)
        CPF_PAC = converte_cpf(CPF_PAC)

        if CPF_PAC in pacientes:
            print("!!! CPF já está cadastrado! !!!")
        else: return CPF_PAC



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

    CARGO = escolha_cargo()

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

    DATA_DE_NASC = input("Data de nascimento do Funcionário (Formato DD/MM/AAAA): ").split('/')
    DATA_DE_NASC = correcao_erro_data(DATA_DE_NASC)

    CPF = str(input("CPF do funcionário: "))
    CPF = correcao_erro_CPF(CPF)

    CPF = converte_cpf(CPF)

    SALARIO = (input("Salario do funcionário: "))
    SALARIO = float(correcao_erro_salario(SALARIO))

    NOME = str(input("Nome do funcionário: "))

    CRE = str(input("CRE do funcionário: "))

    if CRE == '':
        CRE = 'Null'
    else: CRE = f"'{CRE}'"


    CRM = str(input("CRM do funcionário: "))
    if CRM == '':
        CRM = 'Null'
    else: CRM = f"'{CRM}'"

    MEDIA_Av = (input("Media de avaliação do funcionário: "))
    MEDIA_Av = float(correcao_erro_Media(MEDIA_Av))

    TELEFONE1 = str(input("Primeiro número de telefone do funcionário: "))
    TELEFONE1 = correcao_erro_tel(TELEFONE1)
    if TELEFONE1 == '':
        TELEFONE1 = 'Null'

    else: TELEFONE1 = converte_tel(TELEFONE1)

    TELEFONE2 = str(input("Segundo número de telefone do funcionário: "))
    TELEFONE2 = correcao_erro_tel(TELEFONE2)
    if TELEFONE2 == '':
        TELEFONE2 = 'Null'
    else: TELEFONE1 = converte_tel(TELEFONE2)
    
    temp = CLASSESMEDICO.funcionario(ID_FUNCIONARIO,CARGO, SEXO, DATA_DE_NASC, CPF, SALARIO, NOME, CRE, CRM, MEDIA_Av, TELEFONE1, TELEFONE2)
    
    cursor = conn.cursor()

    try :
        cursor.execute(f"""
        INSERT INTO FUNCIONARIO(ID_FUNCIONARIO, CARGO, SEXO, DATA_DE_NASC, CPF, SALARIO, NOME, CRE, CRM, MEDIA_Av, TELEFONE1, TELEFONE2) 
        VALUES ({temp.ID_FUNCIONARIO},'{temp.CARGO}','{temp.SEXO}','{temp.DATA_DE_NASC[2]}-{temp.DATA_DE_NASC[1]}-{temp.DATA_DE_NASC[0]}','{temp.CPF}',{temp.SALARIO},
        '{temp.NOME}', {temp.CRE},{temp.CRM},{temp.MEDIA_Av},{temp.TELEFONE1},{temp.TELEFONE2})
        """)

        mensagem()
        conn.commit()

    except Exception as Err:
        print(Err)
    
    cursor.close


def cadastrar_paciente(conn):

    #CPF_PAC, SEXO, NOME, DATA_DE_NASC, CNPJ_CONV, CEP, RUA, BAIRRO, COMPLEMENTO, NUMERO, TELEFONE1, TELEFONE2

    CPF_PAC = correcao_chave_pac(conn)

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
    
    DATA_DE_NASC = input("Data de nascimento do Paciente (Formato DD/MM/AAAA): ").split('/')
    DATA_DE_NASC = correcao_erro_data(DATA_DE_NASC)

    CNPJ_CONV = correcao_referencia_CNPJ(conn)

    #CNPJ_CONV = converte_cnpj(CNPJ_CONV)

    CEP = str(input("CEP do Paciente apenas dígitos: "))
    CEP = correcao_erro_CEP(CEP)

    RUA = str(input("Rua do Paciente: "))

    BAIRRO = str(input("Bairro do Paciente: "))

    COMPLEMENTO = str(input("Complemento do endereço do Paciente: "))

    NUMERO = str(input("Número do Paciente: "))

    TELEFONE1 = str(input("Primeiro número de telefone do Paciente: "))
    TELEFONE1 = correcao_erro_tel(TELEFONE1)

    if TELEFONE1 in '':
        TELEFONE1 = 'Null'
    else : TELEFONE1 = converte_tel(TELEFONE1)

    TELEFONE2 = str(input("Segundo número de telefone do Paciente: "))
    TELEFONE2 = correcao_erro_tel(TELEFONE2)
    
    if TELEFONE2 in '':
        TELEFONE2 = 'Null'   
    else: TELEFONE2 = converte_tel(TELEFONE2)

    temp = CLASSESMEDICO.paciente(CPF_PAC, SEXO, NOME, DATA_DE_NASC, CNPJ_CONV, CEP, RUA, BAIRRO, COMPLEMENTO, NUMERO, TELEFONE1, TELEFONE2)
    
    cursor = conn.cursor()

    try :
        cursor.execute(f"""
        INSERT INTO PACIENTE(CPF_PAC, NOME, SEXO, DATA_DE_NASC, CNPJ_CONV, CEP, RUA, BAIRRO, COMPLEMENTO, NUMERO, TELEFONE1, TELEFONE2) 
        VALUES ({temp.CPF_PAC},'{temp.NOME}','{temp.SEXO}','{temp.DATA_DE_NASC[2]}-{temp.DATA_DE_NASC[1]}-{temp.DATA_DE_NASC[0]}',{temp.CNPJ_CONV},{temp.CEP},
        '{temp.RUA}', '{temp.BAIRRO}','{temp.COMPLEMENTO}',{temp.NUMERO},{temp.TELEFONE1},{temp.TELEFONE2})
        """)

        mensagem()
        conn.commit()
        
    except Exception as Err:
        print(Err)

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
    CPF_PAC = pegar_CPF_pac(conn, CPF_PAC)

    CPF_PAC = converte_cpf(CPF_PAC)

    COD_CONS = input("Qual O Codigo da consulta?: ")
    COD_CONS = correcao_chave_COD_CONS(COD_CONS,conn)

    cursor2 = conn.cursor()
    cursor2.execute("""
    SELECT NOME, id_funcionario from FUNCIONARIO where cargo = 'Médico(a)' """)
    
    Medicos = cursor2.fetchall()
    print("lista de Medicos: ")
    for medico in Medicos:
        print(f"""
        Nome do Medico:{medico[0]}
        ID do Medico: {medico[1]}
        """)
    cursor2.close()

    ID_MED = str(input("\nID do médico que atendeu o paciente: "))
    ID_MED = correcao_erro_id_med(ID_MED,conn)

    #DIA = (input("Dia da consulta: "))
    #MES = (input("Mês da Consulta: "))
    #ANO =(input("Ano da Consulta: "))
    
    #DATA = [DIA, MES, ANO ]
    DATA = input("Data da consulta (Formato DD/MM/AAAA): ").split('/')
    DATA = correcao_erro_data(DATA)

    HORA = [(input("Hora da consulta: ")), (input("Minuto da consulta: "))]

    TIPO_RECEITA = str(input("Tipo de Receita do Paciente: "))

    temp = CLASSESMEDICO.consulta(COD_CONS, CPF_PAC, ID_MED, DATA, HORA, TIPO_RECEITA)
    
    cursor = conn.cursor()

    try :
        cursor.execute(f"""
        INSERT INTO CONSULTA(CPF_PAC, COD_CONS, ID_MED, DATA, HORA ,TIPO_RECEITA) 
        VALUES ({temp.CPF_PAC},{temp.COD_CONS},{temp.ID_MED},'{temp.DATA[2]}-{temp.DATA[1]}-{temp.DATA[0]}',
        '{temp.HORA[0]}:{temp.HORA[1]}','{temp.TIPO_RECEITA}')
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
    CPF_PAC = pegar_CPF_pac(conn,CPF_PAC)

    CPF_PAC = converte_cpf(CPF_PAC)

    COD_CONS = correcao_erro_COD_CONS(CPF_PAC, conn)

    TIPO = str(input("Tipo de exame do paciente: "))

    #DIA = (input("Dia da Exame: "))
    #MES = (input("Mês da Exame: "))
    #ANO = (input("Ano da Exame: "))
    
    #DATA = [DIA, MES, ANO ]
    DATA = input("Data do Exame (Formato DD/MM/AAAA): ").split('/')
    DATA = correcao_erro_data(DATA)

    HORA = [(input("Hora do exame: ")), (input("Minuto do exame: "))]

    DIAGNOSTICO = str(input("Diagnóstico do paciente: "))

    temp = CLASSESMEDICO.exame(COD_CONS, TIPO, DATA, HORA,CPF_PAC, DIAGNOSTICO)
    
    cursor = conn.cursor()

    try :
        cursor.execute(f"""
        INSERT INTO EXAME(CPF_PAC, COD_CONS, TIPO, DATA, HORA, DIAGNOSTICO) 
        VALUES ({temp.CPF_PAC},{temp.COD_CONS},'{temp.TIPO}','{temp.DATA[2]}-{temp.DATA[1]}-{temp.DATA[0]}',
        '{temp.HORA[0]}:{temp.HORA[1]}','{temp.DIAGNOSTICO}')
        """)

        print("Exame Registrado")
        conn.commit()

    except Exception as Err:
        print(Err)

    cursor.close()



def adicionar_receita(conn):
    pass
def alocar_enfermeira(conn):
    pass