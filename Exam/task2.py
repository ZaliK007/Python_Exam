import random

# a = str(input('Введите к, н, б:'))
#
# list = ['к', 'н', 'б']
# ran = random.choice(list)
# print(ran)

# if a != list[0] and a != list[1] and list[2]:
#     print('Введи только к, н, б')
#     b = str(input('Введите к, н, б:'))

def play():
    a = str(input('Введите к, н, б:'))

    list = ['к', 'н', 'б']
    ran = random.choice(list)
    if ran == 'к' and a == 'н':
        print(ran)
        print('бот выграл')
    if ran == 'н' and a == 'н':
        print(ran)
        print("Ничья")
    if ran == 'б' and a == 'н':
        print(ran)
        print('Ты выграл')
    if ran == 'к' and a == 'к':
        print(ran)
        print('ничья')
    if ran == 'н' and a == 'к':
        print(ran)
        print('ты выграл')
    if ran == 'б' and a == 'к':
        print(ran)
        print('бот выграл')
    if ran == 'к' and a == 'б':
        print(ran)
        print('ты выграл')
    if ran == 'н' and a == 'б':
        print(ran)
        print('бот выграл')
    if ran == 'б' and a == 'б':
        print(ran)
        print('ничья')

    if a != list[0] and a != list[1] and list[2]:
            print('Введи только к, н, б')
            play()
play()

# if a != list[0] and a != list[1] and list[2]:
#     print('Введи только к, н, б')
#     play()


def one_more():
    one_more_time = str(input('Хочешь еще раз сыграть (y/n)'))
    for i in one_more_time:
        if i == 'y':
            play()
        else:
            print('Спасибо за игру')
            break
one_more()
one_more()
