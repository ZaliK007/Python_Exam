def Victorina():
    questions = [('У осминогов 2 сердца', 'нет'), ('В русском 10 гласных звуков', 'нет'), ('У человека есть средднее ухо', 'да'),
                 ('Правдали что черепахи плачут', 'да'),]
    for i, x in questions:
        print(i, 'да/нет')
        answer = input()
        if answer == x:
            print("правильный ответ")
        else:
            print("неправильный ответ")


Victorina()