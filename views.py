from curses.ascii import isdigit
import json
from pkgutil import get_data

data_json = []
class Get_info:
    def get_data(self):
        with open('data.json') as file:
            return json.load(file)

    def catalog(self, i):
        print(f'''
            ID             : {i["id"]}
            Марка          : {i["mark"]}
            Модель         : {i["model"]}
            Год выпуска    : {i["year"]}
            Объем двигателя: {i["engine"]}
            Цвет           : {i["color"]}
            Кузов          : {i["body"]}
            пробег         : {i["mileage"]}
            Цена           : {i["price"]}
            лайки          : {i["likes"]}
            '''   
        )

    def get_id(self):
        with open('id.txt', 'r') as file:
            id = int(file.read())
            id += 1
        with open('id.txt', 'w') as file:
            file.write(str(id))
        return id

    def _get_or_set_objects_and_id(self):
        try:
            if (self.objects or not self.objects) and (self.id or not self.id):
                pass
        except (NameError, AttributeError):
            self.objects = []
            self.id = 0

class CreateMixin(Get_info):

    def create_product(self):
        self._get_or_set_objects_and_id()
        try:    
            product = {
                'id': self.get_id(),
                'mark': input('Введите марку машины: '), 
                'model': input('Введите модель машины: '), 
                'year': int(input('Введите год выпуска машины: ')), 
                'engine': round(float(input('Введите объем двигателя машины: ')),1), 
                'color': input('Введите цвет машины: '),
                'body': input('Выберите тип кузова (седан, универсал. купе, хэтчбек, минивен, внедорожник, пикап): '),
                'mileage': int(input('Введите пробег машины: ')),
                'price': round(float(input('Введите цену машины: ')),2),
                'comment': [],
                'likes': 0
                }

        except ValueError:
            print()
            print('Вы ввели неверные данные!')
            print()
            self.create_product()
        else:
            data_json.append(product)
            with open('data.json', 'w') as file:
                json.dump(data_json, file)
            
            

class UpdateMixin(Get_info):

    def update_product(self):
        data = self.get_data()
        flag = False

        id = int(input('Введите id продукта: '))
        
        product = list(filter(lambda x: x['id'] == id, data))

        if not product:
            return 'Такого продукта нет'

        index_ = data.index(product[0])
        choice_ = int(input('что вы хотите изменить? 1 - Марка, 2 - Модель, 3 - описание, 4 - год выпуска, 5 - цена: '))

        if choice_ == 1:
            data[index_]["mark"] = input('Введите новую марку: ')

        elif choice_ == 2:
            data[index_]["model"] = input('Введите новую модель: ')

        elif choice_ == 3:
            data[index_]["year"] = int(input('Введите новую дату выпуска: '))

        elif choice_ == 4:
            data[index_]["engine"] = input('Введите новый объем двигателя: ')

        elif choice_ == 4:
            data[index_]["color"] = input('Введите новый цвет: ')

        elif choice_ == 4:
            data[index_]["body"] = input('Введите новый тип кузова: ')
            
        elif choice_ == 4:
            data[index_]["miliage"] = input('Введите новый пробег: ')

        elif choice_ == 5:
            data[index_]["price"] = input('Введите новую цену: ')

        else:
            print('Такого поля нет')

        with open('data.json', 'w') as file:
            json.dump(data, file)

class ListingRetrieveMixin(Get_info):
    def listing(self):
        data = self.get_data()
        
        while True:
            with open('data.json','r') as file:
                for i in eval(file.read()):
                    self.catalog(i)
            id = input('Введите id продукта для просмотра коментариев(retrieve)(end - exit): ')
            
            if id.lower() == 'end':
                return 
            elif id.isdigit():
                id = int(id)
            else:
                print('вы ввели не коректные данные')
                self.listing()
            product = list(filter(lambda x: x['id'] == id, data))

            if not product:
                print('Такого продукта нет')
                self.listing()

            index_ = data.index(product[0])
            for i in product:
                self.catalog(i)
                print('comments:')
                for comments in i['comment']:
                    print(comments)
            ch = input('продолжть? (1 - коментарии, 2 - лайк, any keys - exit): ')
            if ch == '1':
                data[index_]["comment"].append(self.user+': '+input('введите комент: '))
            elif ch == '2':
                data[index_]["likes"] += 1
            else:
                return
            with open('data.json', 'w') as file:
                json.dump(data, file)

class DestroyMixin(Get_info):
    def delete_product(self):
        data = self.get_data()

        id = int(input('Введите id продукта для удоления: '))
        product = list(filter(lambda x: x["id"] == id, data))

        if not product:
            return 'Такого продукта нет'
            
        index_ = data.index(product[0])
        data.pop(index_)

        with open('data.json', 'w') as file:
            json.dump(data, file)
