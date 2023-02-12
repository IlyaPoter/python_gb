import logger

def get_data():
    a = input('Введите число: ')
    operator = input('Введите действие над числом: ')
    b = input('Введите число: ')

    logger.log_all(f'Получаем число {a}, оператор = "{operator}", число {b}')



    if 'j' in a:
        a = complex(a)
    else: a = int(a)

    if 'j' in b:
        b = complex(b)
    else: b = int(b)

    return a, b, operator

