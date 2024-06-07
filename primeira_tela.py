from tkinter import *
from banco_de_dados import Banco
from datetime import datetime
from PIL import Image, ImageTk
from segunda_tela import tela2
from formatar_data_digitada import adicionar_barra


def cor_de_fundo_e_icone(janela_1):
    # Cor de fundo
    janela_1['bg'] = '#4c8fde'
    # Adicionar icone
    janela_1.iconbitmap('icone.ico')


def tamanho_da_janela(janela_1):
    # Obtendo as dimensões da tela
    largura_tela = janela_1.winfo_screenwidth()
    altura_tela = janela_1.winfo_screenheight()

    # Calculando 40% da largura e 80% da altura  da tela
    largura_janela = int(0.4 * largura_tela)
    altura_janela = int(0.8 * altura_tela)

    # Calculando os deslocamentos para centralizar a janela
    deslocamento_horizontal = (largura_tela - largura_janela) // 2
    deslocamento_vertical = (altura_tela - altura_janela) // 2

    # Configurando a janela com a largura, altura e deslocamentos calculados
    janela_1.geometry(f"{largura_janela}x{altura_janela}+{deslocamento_horizontal}+{deslocamento_vertical}")

    # Impede que o usuario possa mudar o tamanho da tela
    janela_1.resizable(False, False)


def cria_label_digitar_dados(janela_1):
    # Adiciona o label 1
    label_digitar_dados = Label(janela_1,
                                bg='#4c8fde',
                                text='Digite seus dados:',
                                fg='white',
                                font='Arial 20',
                                width=20,
                                height=3
                                )
    label_digitar_dados.pack()


def espaco(janela_1):
    # Adiciona um espaço entre a caixa de texto e o próximo objeto com a cor '#4c8fde'
    espac = Label(janela_1, text="", height=1, background='#4c8fde')
    espac.pack()


def cria_label_nome(janela_1):
    label_nome = Label(janela_1,
                       text='Nome:',
                       bg='#4c8fde',
                       fg='white',
                       font='Arial 20',
                       width=20
                       )
    label_nome.pack()


def nome_text_box(janela_1):
    global nome
    # Cria a caixa de texto
    nome = Entry(janela_1,
                 width=20)
    # Caixa de texto do nome
    nome.pack()


def cria_label_email(janela_1):
    label_email = Label(janela_1,
                        text='Email:',
                        bg='#4c8fde',
                        fg='white',
                        font='Arial 20',
                        width=20
                        )
    label_email.pack()


def email_text_box(janela_1):
    global email
    # Caixa de texto do email
    email = Entry(janela_1,
                  width=20)
    # Adiciona a caixa de texto à janela
    email.pack()


def cria_label_data(janela_1):
    label_data = Label(janela_1,
                       text='Data de nascimento:',
                       bg='#4c8fde',
                       fg='white',
                       font='Arial 20',
                       width=23
                       )
    label_data.pack()


def data_text_box(janela_1):
    global data
    # Caixa de texto da data
    data = Entry(janela_1,
                 width=20)
    data.pack()
    data.bind('<Key>', lambda event: adicionar_barra(event, data, END))


def abrir_outra_janela(janela_1):
    janela_1.withdraw()
    tela2(janela_1)


# Ocorre quando a pessoa clica no botão de adicionar dados
def adicionar_dado():
    try:
        if nome.get() == '':
            label_erro.config(text='Nome invalido')
            return

        # Verificar se "@" está no texto e se termina com ".com"
        if "@" not in email.get() or not email.get().lower().endswith(".com"):
            label_erro.config(text='Email invalido')
            return

        # Pega valores digitados
        nome_digitado = nome.get().capitalize()
        email_digitado = email.get().lower()
        data_digitada = data.get()
        # Converte a string para um objeto datetime
        data_final = datetime.strptime(data_digitada, '%d/%m/%Y')

        # Cria uma nova instância da classe banco
        classe = Banco()

        # Adiciona os dados de uma nova pessoa ao banco de dados
        classe.adicionar_dados(nome_digitado, email_digitado, data_final)

        # Atualiza a mensagem do label para 'Adicionado com sucesso'
        label_erro.config(text='Adicionado com sucesso')
    except ValueError:
        label_erro.config(text='Data invalida')


def frame_com_botoes(janela_1):
    # Criando um frame para conter os botões, com a cor de fundo desejada
    frame = Frame(janela_1,
                  bg='#4c8fde')
    frame.pack()

    # Adicionando o primeiro botão ao contêiner
    adicionar = Button(frame,
                       text="Adicionar",
                       command=lambda: adicionar_dado(),
                       bg='#ffffca',
                       fg='black')
    # Coloca o primeiro botão na tela, com um leve espaçamento à direita
    adicionar.pack(side="left", padx=5)

    # Adicionando o segundo botão ao contêiner
    tabela = Button(frame,
                    text="Ver tabela",
                    command=lambda: abrir_outra_janela(janela_1),
                    bg='#ffffca',
                    fg='black')
    # Coloca o segundo botão na tela, com um leve espaçamento à esquerda
    tabela.pack(side="left",
                padx=5)


def cria_imagem(janela_1, largura_atual, altura_atual):
    # Carrega a imagem usando o módulo PIL
    imagem = Image.open("imagem.png")

    # Redimensiona a imagem para o tamanho desejado
    imagem = imagem.resize((int(0.2 * largura_atual), int(0.2 * altura_atual)))

    # Converte a imagem PIL em uma imagem Tkinter
    imagem_tk = ImageTk.PhotoImage(imagem)

    # Cria um rótulo e adiciona a imagem ao rótulo
    rotulo = Label(janela_1, bg='#4c8fde')
    rotulo.imagem_tk = imagem_tk  # Armazena a imagem como um atributo do rótulo
    rotulo.config(image=rotulo.imagem_tk)

    # Posiciona o rótulo na janela
    rotulo.pack()


def tela1():

    # Criando uma instância da classe Tk
    janela_1 = Tk()
    # Titulo da janela
    janela_1.title("Sistema de cadastro")

    # chama fução que cria a cor de fundo e coloca o icone
    cor_de_fundo_e_icone(janela_1)
    tamanho_da_janela(janela_1)

    # Para calcular largura e altura da imagem no final
    largura_atual = janela_1.winfo_width()
    altura_atual = janela_1.winfo_height()

    cria_label_digitar_dados(janela_1)

    cria_label_nome(janela_1)

    nome_text_box(janela_1)

    espaco(janela_1)

    cria_label_email(janela_1)

    email_text_box(janela_1)

    espaco(janela_1)

    cria_label_data(janela_1)

    data_text_box(janela_1)

    espaco(janela_1)

    frame_com_botoes(janela_1)

    cria_imagem(janela_1, largura_atual, altura_atual)

    # label que mostra a mensagem de sucesso ou de falha
    global label_erro
    label_erro = Label(janela_1,
                       bg='#4c8fde',
                       fg='white',
                       font='Arial 20',
                       width=20,
                       height=3
                       )
    label_erro.pack()

    # Iniciando o loop principal da interface
    janela_1.mainloop()


if __name__ == '__main__':
    tela1()
