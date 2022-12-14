import psycopg2
from Conection import conection
from Menus import Menus_1
from Menus import Menus_2

def Menu_1(conn):

    menu_1 = True
    while menu_1:
        
        print("""
        ---------------------------BEM VINDO AO 4US----------------------------
        |                             OLA ADMIN                               |
        |                                                                     |
        |                                                                     |
        |                   Qual dado deseja cadastrar no Banco?              |
        |                                                                     |
        |      [1] Cadastrar Dados de Funcionario                             | 
        |      [2] Cadastrar Dados de Paciente                                |
        |      [3] Cadastrar Dados de Consulta                                |
        |      [4] Cadastrar Dados de Medicamentos                            |
        |      [5] Cadastrar Dados de Exames                                  |
        |      [6] Voltar ao Menu Principal                                   |
        |                                                                     |
        |                                                                     |
        |                                                                     |
        -----------------------------------------------------------------------
        """)

        escolha = ' '
        
        while escolha not in ["1",'2','3','4','5','6']:
            escolha = input("Sua escolha: ").strip()

        escolha = int(escolha)
    
        match escolha:
            case 1:
                Menus_1.cadastrar_funcionario(conn)
            case 2:
                Menus_1.cadastrar_paciente(conn)
            case 3:
                Menus_1.marcar_consulta(conn)
            case 4:
                Menus_1.cadastrar_medicamento(conn)
            case 5:
                Menus_1.marcar_exame(conn)
            case 6:
                return

def Menu_2(conn):

    menu_2 = True
    while menu_2:

        print("""
        ---------------------------------- 4US--------------------------------
        |                               **OLA ADMIN**                         |
        |                                                                     |
        |                                                                     |
        |                   Escolha Uma Funcao para executar:                 |
        |                                                                     |
        |      [1] Verificar Consulta Cadastrada                              | 
        |      [2] Verificar Pacientes Cadastrados                            |
        |      [3] Verificar Medicamento Cadastrados                          |
        |      [4] Verificar Funcionarios Cadastrados                         |
        |      [5] Voltar ao Menu Principal                                   |
        |                                                                     |
        -----------------------------------------------------------------------
        """)
        escolha = ' '
        while escolha not in ["1",'2','3','4','5']:
            escolha = input("Sua escolha: ").strip()

        escolha = int(escolha)
            
        match escolha:
            case 1:
                Menus_2.verif_consulta(conn)
                pass

            case 2:
                Menus_2.verif_paciente(conn)
                pass

            case 3:
                Menus_2.verif_medicamento(conn)
                pass

            case 4:
                Menus_2.verif_funcionario(conn)
                pass

            case 5:
                return
                    

def Menu_Principal(conn):
    
    menu_p = True
    while menu_p:

        print("""
        ---------------------------BEM VINDO AO 4US----------------------------
        |                               OLA ADMIN                             |
        |                                                                     |
        |                                                                     |
        |                   Escolha Uma Funcao para executar:                 |
        |                                                                     |
        |      [1] Cadastrar Dados no Sistema                                 | 
        |      [2] Visualizar Funcoes do Sistema                              |
        |      [3] Sair do Sistema                                            |
        |                                                                     |
        |                                                                     |
        |                                                                     |
        -----------------------------------------------------------------------
        """)

        escolha = ''
        while escolha not in ['1','2','3']:
            escolha = input("Sua escolha: ").strip()
        escolha = int(escolha)
        
        match escolha:
            case 1:
                Menu_1(conn)
            case 2:
                Menu_2(conn)
            case 3:
                return
       
conn = conection()
Menu_Principal(conn)