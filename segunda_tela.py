from tkinter import *
from tkinter import ttk
from banco_de_dados import Banco
from datetime import datetime
from main import primeira_tela


def formatar_nome():
    nome_na_caixa_de_texto = caixa_nome.get().capitalize()
    if caixa_nome.get() == '':
        nome_na_caixa_de_texto = None
    return nome_na_caixa_de_texto


def formatar_email():
    email_na_caixa_de_texto = caixa_email.get().lower()
    if caixa_email.get() == '':
        email_na_caixa_de_texto = None
    return email_na_caixa_de_texto


def formatar_data():
    data_na_caixa_de_texto = data.get()
    if data.get() == '':
        data_na_caixa_de_texto = None
    else:
        data_na_caixa_de_texto = data_na_caixa_de_texto.replace('/', '-')
        a = data_na_caixa_de_texto[0:2]
        b = data_na_caixa_de_texto[6:10]
        teste = b + data_na_caixa_de_texto[2:6] + a
        data_na_caixa_de_texto = teste

    return data_na_caixa_de_texto


def create_label(frame, text, x, y, width, height, bg='#4c8fde'):
    label = Label(frame, text=text, bg=bg)
    label.place(x=x, y=y, width=width, height=height)
    return label


def botao_de_fechar(janela_1, frame):
    botao_fechar = Button(frame,
                          text="X",
                          bg='red',
                          command=janela_1.destroy)

    botao_fechar.pack(side="right",
                      anchor="nw")  # Posiciona o botão no canto superior direito do frame


def botao_de_minimizar(janela_1, frame):
    botao_minimizar = Button(frame,
                             text="-",
                             command=janela_1.iconify)

    botao_minimizar.pack(side="right",
                         anchor="nw")  # Posiciona o botão no canto superior direito do frame


def abrir_outra_janela(janela_1):
    janela_1.destroy()
    primeira_tela.tela1()


def botao_de_voltar(janela_1, frame):
    botao_voltar = Button(frame,
                          text="Voltar",
                          command=lambda: abrir_outra_janela(janela_1))  # Passando janela_1 como argumento
    botao_voltar.pack(side="left", anchor="nw")


def pesquisar(janela_1, largura_janela, altura_janela):
    tabela(janela_1, largura_janela, altura_janela, numero=1, resetb=True)
    # Atualiza o texto do label 'pagina'
    pagina.config(text="1")


def botao_de_pesquisar(frame, janela_1, largura_frame,
                       altura_frame, largura_botao,
                       altura_botao, largura_janela, altura_janela):
    # Calculando as coordenadas x e y para centralizar o botão no frame
    x_botao = (largura_frame - largura_botao) / 2
    y_botao = (altura_frame - altura_botao) / 1.5

    # Criando um botão
    botao_de_pesquisa = Button(frame,
                               text="Pesquisar",
                               bg='#ffffca',
                               command=lambda: pesquisar(janela_1, largura_janela, altura_janela))
    # Posicionando e dimensionando o botão dentro do frame
    botao_de_pesquisa.place(x=x_botao,
                            y=y_botao,
                            width=largura_botao,
                            height=altura_botao)


