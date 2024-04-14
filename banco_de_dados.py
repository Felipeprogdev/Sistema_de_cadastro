import sqlite3
from datetime import datetime


class Banco:
    # Cria arquivo
    banco = sqlite3.connect('dados_das_pessoas.db')
    # Para utilizar os comandos sql
    cursor = banco.cursor()


    def carregar_dados(self, tabel, inicio=0, variavel_id=None, variavel_nome=None, variavel_email=None, variavel_data=None):
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
            tabel.insert('', 'end', values=(id_linha, nome, email, data_formatada))


    def adicionar_dados(self,  __nome: str, __email: str, __data: datetime):
        # Converte o objeto datetime para uma string no formato 'YYYY-mm-dd'
        data_final_str = __data.strftime('%Y-%m-%d')

        # Inserir dados no banco
        self.cursor.execute("INSERT INTO dados (nome, email, data) VALUES (?, ?, ?)", (__nome, __email, data_final_str))
        self.banco.commit()

    def editar_dados(self, id_alvo, novo_nome=None, novo_email=None, nova_data=None):
        # Se novo_nome não for None, atualize o nome
        if novo_nome is not None:
            self.cursor.execute(""" UPDATE dados SET nome = ? WHERE id = ? """, (novo_nome, id_alvo))

        # Se novo_email não for None, atualize o email
        if novo_email is not None:
            self.cursor.execute(""" UPDATE dados SET email = ? WHERE id = ? """, (novo_email, id_alvo))

        # Se nova_data não for None, atualize a data
        if nova_data is not None:
            self.cursor.execute(""" UPDATE dados SET data = ? WHERE id = ? """, (nova_data, id_alvo))

        # Commit as mudanças no banco de dados
        self.banco.commit()

    def deletar_dados(self, __id):
        try:
            # Deletar dados no banco
            self.cursor.execute("DELETE from dados WHERE id = ?", (__id,))
            self.banco.commit()
        except Exception as e:
            print(f"Erro ao deletar dados: {e}")
            # Aqui você pode adicionar qualquer código para lidar com o erro

    def obter_ultimo_id(self, nome=None, email=None, data=None):
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
        self.cursor.execute(consulta_sql, valores)

        # Recupera o resultado
        resultado = self.cursor.fetchone()

        # O resultado é uma tupla, então pegamos o primeiro elemento
        ultimo_id = resultado[0] if resultado else None

        return ultimo_id


if __name__ == '__main__':
    pass
