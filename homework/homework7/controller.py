from calculation import calc
from user_interface import get_data as gd
from logger import log_all



def control_data():
    log_all('Записываем переменные. Вызываем функцию вычисления.')
    first_value, second_value, operator = gd()
    result = calc(first_value, second_value, operator)
    return result