def frame_de_pesquisa(janela_1, largura_janela, altura_janela):
    largura_frame = largura_janela * 1  # 100% da largura da janela
    altura_frame = altura_janela * 0.2  # 20% da altura da janela

    x = (largura_janela - largura_frame) / 2  # Centralizado na largura
    y = 0  # No topo da janela

    frame = Frame(janela_1, bg='#4c8fde',
                  borderwidth=1)

    frame.place(x=x,
                y=y,
                width=largura_frame,
                height=altura_frame)

    botao_de_fechar(janela_1, frame)

    botao_de_minimizar(janela_1, frame)

    botao_de_voltar(janela_1, frame)

    # Definindo a largura e a altura do botão como uma porcentagem da largura e altura do frame
    largura_botao = largura_frame * 0.1  # 10% da largura do frame
    altura_botao = altura_frame * 0.2  # 20% da altura do frame

    botao_de_pesquisar(frame, janela_1, largura_frame,
                       altura_frame, largura_botao, altura_botao,
                       largura_janela, altura_janela)

    # Definindo a largura e a altura do label como uma porcentagem da largura e altura do frame
    largura_label = largura_frame * 0.1  # 1% da largura do frame
    altura_label = altura_frame * 0.15  # 10.5% da altura do frame

    pesquisa_id(frame, largura_label, altura_label, largura_frame, altura_frame, largura_botao, altura_botao)

    x_label_id = (largura_frame - largura_botao) / 3.58
    y_label_id = (altura_frame - altura_botao) / 10

    create_label(frame, 'Id:', x_label_id, y_label_id, largura_label, altura_label)

    pesquisa_nome(frame, largura_label, altura_label, largura_frame, altura_frame, largura_botao, altura_botao)

    x_label_nome = (largura_frame - largura_botao) / 2.29
    y_label_nome = (altura_frame - altura_botao) / 10

    create_label(frame, 'Nome:', x_label_nome, y_label_nome, largura_label, altura_label)

    pesquisa_email(frame, largura_label, altura_label, largura_frame, altura_frame, largura_botao, altura_botao)

    x_label_email = largura_frame - (largura_frame - largura_botao) / 1.9
    y_label_email = (altura_frame - altura_botao) / 10

    create_label(frame, 'email:', x_label_email, y_label_email, largura_label, altura_label)

    pesquisa_data(frame, largura_label, altura_label, largura_frame, altura_frame, largura_botao, altura_botao)

    x_label_data = largura_frame - (largura_frame - largura_botao) / 2.7
    y_label_data = (altura_frame - altura_botao) / 10

    create_label(frame, 'Data:', x_label_data, y_label_data, largura_label, altura_label)


# numero é a variavel que define que o programa deve chamar o banco para carregar
# inicio é a pagina que o banco ira procurar e multiplicar por 21 para colocar na tela
# resetb é para limpar a tabela
def tabela(janela_1, largura_janela, altura_janela, numero=0, inicio=0, resetb=False):

    # Definindo a posição e o tamanho do frame com base no tamanho da janela
    x = largura_janela * 0.2  # 20% da largura da janela
    y = altura_janela * 0.2  # 20% da altura da janela
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

    if resetb:
        tabel.delete()

    if caixa_id.get() == '':
        id_na_caixa_de_texto = None
    else:
        id_na_caixa_de_texto = int(caixa_id.get())

    nome_na_caixa_de_texto = formatar_nome()

    email_na_caixa_de_texto = formatar_email()

    data_na_caixa_de_texto = formatar_data()

    if numero == 1:
        # Cria uma nova instância da classe Banco
        classe = Banco()
        # Adiciona os dados de uma nova pessoa ao banco de dados
        classe.carregar_dados(tabel, inicio=inicio, variavel_id=id_na_caixa_de_texto,
                              variavel_nome=nome_na_caixa_de_texto,
                              variavel_email=email_na_caixa_de_texto,
                              variavel_data=data_na_caixa_de_texto)
        tabel.pack(fill=BOTH, expand=1)  # Adiciona a tabela ao frame

    # Obtém uma lista de todos os itens na tabela
    itens = tabel.get_children()

    # Se a tabela não estiver vazia
    if itens:

        # Obtém o último item na tabela
        ultimo_item = itens[-1]

        # Obtém o ID do último item
        ultimo_id = tabel.item(ultimo_item, 'values')[0]

        global ultimo_id_da_tabela
        ultimo_id_da_tabela = ultimo_id


