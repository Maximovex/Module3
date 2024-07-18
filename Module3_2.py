def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    email_ext=('.com','.ru','.net','.org')
    allright=False
    if '@'in (recipient and sender):
        for i in email_ext:
            if i in (recipient and sender):
                allright= True
                break
        else:
            print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        if allright: 
            if recipient==sender:
                print('Нельзя отправить письмо самому себе!')
            if sender=='university.help@gmail.com':
                print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
            else:
                print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")

send_email('Это сообщение для проверки связи', 'vasyok@1337gmail')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fanmail.ru', sender='urban.infogmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
