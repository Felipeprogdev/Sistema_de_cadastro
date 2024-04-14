import sqlite3
from datetime import datetime


class Banco:
    # Cria arquivo
    banco = sqlite3.connect('dados_das_pessoas.db')
    # Para utilizar os comandos sql
    cursor = banco.cursor()


    def carregar_dados(self, inicio=0, variavel_id=None, variavel_nome=None, variavel_email=None, variavel_data=None):
        # Inicia a consulta SQL
        consulta_sql = "SELECT id, nome, email, data FROM dados WHERE 1=1"

        # Adiciona condições à consulta SQL com base nos dados fornecidos
        if variavel_id:
            consulta_sql += f" AND id = {variavel_id}"
        if variavel_nome:
            consulta_sql += f" AND nome = '{variavel_nome}'"
        if variavel_email:
            consulta_sql += f" AND email = '{variavel_email}'"
        if variavel_data:
            consulta_sql += f" AND data = '{variavel_data}'"

        # Execute a consulta SELECT para recuperar os dados
        self.cursor.execute(consulta_sql)

        # Recupere todos os resultados
        resultados = self.cursor.fetchall()

        max_rows = 21

        inicio = inicio * 21

        fim = inicio + max_rows

        # Limita o número de linhas retornadas
        resultados = resultados[inicio:fim]


        # Processa cada linha individualmente
        for linha in resultados:
            id_linha, nome, email, data = linha
            # Converta a string da data para um objeto datetime
            data_obj = datetime.strptime(data, '%Y-%m-%d')
            # Formate o objeto datetime para o formato desejado
            data_formatada = data_obj.strftime('%d/%m/%Y')
            # Insere cada linha na tabela
            print('', 'end', id_linha, nome, email, data_formatada)