def adicionar_barra(event, data_acessada):
    if event.keysym in ['Left', 'Right', 'Up', 'Down']:
        return

    # Verifica se o caractere digitado é um número, uma barra ou backspace
    elif event.char.isdigit() or event.char == '/' or event.char == '\x08':
        # Pega valor digitado
        entrada = data_acessada.get()

        # Verifica se já foram digitados 10 caracteres ou se foi digitado um backspace
        if len(entrada) < 10 or event.char == '\x08':
            # Se for um backspace não adicione a /

            if event.char != '\x08':
                if len(entrada) == 4 and int(event.char) >= 3:
                    # Limpa a caixa de texto
                    data_acessada.delete(0, END)
                    data_acessada.insert(END, entrada[0])
                    data_acessada.insert(END, entrada[1])
                    data_acessada.insert(END, entrada[2])
                    data_acessada.insert(END, entrada[3])
                    return 'break'

                if len(entrada) == 1 and int(entrada[0]) == 3 and int(event.char) >= 2:
                    # Limpa a caixa de texto
                    data_acessada.delete(0, END)
                    # Insere '0', o antigo índice 0, '/', '0' e o caractere digitado
                    data_acessada.insert(END, '0')
                    data_acessada.insert(END, entrada[0])
                    data_acessada.insert(END, '/')
                    data_acessada.insert(END, '0')
                    data_acessada.insert(END, event.char)
                    data_acessada.insert(END, '/')
                    return 'break'

                if (
                        len(entrada) == 0 and event.char.isdigit() and int(event.char) >= 4 and int
                        (event.char) <= 9 or len(entrada) == 3 and event.char.isdigit() and int
                        (event.char) >= 2 and int(event.char) <= 9
                ):
                    data_acessada.insert(END, '0')
                    data_acessada.insert(END, event.char)
                    data_acessada.insert(END, '/')
                    return 'break'

                if len(entrada) == 1 or len(entrada) == 4:
                    '''Insere uma barra após os dois primeiros caracteres ou após os cinco 
                    primeiros, exceto se o caractere for backspace'''
                    data_acessada.insert(END, event.char)
                    data_acessada.insert(END, '/')
                    return 'break'

        else:
            # Se o caractere não for um número, uma barra ou backspace, não o insere na caixa de texto
            return 'break'

    else:
        # Se o caractere não for um número, uma barra, backspace ou uma tecla de seta, não o insere na caixa de texto
        return 'break'


def formatar_id(event):
    value = event.char
    keysym = event.keysym
    if not value.isdigit() and keysym not in ["Left", "Right", "Up", "Down", "BackSpace"]:
        return "break"


def pesquisa_id(frame, largura_label, altura_label, largura_frame, altura_frame, largura_botao, altura_botao):

    # Calculando as coordenadas x e y para centralizar o botão no frame
    x_id = (largura_frame - largura_botao) / 3.6
    y_id = (altura_frame - altura_botao) / 3

    global caixa_id
    caixa_id = Entry(frame)
    caixa_id.place(x=x_id,
                   y=y_id,
                   width=largura_label,
                   height=altura_label
                   )
    caixa_id.bind('<Key>', formatar_id)


def pesquisa_nome(frame, largura_label, altura_label, largura_frame, altura_frame, largura_botao, altura_botao):
    # Calculando as coordenadas x e y para centralizar o botão no frame
    x_nome = (largura_frame - largura_botao) / 2.3
    y_nome = (altura_frame - altura_botao) / 3

    global caixa_nome
    caixa_nome = Entry(frame)
    caixa_nome.place(x=x_nome,
                     y=y_nome,
                     width=largura_label,
                     height=altura_label)


def pesquisa_email(frame, largura_label, altura_label, largura_frame, altura_frame, largura_botao, altura_botao):
    # Calculando as coordenadas x e y para centralizar o botão no frame
    x_email = largura_frame - (largura_frame - largura_botao) / 1.9
    y_email = (altura_frame - altura_botao) / 3

    global caixa_email
    caixa_email = Entry(frame)
    caixa_email.place(x=x_email,
                      y=y_email,
                      width=largura_label,
                      height=altura_label
                      )


