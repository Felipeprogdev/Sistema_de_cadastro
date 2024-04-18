import sqlite3
import primeira_tela


def criar_tabela():
    banco = sqlite3.connect('dados_das_pessoas.db')
    cursor = banco.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='dados'")
    if cursor.fetchone() is None:
        cursor.execute("CREATE TABLE dados ("
                       "id INTEGER PRIMARY KEY,"
                       " nome TEXT,"
                       " email TEXT,"
                       " data DATE )")

    banco.commit()

    banco.close()
    primeira_tela.tela1()


if __name__ == '__main__':
    criar_tabela()
