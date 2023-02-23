def calc(text):
    text = text.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ').split()
    if text[1] == '+':
        return int(text[0]) + int(text[2])
    elif text[1] == '-':
        return int(text[0]) - int(text[2])
    elif text[1] == '*':
        return int(text[0]) * int(text[2])
    else:
        return int(text[0]) / int(text[2])
