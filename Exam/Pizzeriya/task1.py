class Main:
    def __init__(self):
        self.spisok_name = []
        self.name = input('1 - peperoni\n2 - BBQ\n3 - dari morya\nВыберите: ')
        self.spisok_name.append(self.name)
        self.spisok_nachinka = []
        self.nachinka = input('1 - cheese\n2 - tomato\n3 - chili\nВыберите: ')
        self.spisok_nachinka.append(self.nachinka)
        self.name_pizza = ['peperoni', 'BBQ', 'dari_morya']
        self.name_nachinka = ['cheese', 'tomato', 'chili']
        self.price_name = ['20', '30', '40']
        self.pice_nachinka = ['3', '4', '5']


class Terminal(Main):
    def vivod(self):
        for x in self.spisok_name: #Выводит имя пиццы
            if x == '1':
                print(f'Ваш заказ:\nПицца {self.name_pizza[0]}')
            if x == '2':
                print(f'Ваш заказ:\nПицца {self.name_pizza[1]}')
            if x == '3':
                print(f'Ваш заказ:\nПицца {self.name_pizza[2]}')

        for i in self.spisok_nachinka: #Выводит имя начинки
            if i == '1':
                print(f'Начинка {self.name_nachinka[0]}')
            if i == '2':
                print(f'Начинка {self.name_nachinka[1]}')
            if i == '3':
                print(f'Начинка {self.name_nachinka[2]}')

        for _ in self.name: # Выводит цену пиццы
            if _ == '1':
                print(f'Цена пиццы {self.price_name[0]}$')
            if _ == '2':
                print(f'Цена пиццы {self.price_name[1]}$')
            if _ == '3':
                print(f'Цена пиццы {self.price_name[2]}$')

        for m in self.nachinka:
            if m == '1': # Выводит цену начинки
                print(f'Цена начинки {self.pice_nachinka[0]}$')
            if m == '2':
                print(f'Цена начинки {self.pice_nachinka[1]}$')
            if m == '3':
                print(f'Цена начинки {self.pice_nachinka[2]}$')


a = Terminal()
a.vivod()
for i in range(3):
    one_more_time = input('Хотите еще заказать y/n: ')
    if one_more_time == 'y':
        b = Terminal()
        b.vivod()
    else:
        break
