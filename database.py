import psycopg2

class Database():

    CRIA_TABELA_SEMESTRES = """
        create table if not exists semestres (
            ano int,
            semestre int,
            check (semestre in (1,2)),
            primary key (ano, semestre)
        );
    """
    INSERE_SEMESTRE = "insert into semestres values (%s, %s);"
    CONSULTA_SEMESTRES = "select * from semestres order by ano, semestre;"
    DELETA_SEMESTRE = "delete from semestres where ano = %s and semestre = %s;"
    UPDATE_SEMESTRE = "update semestres set ano = %s, semestre = %s where (ano = %s and semestre = %s);"

    def __init__(self, host='localhost', database='app_cronograma',user='postgres',password='pgsql'):

        self.conexao = None
        try:
            self.conexao = psycopg2.connect(
                host=host,
                database=database,
                user=user,
                password=password
            )
            print('Conexao estabelicida com sucesso!!')
        except Exception as erro:
            print(f'Erro ao conectar com o banco de dados: {erro}')

    def deleta_semestre(self, ano, semestre):
        try:
            with self.conexao:
                with self.conexao.cursor as cursor:
                    cursor.execute(self.DELETA_SEMESTRE, (ano, int(semestre)))
                    print('Semestre excluido com sucesso!!')
        except Exception as erro:
            print(f'Erro ao excluir o semestre: {erro}')

    def create_tables(self):
        try:
            with self.conexao:
                with self.conexao.cursor() as cursor:
                    cursor.execute(self.CRIA_TABELA_SEMESTRES)
                    print('Tabela semestre criada com sucesso!')
        except Exception as erro:
            print(f'Erro ao criar a tabela semestre: {erro}')

    def insere_semestre(self, ano, semestre):
        try:
            with self.conexao:
                with self.conexao.cursor() as cursor:
                    cursor.execute(self.INSERE_SEMESTRE, (int(ano), int(semestre)))
                    print('Semestre cadastrado com sucesso!')
        except Exception as erro:
            print(f'Erro ao cadastrar o semestre: {erro}')

    def consulta_semestres(self):
        try:
            with self.conexao:
                with self.conexao.cursor() as cursor:
                    cursor.execute(self.CONSULTA_SEMESTRES)
                    return cursor.fetchall()
        except Exception as erro:
            print(f'Erro ao consultar o banco de dados: {erro}')

    def update_semestre(self, novo_ano, novo_semestre, ano, semestre):
        try:
            with self.conexao:
                with self.conexao.cursor() as cursor:
                    cursor.execute(self.UPDATE_SEMESTRE, (novo_ano, novo_semestre, ano, semestre))
                    print('Semestre alterado com sucesso!')
        except Exception as erro:
            print(f'Erro ao alterar o semestre: {erro}')





