from tkinter import *
from banco_de_dados import Banco
from datetime import datetime
from PIL import Image, ImageTk
from segunda_tela import tela2

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


def cria_label_1(janela_1):
    # Adiciona o label 1
    label_1 = Label(janela_1,
                    bg='#4c8fde',
                    text='Digite seus dados:',
                    fg='white',
                    font='Arial 20',
                    width=20,
                    height=3
                    )
    label_1.pack()


def cria_label_2(janela_1):
    # Adiciona o label 2
    label_2 = Label(janela_1,
                    text='Digite seu nome:',
                    bg='#4c8fde',
                    fg='white',
                    font='Arial 20',
                    width=20
                    )
    label_2.pack()


def cria_label_3(janela_1):
    # Adiciona o label 3
    label_3 = Label(janela_1,
                    text='Digite seu email:',
                    bg='#4c8fde',
                    fg='white',
                    font='Arial 20',
                    width=20
                    )
    label_3.pack()


def cria_label_4(janela_1):
    # Adiciona o label 4
    label_4 = Label(janela_1,
                    text='Digite sua data de nascimento:',
                    bg='#4c8fde',
                    fg='white',
                    font='Arial 20',
                    width=23
                    )
    label_4.pack()


def espaco(janela_1):
    # Adiciona um espaço entre a caixa de texto e o próximo objeto com a cor '#4c8fde'
    espac = Label(janela_1, text="", height=1, background='#4c8fde')
    espac.pack()


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
    def adicionar_dado():

        try:
            # Pega valores digitados
            nome_digitado = nome.get().capitalize()
            email_digitado = email.get()
            data_digitada = data.get()
            # Converte a string para um objeto datetime
            data_final = datetime.strptime(data_digitada, '%d/%m/%Y')

            # Cria uma nova instância da classe banco
            classe = Banco()

            # Adiciona os dados de uma nova pessoa ao banco de dados
            classe.adicionar_dados(nome_digitado, email_digitado, data_final)

            # Atualiza a mensagem do label para 'Adicionado com sucesso'
            label_erro.config(text='Adicionado com sucesso')
        except Exception as e:  # Captura todas as exceções como 'e'
            # Atualiza a mensagem do label para 'Você digitou algo errado'
            label_erro.config(text='Você digitou algo errado')

    # formatar a data de nascimento digitada
    def adicionar_barra(event):
        # Verifica se o caractere digitado é um número, uma barra ou backspace

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

    def abrir_outra_janela():
        janela_1.destroy()
        tela2()

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

    # Chama a fução que cria o primeiro label
    cria_label_1(janela_1)

    # Chama a função que cria o segundo label
    cria_label_2(janela_1)

    # Cria a caixa de texto
    nome = Entry(janela_1,
                 width=20)
    # Caixa de texto do nome
    nome.pack()

    espaco(janela_1)

    # Chama a função que cria o Terceiro label
    cria_label_3(janela_1)

    # Caixa de texto do email
    email = Entry(janela_1,
                  width=20)
    # Adiciona a caixa de texto à janela
    email.pack()

    espaco(janela_1)

    # Chama a função que cria o quarto label
    cria_label_4(janela_1)

    # Caixa de texto da data
    data = Entry(janela_1,
                 width=20)
    data.pack()
    data.bind('<Key>',
              adicionar_barra)

    espaco(janela_1)

    # Criando um frame para conter os botões, com a cor de fundo desejada
    frame = Frame(janela_1,
                  bg='#4c8fde')
    frame.pack()

    # Adicionando o primeiro botão ao contêiner
    adicionar = Button(frame,
                       text="Adicionar",
                       command=adicionar_dado,
                       bg='#ffffca',
                       fg='black')
    # Coloca o primeiro botão na tela, com um leve espaçamento à direita
    adicionar.pack(side="left", padx=5)

    # Adicionando o segundo botão ao contêiner
    botao2 = Button(frame,
                    text="Ver tabela",
                    command=lambda: abrir_outra_janela(),
                    bg='#ffffca',
                    fg='black')
    # Coloca o segundo botão na tela, com um leve espaçamento à esquerda
    botao2.pack(side="left",
                padx=5)

    cria_imagem(janela_1, largura_atual, altura_atual)

    # Adiciona o label 1
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
