# class Main:
#     def __init__(self):
#         self.name = input('Выберите пиццу \n1 - Peperoni (20$) \n2 - Barbequ (25$) \n3 - Dari_morya (30$) \nВведите: ')
#         self.nachinka = input('Выберите начинку \n1 - tomato (5$) \n2 - cheese (10$) \n3 - big testo (3$)'
#                               '\n4 - small testo(5$) \nВведите: ')
#
#
#
# class Terminal(Main):
#     def sort(self):
#         return self.name, self.nachinka
#
#
#
# a = Terminal()
# print(f'Ваша пицца {a.name} \n Ваша начинка {a.nachinka} \n Общая цена ', )
# # b = Terminal()
# # b.sort()



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

        # for _ in self.name:
        #     if _ == '1':
        #         _ = self.price_name[0]
        #     if _ == '2':
        #         _ = self.price_name[1]
        #     if _ == '3':
        #         _ = self.price_name[2]
        #
        # for _ in self.nachinka:
        #     if _ == '1':
        #         _1 = self.pice_nachinka[0]
        #     if _ == '2':
        #         _1 = self.pice_nachinka[1]
        #     if _ == '3':
        #         _1 = self.pice_nachinka[2]
        #     print('Общая цена: ', _ + _1, '$')



a = Terminal()
a.vivod()
for i in range(3):
    one_more_time = input('Хотите еще заказать y/n: ')
    if one_more_time == 'y':
        b = Terminal()
        b.vivod()
    else:
        break
