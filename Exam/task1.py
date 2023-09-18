class Main:
    def __init__(self):
        self.name = input('1 - peperoni \n2 - barbequ \n3 - dari morya \nВыберите пиццу: ')
        self.nachinka = input('1 - ketchup \n2 - kolbasa \n3 - big testo \n4 - small testo \nВыберите начинку: ')
        self.price = (self.name + self.nachinka)
        self.text = (self.name, self.nachinka)
        self.vir = 'E'

    def __str__(self):
        if self.text[0]:
            self.vir = f'\nПицца: {self.text[0]}\nНачинка: {self.text[1]}\nцена: {self.price}$'
        return self.vir

    def sortirovka(value):
        name = {'1': 10, '2': 25, '3': 55}
        nachinka = {'1': 7, '2': 11, '3': 13, '4': 5}
        if value in name: return name[value]
        elif value in nachinka: return nachinka[value]
        else: return 0

    def smth(value):
        name = {'1': 'peperoni', '2': 'barbequ', '3': 'dari morya'}
        nachinka = {'1': 'ketchup', '2': 'kolbasa', '3': 'big testo', '4': 'small testo'}
        if value in name:
            return name[value]
        elif value in nachinka:
            return nachinka[value]


class Terminal:
    def __init__(self):
        self.count = self.von()
        self.overall = sum([x.price for x in self.count])

    def info(self):
        print('Детали заказа:')
        for x in [z for z in self.count if str(z) != 'E']:
            print(x)
        print(f'Общая цена: {self.overall} $')

    def von(self):
        basket = []
        while True:
            a = Main()
            basket.append(a)
            print(f'Ваш заказ:{a}') if str(a) != 'E' else print('\nНе правильный заказ!')
            cont = input('Хотите заказать еще один y/n\n')
            if cont.lower().strip() == 'n': break
        return basket


a = Terminal()
a.info()