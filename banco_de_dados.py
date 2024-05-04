import sqlite3
from datetime import datetime


class Banco:
    def __init__(self):
        self.db_name = 'dados_das_pessoas.db'

    def carregar_dados(self, tabel, inicio=0, variavel_id=None, variavel_nome=None,
                       variavel_email=None, variavel_data=None):
        banco = sqlite3.connect(self.db_name)
        cursor = banco.cursor()

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
        cursor.execute(consulta_sql)

        # Recupere todos os resultados
        resultados = cursor.fetchall()

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
            tabel.insert('', 'end', values=(id_linha, nome, email, data_formatada))

        banco.close()

    def adicionar_dados(self,  __nome: str, __email: str, __data: datetime):
        banco = sqlite3.connect(self.db_name)
        cursor = banco.cursor()

        # Converte o objeto datetime para uma string no formato 'YYYY-mm-dd'
        data_final_str = __data.strftime('%Y-%m-%d')

        # Inserir dados no banco
        cursor.execute("INSERT INTO dados (nome, email, data) VALUES (?, ?, ?)", (__nome, __email, data_final_str))
        banco.commit()
        banco.close()

    def editar_dados(self, id_alvo, novo_nome=None, novo_email=None, nova_data=None):
        banco = sqlite3.connect(self.db_name)
        cursor = banco.cursor()

        # Se novo_nome não for None, atualize o nome
        if novo_nome is not None:
            cursor.execute(""" UPDATE dados SET nome = ? WHERE id = ? """, (novo_nome, id_alvo))

        # Se novo_email não for None, atualize o email
        if novo_email is not None:
            cursor.execute(""" UPDATE dados SET email = ? WHERE id = ? """, (novo_email, id_alvo))

        # Se nova_data não for None, atualize a data
        if nova_data is not None:
            cursor.execute(""" UPDATE dados SET data = ? WHERE id = ? """, (nova_data, id_alvo))

        # Commit as mudanças no banco de dados
        banco.commit()
        banco.close()

    def deletar_dados(self, __id):
        banco = sqlite3.connect(self.db_name)
        cursor = banco.cursor()

        try:
            # Deletar dados no banco
            cursor.execute("DELETE from dados WHERE id = ?", (__id,))
            banco.commit()
            banco.close()
        except sqlite3.Error:
            banco.close()
            pass

    # Obtem o ultimo id para paginação
    def obter_ultimo_id(self, nome=None, email=None, data=None):
        banco = sqlite3.connect(self.db_name)
        cursor = banco.cursor()

        # Inicia a consulta SQL
        consulta_sql = "SELECT id FROM dados WHERE 1=1"

        # Adiciona condições à consulta SQL com base nos dados fornecidos
        if nome is not None:
            consulta_sql += f" AND nome = ?"
        if email is not None:
            consulta_sql += f" AND email = ?"
        if data is not None:
            consulta_sql += f" AND data = ?"

        # Adiciona a ordenação e limita o resultado a 1
        consulta_sql += " ORDER BY id DESC LIMIT 1"

        # Cria uma lista com os valores que não são None
        valores = [valor for valor in (nome, email, data) if valor is not None]

        # Executa a consulta SQL
        cursor.execute(consulta_sql, valores)

        # Recupera o resultado
        resultado = cursor.fetchone()

        # O resultado é uma tupla, então pegamos o primeiro elemento
        ultimo_id = resultado[0] if resultado else None

        banco.close()

        return ultimo_id


if __name__ == '__main__':
    pass
