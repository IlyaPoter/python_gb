import logger

def calc(first_value, second_value, operator):
    logger.log_all(f'Производится расчет {first_value} {operator} {second_value}')
    if operator == '+':
        return first_value + second_value
    elif operator == '-':
        return first_value - second_value
    elif operator == '*':
        return first_value * second_value
    elif operator == '/':
        return first_value / second_value