def pesquisa_data(frame, largura_label, altura_label, largura_frame, altura_frame, largura_botao, altura_botao):
    # Calculando as coordenadas x e y para centralizar o botão no frame
    x_data = largura_frame - (largura_frame - largura_botao) / 2.7
    y_data = (altura_frame - altura_botao) / 3
    global data
    data = Entry(frame)
    data.place(x=x_data,
               y=y_data,
               width=largura_label,
               height=altura_label)
    data.bind('<Key>', lambda event: adicionar_barra(event, data))


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


def proxima_pagina(janela_1, largura_janela, altura_janela):

    nome_na_caixa_de_texto = formatar_nome()

    email_na_caixa_de_texto = formatar_email()

    data_na_caixa_de_texto = formatar_data()

    classe = Banco()
    ultimo_id = classe.obter_ultimo_id(nome=nome_na_caixa_de_texto,
                                       email=email_na_caixa_de_texto, data=data_na_caixa_de_texto)

    if int(ultimo_id_da_tabela) == int(ultimo_id):
        pass

    else:

        numero_pagina = int(pagina.cget('text'))

        tabela(janela_1, largura_janela, altura_janela, numero=1, inicio=numero_pagina, resetb=True)

        numero_pagina += 1

        # Altera o texto do label
        pagina.config(text=str(numero_pagina))


def pagina_anterior(janela_1, largura_janela, altura_janela):

    if int(pagina.cget('text')) == 1:
        pass

    else:
        numero_pagina = int(pagina.cget('text'))

        numero_pagina -= 2

        tabela(janela_1, largura_janela, altura_janela, numero=1, inicio=numero_pagina, resetb=True)

        numero_pagina += 1
        pagina_str = numero_pagina
        pagina.config(text=pagina_str)


def paginacao_da_tabela(janela_1, largura_janela, altura_janela):
    # Definindo a posição e o tamanho do frame com base no tamanho da janela
    x = largura_janela * 0.2  # 20% da largura da janela
    y = altura_janela * 0.8  # 80% da altura da janela
    largura_frame = largura_janela * 0.6  # 60% da largura da janela
    altura_frame = altura_janela * 0.1  # 10% da altura da janela

    frame_paginacao = Frame(janela_1,
                            bg='#4c8fde',
                            borderwidth=1)
    frame_paginacao.place(x=x,
                          y=y,
                          width=largura_frame,
                          height=altura_frame)

    # Adiciona um label ao frame
    global pagina
    pagina = Label(frame_paginacao, text="1", bg='#4c8fde')
    pagina.place(relx=0.5, rely=0.5, anchor='center')

    botao_esquerda = Button(frame_paginacao, text="<", bg='#ffffca',
                            command=lambda: pagina_anterior(janela_1,
                                                            largura_janela, altura_janela))
    botao_esquerda.place(relx=0.4, rely=0.5, anchor='center')

    botao_direita = Button(frame_paginacao, text=">", bg='#ffffca',
                           command=lambda: proxima_pagina(janela_1,
                                                          largura_janela, altura_janela))
    botao_direita.place(relx=0.6, rely=0.5, anchor='center')


def deletar_dados_pelo_id(janela_1, largura_janela, altura_janela):
    # Definindo a posição e o tamanho do frame com base no tamanho da janela
    x = 0  # Inicia no canto esquerdo
    y = (altura_janela - (altura_janela * 0.4)) / 2  # Centraliza na vertical
    largura_frame = largura_janela * 0.19  # 19% da largura da janela
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

        if id_digitado == str:
            return

        classe = Banco()
        classe.deletar_dados(id_digitado)
        tabela(janela_1, largura_janela, altura_janela, numero=1, resetb=False)

        pagina.config(text="1")

    Label(frame_deletar,
          text="Deletar dados",
          bg='#4c8fde').place(relx=0.5, rely=0, anchor='n')

    Label(frame_deletar,
          text="Digite seu Id",
          bg='#4c8fde').place(relx=0.5, rely=0.2, anchor='n')  # Ajuste a posição vertical conforme necessário

    id_entry = Entry(frame_deletar)
    id_entry.place(relx=0.5, rely=0.4, anchor='n')  # Ajuste a posição vertical conforme necessário
    id_entry.bind('<Key>', formatar_id)

    Button(frame_deletar,
           text="Deletar",
           bg='#ffffca',
           command=deletar).place(relx=0.5, rely=0.6, anchor='n')  # Ajuste a posição vertical conforme necessário


