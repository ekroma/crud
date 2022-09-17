import json
from views import *

class Car(CreateMixin, UpdateMixin, ListingRetrieveMixin, DestroyMixin):
    def __init__(self, user, password):
        self.user = user
        self.__password = password
    
    def check_pass(self, password):
        if self.__password == password:
            print('вы успешно вошли')
            global flag
            flag = False
        else:
            print('пороль не верный')
            



flag = True
while flag == True:
    enter = input('1 - зарегистрироватся, 2 - войти: ')
    if enter == '1':
        loggin = input('введите логин: ')
        password = input('введите пороль: ')
        check_pass = input('подтвердите пороль: ')
        if password == check_pass:
            locals()[loggin] = Car(loggin, password=password)
            print('вы успешно зарегались')
        else:
            print('пороли не совподают')
    elif enter == '2':
        loggin = input('введите логин: ')
        password = input('введите пороль: ')

        try:
            eval(loggin).check_pass(password)
        except:
            print('токого логина нет')

while True:
    i = input('1 - create, 2 - listing, 3 - update, 4 - delet, end - exit: ')

    if i == '1':
        locals()[loggin].create_product()
    elif i == '2':
        locals()[loggin].listing()
    elif i == '3':
        locals()[loggin].update_product()
    elif i == '4':
        locals()[loggin].delete_product()
    elif i.lower() == 'end':
        exit
    else:
        print('токой операции нет')

 