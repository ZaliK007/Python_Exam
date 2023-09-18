import random
print('Угадай Ютубера')
def Hangman():
    list = ['кофи', 'андифай', 'эксайл', 'парадеевич', 'кореш']
    a = random.choice(list)
    conjecture = 'аеёиыоуэяю'
    popitki = 6
    while popitki > 0:
        b = 0
        for i in a:
            if i in conjecture: print(i, end=' ')
            else:
                print('_', end=' ')
                b += 1

        if b == 0:
            print('Ты выграл')
            break

        conjecture1 = input('Напишите букву: ')
        conjecture += conjecture1
        if conjecture1 not in a:
            popitki -= 1
            print('Не правилдьно')
            print(f'У тебя осталось попыток, {popitki}')
            if popitki < 6: print(' | ')
            if popitki < 5: print(' | ')
            if popitki < 4: print(' O ')
            if popitki < 3: print('/|\ ')
            if popitki < 2: print(' | ')
            if popitki < 1: print('/ \ ')
            if popitki == 0:
                print(f'Ты проиграл это было слово {a}')

answer = 'да'
while answer == 'да':
    Hangman()
    print('Хочешь  сыграть еще раз? \nда/нет')
    answer = str(input())
