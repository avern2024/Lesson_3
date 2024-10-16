# Создаем функцию для проверки валидности адреса электронной почты
def is_valid_email(email):
    # Проверяем наличие символа '@' и одного из доменов
    return '@' in email and any(domain in email for domain in ['.com', '.ru', '.net'])


def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if not is_valid_email(recipient):
        print('Невозможно отправить письмо с адреса <sender> на адрес <recipient>')
    elif not is_valid_email(sender):
        print('Невозможно отправить письмо с адреса <sender> на адрес <recipient>')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == "university.help@gmail.com":
        print('Письмо успешно отправлено с адреса <sender> на адрес <recipient>')
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>')


send_email('Это сообщение для проверки связи', 'avern@ya.con')
send_email('Это сообщение для проверки связи', 'avernya.com')
send_email('Это сообщение для проверки связи', 'avern@ya.com', sender='avernya.com')
send_email('Это сообщение для проверки связи', 'avern@ya.com', sender='avern@ya.com')
send_email('Это сообщение для проверки связи', 'avern@ya.com')
