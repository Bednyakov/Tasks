with open('chat_log.txt', 'w', encoding='UTF-8') as chat:
    chat.writelines('Чат:\n')

def chat(chatfile):
    while True:
        try:
            name = input('Введите имя: ')
            act = int(input('''1 - Посмотреть текущий текст чата
2 - Отправить сообщение
Введите нужный вариант: '''))
            if act == 1:
                with open(chatfile, 'r', encoding='UTF-8') as file:
                    print(file.read())
            if act == 2:
                with open(chatfile, 'a', encoding='UTF-8') as file:
                    message = input('Сообщение: ')
                    file.writelines(f'{str(name)}: {str(message)}\n')
        except:
            print('\nДействуйте по инструкции.')

chat('chat_log.txt')