def editar_dados(janela_1, largura_janela, altura_janela):

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
          bg='#4c8fde').place(relx=0.5, rely=0.02, anchor='center')

    Label(frame_editar,
          text="Id",
          bg='#4c8fde').place(relx=0.5, rely=0.10, anchor='center')

    id_text_box = Entry(frame_editar)
    id_text_box.place(relx=0.5, rely=0.15, anchor='center')
    id_text_box.bind('<Key>', formatar_id)

    Label(frame_editar,
          text="Nome",
          bg='#4c8fde').place(relx=0.5, rely=0.20, anchor='center')

    nome_text_box = Entry(frame_editar)
    nome_text_box.place(relx=0.5, rely=0.25, anchor='center')

    Label(frame_editar,
          text="Email",
          bg='#4c8fde').place(relx=0.5, rely=0.30, anchor='center')

    email_text_box = Entry(frame_editar)
    email_text_box.place(relx=0.5, rely=0.35, anchor='center')

    Label(frame_editar,
          text="Data de nascimento",
          bg='#4c8fde').place(relx=0.5, rely=0.40, anchor='center')

    data_text_box = Entry(frame_editar)
    data_text_box.place(relx=0.5, rely=0.45, anchor='center')
    data_text_box.bind('<Key>', lambda event: adicionar_barra(event, data_text_box))

    def editar():
        try:
            id_digitado = int(id_text_box.get())
            nome_digitado = nome_text_box.get().capitalize() if nome_text_box.get().strip() != "" else None
            email_digitado = email_text_box.get() if email_text_box.get().strip() != "" else None
            if email_digitado is not None:
                # Verificar se "@" está no texto e se termina com ".com"
                if "@" not in email_digitado or not email_digitado.lower().endswith(".com"):
                    print('sadasd')
                    label_erro.config(text='Email invalido')
                    return
                else:
                    email_digitado.lower()
            data_digitada = data_text_box.get() if data_text_box.get().strip() != "" else None
            if data_digitada:
                # Converte a string para um objeto datetime
                data_digitada = datetime.strptime(data_digitada, '%d/%m/%Y')
                # Quando for exibir ou usar, formate para string apenas com a data
                data_digitada = data_digitada.strftime('%Y-%m-%d')

            classe = Banco()
            classe.editar_dados(id_digitado, nome_digitado, email_digitado, data_digitada)

            tabela(janela_1, largura_janela, altura_janela, numero=1, resetb=False)

            # Atualiza o texto do label 'pagina'
            pagina.config(text="1")
            label_erro.config(text='Editado com sucesso')
        except ValueError:
            label_erro.config(text='Data invalida')

    Button(frame_editar,
           text="Editar",
           bg='#ffffca',
           command=editar).place(relx=0.5, rely=0.55, anchor='s')

    label_erro = Label(frame_editar, text="", bg='#4c8fde')
    label_erro.place(relx=0.5, rely=0.65, anchor='s')


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

    frame_de_pesquisa(janela_1, largura_janela, altura_janela)

    tabela(janela_1, largura_janela, altura_janela, numero=1)

    # Isso é para pegar os dados que irão passar na paginação, exemplo, a pessoa pesquisou nome x
    # a paginação ira se basear nesse nome x e ira paginar com ele
    paginacao_da_tabela(janela_1, largura_janela, altura_janela)

    deletar_dados_pelo_id(janela_1, largura_janela, altura_janela)

    editar_dados(janela_1, largura_janela, altura_janela)

    # Iniciando o loop principal da interface
    janela_1.mainloop()


if __name__ == '__main__':
    tela2()
