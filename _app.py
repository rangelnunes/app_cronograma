from database import Database

MENU_DE_OPCOES = """ #### MENU ####

1) Inserir um novo semestre letivo
2) Consultar semestres cadastrados
3) Excluir um semestre
4) Alterar um semestre
5) Sair.

Digite a opção desejada: """

def cadastra_semestre():
    ano = input("Digite o ano: ")
    semestre = input("Digite o semestre (1 ou 2): ")
    bd.insere_semestre(ano, semestre)

def consulta_semestres():
    semestres = bd.consulta_semestres()
    for semestre in semestres:
        print(f'Semestre: {semestre[0]}.{semestre[1]}')
        print('-' * 20 + "\n")
def deleta_semestre():
    ano = input('Digite o ano a ser excluido: ')
    semestre = input('Digite o semestre: ')

    bd.deleta_semestre(int(ano), semestre)

def alterar_semestre():
    ano = input('Digite o ano que deseja alterar: ')
    semestre = input('Digite o semestre que deseja alterar: ')
    novo_ano = input('Digite o novo valor para o ano: ')
    novo_semestre = input('Digite o novo valor para o semestre: ')

    bd.update_semestre(novo_ano, novo_semestre, ano, semestre)


while (opcao := input(MENU_DE_OPCOES)) != '5':
    try:
        print(f"opcao: {opcao}")

        bd = Database()
        bd.create_tables()

        if opcao == '1':
            cadastra_semestre()
        elif opcao == '2':
            consulta_semestres()
        elif opcao == '3':
            deleta_semestre()
        elif opcao == '4':
            alterar_semestre()
    except KeyError:
        print("Opção inválida! Tente novamente.")







