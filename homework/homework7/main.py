from calculation import calc
from user_interface import get_data as gd
import logger
import controller







user_input = input('Вычисление - 1. Вывод лога - 2.   ')
if user_input == '1':
    print(controller.control_data())
else:
    logger.log_out()








# first_value, second_value, operator = gd()
# # logger.log_res(calc(*logger.log_in(first_value, second_value, operator)))

# print(calc(first_value, second_value, operator))
