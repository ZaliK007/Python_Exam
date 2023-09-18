import random
number = random.randint(0, 15)
random_numer = 0
print('Есть число от 0 до 15, ты должен угадать')
while random_numer < 3:
    num = int(input())
    random_numer += 1

    if num < number:
        print('Больше')

    if num > number:
        print('Меньше')

    if num < number:
        print("Больше")

    if num > number:
        print('Меньше')

    if num == number:
        break

if num == number:
    print("Ты угадал мое число!")
else:
    print ("Не угадал! Я загадал число {0}".format(number))