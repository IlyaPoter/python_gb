# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = 'ыоатылабв влп вав впь дыаь ыабвдаь вп абвв пав абв'
text = text.split()
result_text = list(filter((lambda el: 'абв' not in el),text))
print(' '.join(result_text))
