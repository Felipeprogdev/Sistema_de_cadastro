def adicionar_barra(event, data, end):
    if event.keysym in ['Left', 'Right', 'Up', 'Down']:
        return

    # Verifica se o caractere digitado é um número, uma barra ou backspace
    elif event.char.isdigit() or event.char == '/' or event.char == '\x08':
        # Pega valor digitado
        entrada = data.get()

        # Verifica se já foram digitados 10 caracteres ou se foi digitado um backspace
        if len(entrada) < 10 or event.char == '\x08':
            # Se for um backspace não adicione a /

            if event.char != '\x08':
                if len(entrada) == 4 and int(event.char) >= 3:
                    # Limpa a caixa de texto
                    data.delete(0, end)
                    data.insert(end, entrada[0])
                    data.insert(end, entrada[1])
                    data.insert(end, entrada[2])
                    data.insert(end, entrada[3])
                    return 'break'

                if len(entrada) == 1 and int(entrada[0]) == 3 and int(event.char) >= 2:
                    # Limpa a caixa de texto
                    data.delete(0, end)
                    # Insere '0', o antigo índice 0, '/', '0' e o caractere digitado
                    data.insert(end, '0')
                    data.insert(end, entrada[0])
                    data.insert(end, '/')
                    data.insert(end, '0')
                    data.insert(end, event.char)
                    data.insert(end, '/')
                    return 'break'

                if (
                        len(entrada) == 0 and event.char.isdigit() and int(event.char) >= 4 and int
                        (event.char) <= 9 or len(entrada) == 3 and event.char.isdigit() and int
                        (event.char) >= 2 and int(event.char) <= 9
                ):
                    data.insert(end, '0')
                    data.insert(end, event.char)
                    data.insert(end, '/')
                    return 'break'

                if len(entrada) == 1 or len(entrada) == 4:
                    '''Insere uma barra após os dois primeiros caracteres ou após os cinco 
                    primeiros, exceto se o caractere for backspace'''
                    data.insert(end, event.char)
                    data.insert(end, '/')
                    return 'break'

        else:
            # Se o caractere não for um número, uma barra ou backspace, não o insere na caixa de texto
            return 'break'

    else:
        # Se o caractere não for um número, uma barra, backspace ou uma tecla de seta, não o insere na caixa de texto
        return 'break'


if __name__ == '__main__':
    pass
