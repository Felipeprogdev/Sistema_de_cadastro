from tkinter import *
from tkinter import ttk
from banco_de_dados import Banco
from datetime import datetime
from main import primeira_tela


def create_label(frame, text, x, y, width, height, bg='#4c8fde'):
    label = Label(frame, text=text, bg=bg)
    label.place(x=x, y=y, width=width, height=height)
    return label


def botao_de_fechar(janela_1, frame):

    # Adicionando o botão ao frame
    botao_fechar = Button(frame,
                          text="X",
                          bg='red',
                          command=janela_1.destroy)

    botao_fechar.pack(side="right",
                      anchor="nw")  # Posiciona o botão no canto superior direito do frame


def botao_de_minimizar(janela_1, frame):
    # Adicionando o botão ao frame
    botao_minimizar = Button(frame,
                             text="-",
                             command=janela_1.iconify)

    botao_minimizar.pack(side="right",
                         anchor="nw")  # Posiciona o botão no canto superior direito do


def botao_de_voltar(janela_1, frame):
    def abrir_outra_janela():
        janela_1.destroy()
        primeira_tela.tela1()

    # Adicionando o botão ao frame
    botao_voltar = Button(frame,
                          text="Voltar",  # Texto que remete a voltar
                          command=lambda: abrir_outra_janela())  # Ação ao clicar

    botao_voltar.pack(side="left",  # Posiciona o botão no canto superior esquerdo
                      anchor="nw")


# numero é a variavel que define que o programa deve chamar o banco para carregar
# inicio é a pagina que o banco ira procurar e multiplicar por 21 para colocar na tela
# resetable é para limpar a tabela
def tabela(janela_1, largura_janela, altura_janela, numero=0, inicio=0, resetabela=False,
           _id=None, _nome=None, _email=None, _data=None, colocar_dados=True):

    # Definindo a posição e o tamanho do frame com base no tamanho da janela
    x = largura_janela * 0.2  # 10% da largura da janela
    y = altura_janela * 0.2  # 10% da altura da janela
    largura_frame = largura_janela * 0.6  # 60% da largura da janela
    altura_frame = altura_janela * 0.6  # 60% da altura da janela

    frame_tabela = Frame(janela_1,
                         bg='#4c8fde',
                         borderwidth=1)
    frame_tabela.place(x=x,
                       y=y,
                       width=largura_frame,
                       height=altura_frame)

    tabel = ttk.Treeview(frame_tabela,
                         columns=('id', 'nome', 'email', 'data de nascimento'),
                         show='headings',
                         )

    tabel.column('id', minwidth=10, width=50)
    tabel.column('nome', minwidth=10, width=150)
    tabel.column('email', minwidth=10, width=150)
    tabel.column('data de nascimento', minwidth=10, width=100)
    tabel.heading('id', text='ID')
    tabel.heading('nome', text='Nome')
    tabel.heading('email', text='Email')
    tabel.heading('data de nascimento', text='Data de Nascimento')

    if resetabela == True:
        tabel.delete()

    if numero == 1:
        # Cria uma nova instância da classe Banco
        classe = Banco()
        # Adiciona os dados de uma nova pessoa ao banco de dados
        classe.carregar_dados(tabel, inicio, variavel_id=_id, variavel_nome=_nome,
                              variavel_email=_email, variavel_data=_data)

        if colocar_dados == True:
            tabel.pack(fill=BOTH, expand=1)  # Adiciona a tabela ao frame

    # Obtém uma lista de todos os itens na tabela
    itens = tabel.get_children()

    # Se a tabela não estiver vazia
    if itens:

        # Obtém o último item na tabela
        ultimo_item = itens[-1]

        # Obtém o ID do último item
        ultimo_id = tabel.item(ultimo_item, 'values')[0]

        # Abre o arquivo no modo de escrita ('w')
        with open("variaveis.txt", "w") as arquivo:
            # Escreve cada variável em uma linha diferente
            arquivo.write((_id if _id is not None else '') + "\n")
            arquivo.write((_nome if _nome is not None else '') + "\n")
            arquivo.write((_email if _email is not None else '') + "\n")
            arquivo.write((str(_data) if _data is not None else '') + '\n')
            arquivo.write(str(ultimo_id))  # Escreve o último ID da tabela

            # Fecha o arquivo
            arquivo.close()


