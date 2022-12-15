import psycopg2
from Conection import conection
from Menus import Menus_1
from Menus import Menus_2
from Menus import Menus_3

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
        |      [0] Voltar ao Menu Principal                                   |
        |                                                                     |
        |                                                                     |
        |                                                                     |
        -----------------------------------------------------------------------
        """)

        escolha = ' '
        
        while escolha not in ["0", "1",'2','3','4','5']:
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
            case 0:
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
        |      [3] Verificar Funcionarios Cadastrados                         |
        |      [4] Verificar Medicamento Cadastrados                          |
        |      [0] Voltar ao Menu Principal                                   |
        |                                                                     |
        -----------------------------------------------------------------------
        """)
        escolha = ' '
        while escolha not in ["0", "1",'2','3','4']:
            escolha = input("Sua escolha: ").strip()

        escolha = int(escolha)
            
        match escolha:
            case 1:
                Menus_2.verif_consulta(conn)

            case 2:
                Menus_2.verif_paciente(conn)
                
            case 3:
                Menus_2.verif_funcionario(conn)

            case 4:
                Menus_2.verif_medicamento(conn)

            case 0:
                return

def Menu_3(conn):
    
    menu_3 = True
    
    while(menu_3):
        print("""
        ---------------------------BEM VINDO AO 4US----------------------------
        |                             OLA ADMIN                               |
        |                                                                     |
        |                                                                     |
        |                   Qual dado deseja excluir do Banco?                |
        |                                                                     |
        |      [1] Excluir Dados de Funcionario                               | 
        |      [2] Excluir Dados de Paciente                                  |
        |      [3] Excluir Dados de Consulta                                  |
        |      [4] Excluir Dados de Medicamentos                              |
        |      [0] Voltar ao Menu Principal                                   |
        |                                                                     |
        |                                                                     |
        |                                                                     |
        -----------------------------------------------------------------------
        """)
        
        escolha = ' '
        while escolha not in ["0", "1",'2','3','4','5']:
            escolha = input("Sua escolha: ").strip()

        escolha = int(escolha)
    
        match escolha:
            case 1:
                Menus_3.excluir_funcionario(conn)
            case 2:
                Menus_3.excluir_paciente(conn)
            case 3:
                Menus_3.excluir_consulta(conn)
            case 4:
                Menus_3.excluir_medicamento(conn)
            case 0:
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
        |      [3] Excluir Dados do Sistema                                   |
        |      [0] Sair do Sistema                                            |
        |                                                                     |
        |                                                                     |
        |                                                                     |
        -----------------------------------------------------------------------
        """)

        escolha = ''
        while escolha not in ['1','2','3', "0"]:
            escolha = input("Sua escolha: ").strip()
        escolha = int(escolha)
        
        match escolha:
            case 1:
                Menu_1(conn)
            case 2:
                Menu_2(conn)
            case 3:
                Menu_3(conn)
            case 0:
                return
       
conn = conection()
Menu_Principal(conn)