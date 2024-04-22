def formatar_id(event):
    value = event.char
    keysym = event.keysym
    if not value.isdigit() and keysym not in ["Left", "Right", "Up", "Down", "BackSpace"]:
        return "break"


if __name__ == '__main__':
    pass