def botao_de_pesquisar(frame, largura_frame, altura_frame, largura_botao, altura_botao, pesquisar):
    # Calculando as coordenadas x e y para centralizar o botão no frame
    x_botao = (largura_frame - largura_botao) / 2
    y_botao = (altura_frame - altura_botao) / 1.5

    # Criando um botão
    botao_de_pesquisa = Button(frame,
                               text="Pesquisar",
                               bg='#ffffca',
                               command=pesquisar)
    # Posicionando e dimensionando o botão dentro do frame
    botao_de_pesquisa.place(x=x_botao,
                            y=y_botao,
                            width=largura_botao,
                            height=altura_botao)


def botoes_caixas_de_texto_de_pesquisa(janela_1, largura_janela, altura_janela):
    # Definindo a largura e a altura do frame
    largura_frame = largura_janela * 1  # 100% da largura da janela
    altura_frame = altura_janela * 0.2  # 10% da altura da janela

    # Definindo a posição do frame
    x = (largura_janela - largura_frame) / 2  # Centralizado na largura
    y = 0  # No topo da janela

    frame = Frame(janela_1, bg='#4c8fde',
                  borderwidth=1)

    frame.place(x=x,
                y=y,
                width=largura_frame,
                height=altura_frame)

    def adicionar_barra(event):
        # Verifica se o caractere digitado é um número, uma barra ou backspace e formata tudo
        if event.char.isdigit() or event.char == '/' or event.char == '\x08':
            # Pega valor digitado
            entrada = data.get()

            # Verifica se já foram digitados 10 caracteres ou se foi digitado um backspace
            if len(entrada) < 10 or event.char == '\x08':
                # Se for um backspace não adicione a /

                if event.char != '\x08':
                    if len(entrada) == 1 and int(entrada[0]) == 3 and int(event.char) >= 2:
                        # Limpa a caixa de texto
                        data.delete(0, END)
                        # Insere '0', o antigo índice 0, '/', '0' e o caractere digitado
                        data.insert(END, '0')
                        data.insert(END, entrada[0])
                        data.insert(END, '/')
                        data.insert(END, '0')
                        data.insert(END, event.char)
                        data.insert(END, '/')
                        return 'break'

                    if (
                            len(entrada) == 0 and event.char.isdigit() and int(event.char) >= 4 and int
                            (event.char) <= 9 or len(entrada) == 3 and event.char.isdigit() and int
                            (event.char) >= 2 and int(event.char) <= 9
                    ):
                        data.insert(END, '0')
                        data.insert(END, event.char)
                        data.insert(END, '/')
                        return 'break'

                    if len(entrada) == 1 or len(entrada) == 4:
                        '''Insere uma barra após os dois primeiros caracteres ou após os cinco 
                        primeiros, exceto se o caractere for backspace'''
                        data.insert(END, event.char)
                        data.insert(END, '/')
                        return 'break'

            else:
                # Se o caractere não for um número, uma barra ou backspace, não o insere na caixa de texto
                return 'break'

        else:
            # Se o caractere não for um número, uma barra ou backspace, não o insere na caixa de texto
            return 'break'

    def pesquisar():
        id_digitado = caixa_id.get() if caixa_id.get() else None
        nome_digitado = caixa_nome.get().capitalize() if caixa_nome.get() else None
        email_digitado = caixa_email.get() if caixa_email.get() else None
        # Verifica se data_digitada_str não é None
        if data.get() and len(data.get()) == 10:
            # Converte a string para um objeto de data
            data_digitada = datetime.strptime(data.get(), '%d/%m/%Y').date()
        else:
            data_digitada = None

        tabela(janela_1, largura_janela, altura_janela, numero=1, resetabela=True,
               _id=id_digitado, _nome=nome_digitado, _email=email_digitado, _data=data_digitada)

        # O resto do seu código aqui...

        # Atualiza o texto do label 'pagina'
        pagina.config(text="1")

    botao_de_fechar(janela_1, frame)

    botao_de_minimizar(janela_1, frame)

    botao_de_voltar(janela_1, frame)

    # Definindo a largura e a altura do botão como uma porcentagem da largura e altura do frame
    largura_botao = largura_frame * 0.1  # 20% da largura do frame
    altura_botao = altura_frame * 0.2  # 20% da altura do frame

    botao_de_pesquisar(frame, largura_frame, altura_frame, largura_botao, altura_botao, pesquisar)

    # Definindo a largura e a altura do botão como uma porcentagem da largura e altura do frame
    largura_nome = largura_frame * 0.1  # 20% da largura do frame
    altura_nome = altura_frame * 0.15  # 20% da altura do frame

    # Calculando as coordenadas x e y para centralizar o botão no frame
    x_id = (largura_frame - largura_botao) / 3.6
    y_id = (altura_frame - altura_botao) / 3

    # Cria a caixa de texto
    caixa_id = Entry(frame)
    # Caixa de texto do nome
    caixa_id.place(x=x_id,
                   y=y_id,
                   width=largura_nome,
                   height=altura_nome
                   )

    # Calculando as coordenadas x e y para centralizar o botão no frame
    x_label_id = (largura_frame - largura_botao) / 3.58
    y_label_id = (altura_frame - altura_botao) / 10

    create_label(frame, 'Id:', x_label_id, y_label_id, largura_nome, altura_nome)

    # Calculando as coordenadas x e y para centralizar o botão no frame
    x_nome = (largura_frame - largura_botao) / 2.3
    y_nome = (altura_frame - altura_botao) / 3

    # Cria a caixa de texto
    caixa_nome = Entry(frame)
    # Caixa de texto do nome
    caixa_nome.place(x=x_nome,
               y=y_nome,
               width=largura_nome,
               height=altura_nome)

    # Calculando as coordenadas x e y para centralizar o botão no frame
    x_label_nome = (largura_frame - largura_botao) / 2.29
    y_label_nome = (altura_frame - altura_botao) / 10

    create_label(frame, 'Nome:', x_label_nome, y_label_nome, largura_nome, altura_nome)

    # Calculando as coordenadas x e y para centralizar o botão no frame
    x_email = largura_frame - (largura_frame - largura_botao) / 1.9
    y_email = (altura_frame - altura_botao) / 3

    # Cria a caixa de texto do email
    caixa_email = Entry(frame)
    # Caixa de texto do email
    caixa_email.place(x=x_email,
                      y=y_email,
                      width=largura_nome,
                      height=altura_nome
                      )

    # Calculando as coordenadas x e y para centralizar o botão no frame
    x_label_email = largura_frame - (largura_frame - largura_botao) / 1.9
    y_label_email = (altura_frame - altura_botao) / 10

    create_label(frame, 'email:', x_label_email, y_label_email, largura_nome, altura_nome)

    # Calculando as coordenadas x e y para centralizar o botão no frame
    x_data = largura_frame - (largura_frame - largura_botao) / 2.7
    y_data = (altura_frame - altura_botao) / 3

    # Cria a caixa de texto
    data = Entry(frame)
    # Caixa de texto do nome
    data.place(x=x_data,
               y=y_data,
               width=largura_nome,
               height=altura_nome)
    data.bind('<Key>', adicionar_barra)

    # Calculando as coordenadas x e y para centralizar o botão no frame
    x_label_data = largura_frame - (largura_frame - largura_botao) / 2.7
    y_label_data = (altura_frame - altura_botao) / 10

    create_label(frame, 'Data:', x_label_data, y_label_data, largura_nome, altura_nome)


