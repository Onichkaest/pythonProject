# это явно не совсем то, что надо было сделать, но мой мозг лучшего варианта не может пока придумать
#
# Написать программу которая открывает текстовый файл и считает следующее:
# 1. Общее кол-во слов 2. Кол-во уникальных (разных) Не влияет на уникальность:
# Заглавные и прописные буквы Знаки препинания: ',' '.' '!' '?'

# Сохраняет кол-ва в отдельный файл. Выписывает все уникальные слова в алфавитном порядке.


with open('trimushketera.txt', 'r', encoding='UTF8') as read_file:
    data = read_file.read()
with open(f'trimushketera_copy.txt', 'w', encoding='UTF8') as file:
    file.write(data.lower())
    x = len(data)
with open(f'trimushketera_result.txt', 'w', encoding='UTF8') as file:
    file.write(str(x))
    file.write('\n')
    data = data.replace(',', '').replace('.', '').replace('!', '').replace('?', '').replace('-', '').replace(':', '')
    data = set(data.split())  # set so can get rid of duplicates
    data = list(data)  # to list so can sort
    y = (len(data))  # 349403
    file.write(str(y))
    data.sort()
    data = str(data)
    file.write('\n')
    file.write(data)

