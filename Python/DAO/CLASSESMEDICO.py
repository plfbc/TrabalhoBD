
class funcionario():

    def __init__(self,ID_FUNCIONARIO:int,CARGO:str,SEXO:str,DATA_DE_NASC,
    CPF:str, SALARIO:float,NOME:str,CRE:str,CRM:str,MEDIA_Av:float,TELEFONE1:str,TELEFONE2:str):

        self.ID_FUNCIONARIO = ID_FUNCIONARIO
        self.CARGO = CARGO
        self.SEXO = SEXO
        self.DATA_DE_NASC = DATA_DE_NASC
        self.CPF = CPF 
        self.SALARIO = SALARIO
        self.NOME = NOME
        self.CRE = CRE
        self.CRM = CRM
        self.MEDIA_Av = MEDIA_Av
        self.TELEFONE1 = TELEFONE1
        self.TELEFONE2 = TELEFONE2

    def __str__(self) -> str:
        pass

class paciente():
    def __init__(self,CPF_PAC,SEXO,NOME, DATA_DE_NASC,CNPJ_CONV,CEP,RUA,BAIRRO,COMPLEMENTO,NUMERO,TELEFONE1,TELEFONE2):
        self.CPF_PAC = CPF_PAC 
        self.SEXO = SEXO 
        self.NOME = NOME 
        self.DATA_DE_NASC = DATA_DE_NASC 
        self.CNPJ_CONV = CNPJ_CONV 
        self.CEP = CEP
        self.RUA = RUA
        self.BAIRRO = BAIRRO
        self.COMPLEMENTO = COMPLEMENTO
        self.NUMERO = NUMERO 
        self.TELEFONE1 = TELEFONE1 
        self.TELEFONE2 = TELEFONE2
  
class exame():
    def __init__(self,COD_CONS, TIPO,DATA,HORA,CPF_PAC,DIAGNOSTICO):
        self.COD_CONS = COD_CONS
        self.TIPO = TIPO
        self.DATA = DATA
        self.HORA = HORA
        self.CPF_PAC = CPF_PAC
        self.DIAGNOSTICO = DIAGNOSTICO

class consulta():
    def init(self,COD_CONS,CPF_PAC,ID_MED,DATA,HORA,TIPO_RECEITA):

        self.COD_CONS = COD_CONS
        self.CPF_PAC = CPF_PAC
        self.ID_MED = ID_MED
        self.DATA = DATA
        self.HORA = HORA
        self.TIPO_RECEITA = TIPO_RECEITA 

class medicamento():
    def __init__(self, COD_MEDICAMENTO:int, QTD_DISPONIVEL:int,NOME:str,TIPO:str):
        self.COD_MEDICAMENTO = COD_MEDICAMENTO        
        self.QTD_DISPONIVEL = QTD_DISPONIVEL
        self.NOME = NOME
        self.TIPO = TIPO

class convenio():
    def __init__(self,CNPJ_CONV:int, NOME:str, TELEFONE:int):
        self.CNPJ_CONV = CNPJ_CONV
        self.NOME = NOME
        self.TELEFONE = TELEFONE 

class plano_ofertado():
    def __init__(self,CNPJ_CONV, NOME):
        self.CNPJ_CONV = CNPJ_CONV 
        self.NOME = NOME 

class prescreve():
    def __init__(self, COD_MED, COD_CONS, DESCRICAO, UNIDADE, DOSAGEM):
        self.COD_MED = COD_MED
        self.COD_CONS = COD_CONS
        self.DESCRICAO = DESCRICAO
        self.UNIDADE = UNIDADE
        self.DOSAGEM = DOSAGEM

class atende_em():
    def __init__(self, COD_EX, ID_ENFER, DATA, HORA):
        self.COD_EX = COD_EX
        self.ID_ENFER = ID_ENFER
        self.DATA = DATA
        self.HORA = HORA    