def cor_de_fundo_e_icone(janela_1):
    # Cor de fundo
    janela_1['bg'] = '#4c8fde'
    # Adicionar icone
    janela_1.iconbitmap('icone.ico')


def tamanho_da_janela(janela_1):
    # Faz a janela abrir em tela cheia
    janela_1.attributes('-fullscreen', True)
    # Desativa a capacidade de redimensionar a janela
    janela_1.resizable(False, False)


def paginacao_da_tabela(janela_1, largura_janela, altura_janela):
    # Definindo a posição e o tamanho do frame com base no tamanho da janela
    x = largura_janela * 0.2  # 10% da largura da janela
    y = altura_janela * 0.8  # 80% da altura da janela
    largura_frame = largura_janela * 0.6  # 60% da largura da janela
    altura_frame = altura_janela * 0.1  # 10% da altura da janela

    frame_tabela = Frame(janela_1,
                         bg='#4c8fde',
                         borderwidth=1)
    frame_tabela.place(x=x,
                       y=y,
                       width=largura_frame,
                       height=altura_frame)

    # Adiciona um label ao frame
    global pagina
    pagina = Label(frame_tabela, text="1", bg='#4c8fde')
    pagina.place(relx=0.5, rely=0.5, anchor='center')




    def proxima():
        # Abre o arquivo no modo de leitura ('r')
        with open("variaveis.txt", "r") as arquivo:
            # Lê cada linha e remove o caractere de nova linha no final
            id_digitado = arquivo.readline().strip()
            nome_digitado = arquivo.readline().strip()
            email_digitado = arquivo.readline().strip()
            data_digitada = arquivo.readline().strip()
            id_final_da_tabela = int(arquivo.readline().strip())
            arquivo.close()

        # Se a linha estiver vazia, atribui None à variável
        id_digitado = None if id_digitado == '' else id_digitado
        if id_digitado is not None:
            id_digitado = int(id_digitado)
        nome_digitado = None if nome_digitado == '' else nome_digitado
        email_digitado = None if email_digitado == '' else email_digitado
        data_digitada = None if data_digitada == '' else data_digitada
        # Se a linha estiver vazia, atribui None à variável
        data_digitada = None if data_digitada == '' else data_digitada
        # Se data_digitada não é None, converte para datetime
        if data_digitada is not None:
            data_digitada = datetime.strptime(data_digitada, '%Y-%m-%d')
            data_digitada = data_digitada.strftime('%Y-%m-%d')

        classe = Banco()
        ultimo_id = classe.obter_ultimo_id(nome=nome_digitado, email=email_digitado, data=data_digitada)

        if id_digitado != None:
            pass

        else:
            if int(id_final_da_tabela) == ultimo_id:
                pass

            else:
                numero_pagina = int(pagina.cget('text'))

                tabela(janela_1, largura_janela, altura_janela, numero=1, inicio=numero_pagina, resetabela=True,
                       _id=id_digitado, _nome=nome_digitado, _email=email_digitado, _data=data_digitada)


                numero_pagina += 1

                # Altera o texto do label
                pagina.config(text=str(numero_pagina))

    def anterior():
        # Abre o arquivo no modo de leitura ('r')
        with open("variaveis.txt", "r") as arquivo:
            # Lê cada linha e remove o caractere de nova linha no final
            id_digitado = arquivo.readline().strip()
            nome_digitado = arquivo.readline().strip()
            email_digitado = arquivo.readline().strip()
            data_digitada = arquivo.readline().strip()
            arquivo.close()

        # Se a linha estiver vazia, atribui None à variável
        id_digitado = None if id_digitado == '' else id_digitado
        if id_digitado is not None:
            id_digitado = int(id_digitado)
        nome_digitado = None if nome_digitado == '' else nome_digitado
        email_digitado = None if email_digitado == '' else email_digitado
        data_digitada = None if data_digitada == '' else data_digitada
        # Se a linha estiver vazia, atribui None à variável
        data_digitada = None if data_digitada == '' else data_digitada
        # Se data_digitada não é None, converte para datetime
        if data_digitada is not None:
            data_digitada = datetime.strptime(data_digitada, '%Y-%m-%d')
            data_digitada = data_digitada.strftime('%Y-%m-%d')

        if int(pagina.cget('text')) == 1:
            pass

        else:
            numero_pagina = int(pagina.cget('text'))

            numero_pagina -= 2

            tabela(janela_1, largura_janela, altura_janela, numero=1, inicio=numero_pagina, resetabela=True,
                   _id=id_digitado, _nome=nome_digitado, _email=email_digitado, _data=data_digitada
                   )



            numero_pagina += 1
            pagina_str = numero_pagina
            # Altera o texto do label
            pagina.config(text=pagina_str)

    # Adiciona um botão à esquerda do label
    botao_esquerda = Button(frame_tabela, text="<", bg='#ffffca', command=anterior)
    botao_esquerda.place(relx=0.4, rely=0.5, anchor='center')

    # Adiciona um botão à direita do label
    botao_direita = Button(frame_tabela, text=">", bg='#ffffca', command=proxima)
    botao_direita.place(relx=0.6, rely=0.5, anchor='center')


def deletar_dados_pelo_id(janela_1, largura_janela, altura_janela):
    # Definindo a posição e o tamanho do frame com base no tamanho da janela
    x = 0  # Inicia no canto esquerdo
    y = (altura_janela - (altura_janela * 0.4)) / 2  # Centraliza na vertical
    largura_frame = largura_janela * 0.19  # 30% da largura da janela
    altura_frame = altura_janela * 0.4  # 40% da altura da janela

    frame_deletar = Frame(janela_1,
                         bg='#4c8fde',
                         borderwidth=1)
    frame_deletar.place(x=x,
                       y=y,
                       width=largura_frame,
                       height=altura_frame)

    def deletar():
        id_digitado = id_entry.get()

        if id_digitado == None or id_digitado == str:
            return

        classe = Banco()
        classe.deletar_dados(id_digitado)
        tabela(janela_1, largura_janela, altura_janela, numero=1, resetabela=False)

    Label(frame_deletar,
         text="Deletar dados",
         bg='#4c8fde').place(relx=0.5, rely=0, anchor='n')

    Label(frame_deletar,
          text="Digite seu Id",
          bg='#4c8fde').place(relx=0.5, rely=0.2, anchor='n')  # Ajuste a posição vertical conforme necessário

    # Entry para o ID
    id_entry = Entry(frame_deletar)
    id_entry.place(relx=0.5, rely=0.4, anchor='n')  # Ajuste a posição vertical conforme necessário

    Button(frame_deletar,
           text="Deletar",
           bg='#ffffca',
           command=deletar).place(relx=0.5, rely=0.6, anchor='n')  # Ajuste a posição vertical conforme necessário


def editar_dados(janela_1, largura_janela, altura_janela):
    def adicionar_barra(event):
        # Verifica se o caractere digitado é um número, uma barra ou backspace e formata tudo
        if event.char.isdigit() or event.char == '/' or event.char == '\x08':
            # Pega valor digitado
            entrada = data_text_box.get()

            # Verifica se já foram digitados 10 caracteres ou se foi digitado um backspace
            if len(entrada) < 10 or event.char == '\x08':
                # Se for um backspace não adicione a /

                if event.char != '\x08':
                    if len(entrada) == 1 and int(entrada[0]) == 3 and int(event.char) >= 2:
                        # Limpa a caixa de texto
                        data_text_box.delete(0, END)
                        # Insere '0', o antigo índice 0, '/', '0' e o caractere digitado
                        data_text_box.insert(END, '0')
                        data_text_box.insert(END, entrada[0])
                        data_text_box.insert(END, '/')
                        data_text_box.insert(END, '0')
                        data_text_box.insert(END, event.char)
                        data_text_box.insert(END, '/')
                        return 'break'

                    if (
                            len(entrada) == 0 and event.char.isdigit() and int(event.char) >= 4 and int
                            (event.char) <= 9 or len(entrada) == 3 and event.char.isdigit() and int
                            (event.char) >= 2 and int(event.char) <= 9
                    ):
                        data_text_box.insert(END, '0')
                        data_text_box.insert(END, event.char)
                        data_text_box.insert(END, '/')
                        return 'break'

                    if len(entrada) == 1 or len(entrada) == 4:
                        '''Insere uma barra após os dois primeiros caracteres ou após os cinco 
                        primeiros, exceto se o caractere for backspace'''
                        data_text_box.insert(END, event.char)
                        data_text_box.insert(END, '/')
                        return 'break'

            else:
                # Se o caractere não for um número, uma barra ou backspace, não o insere na caixa de texto
                return 'break'

        else:
            # Se o caractere não for um número, uma barra ou backspace, não o insere na caixa de texto
            return 'break'

    # Definindo a posição e o tamanho do frame com base no tamanho da janela
    largura_frame = largura_janela * 0.19  # 19% da largura da janela
    altura_frame = altura_janela * 0.6  # 40% da altura da janela
    x = largura_janela - largura_frame  # Subtrai a largura do frame da largura da janela
    y = (altura_janela - altura_frame) / 2  # Centraliza na vertical

    frame_editar = Frame(janela_1,
                         bg='#4c8fde',
                         borderwidth=1)
    frame_editar.place(x=x,
                       y=y,
                       width=largura_frame,
                       height=altura_frame)

    # Adiciona os labels, caixas de texto e botão ao frame
    Label(frame_editar,
          text="Editar dados",
          bg='#4c8fde').place(relx=0.5, rely=0.1, anchor='center')

    Label(frame_editar,
          text="Digite seu Id",
          bg='#4c8fde').place(relx=0.5, rely=0.2, anchor='center')

    id_text_box = Entry(frame_editar)
    id_text_box.place(relx=0.5, rely=0.3, anchor='center')

    Label(frame_editar,
          text="Digite seu nome",
          bg='#4c8fde').place(relx=0.5, rely=0.4, anchor='center')

    nome_text_box = Entry(frame_editar)
    nome_text_box.place(relx=0.5, rely=0.5, anchor='center')

    Label(frame_editar,
          text="Digite seu email",
          bg='#4c8fde').place(relx=0.5, rely=0.6, anchor='center')

    email_text_box = Entry(frame_editar)
    email_text_box.place(relx=0.5, rely=0.7, anchor='center')

    Label(frame_editar,
          text="Digite a data de nascimento",
          bg='#4c8fde').place(relx=0.5, rely=0.8, anchor='center')

    data_text_box = Entry(frame_editar)
    data_text_box.place(relx=0.5, rely=0.9, anchor='center')
    data_text_box.bind('<Key>', adicionar_barra)

    def editar():
        id_digitado = int(id_text_box.get())
        nome_digitado = nome_text_box.get().capitalize() if nome_text_box.get().strip() != "" else None
        email_digitado = email_text_box.get() if email_text_box.get().strip() != "" else None
        data_digitada = data_text_box.get() if data_text_box.get().strip() != "" else None
        if data_digitada:
            # Converte a string para um objeto datetime
            data_digitada = datetime.strptime(data_digitada, '%d/%m/%Y')
            # Quando for exibir ou usar, formate para string apenas com a data
            data_digitada = data_digitada.strftime('%Y-%m-%d')

        classe = Banco()
        classe.editar_dados(id_digitado, nome_digitado, email_digitado, data_digitada)

        tabela(janela_1, largura_janela, altura_janela, numero=1, resetabela=False)

    Button(frame_editar,
           text="Editar",
           bg='#ffffca',
           command=editar).place(relx=0.5, rely=1.0, anchor='s')


def tela2():
    # Criando uma instância da classe Tk
    janela_1 = Tk()
    # Titulo da janela
    janela_1.title("Sistema de cadastro")

    # Chama fução que cria a cor de fundo e coloca o icone
    cor_de_fundo_e_icone(janela_1)
    tamanho_da_janela(janela_1)

    # Obtendo a largura e a altura da janela
    largura_janela = janela_1.winfo_screenwidth()
    altura_janela = janela_1.winfo_screenheight()

    tabela(janela_1, largura_janela, altura_janela, numero=1)

    # Isso é para pegar os dados que irão passar na paginação, exemplo, a pessoa pesquisou nome x
    # a paginação ira se basear nesse nome x e ira paginar com ele
    botoes_caixas_de_texto_de_pesquisa(janela_1, largura_janela, altura_janela)

    paginacao_da_tabela(janela_1, largura_janela, altura_janela)

    deletar_dados_pelo_id(janela_1, largura_janela, altura_janela)

    editar_dados(janela_1, largura_janela, altura_janela)

    # Iniciando o loop principal da interface
    janela_1.mainloop()


if __name__ == '__main__':
    tela2()
