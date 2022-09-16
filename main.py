import json
from views import *

class Car(CreateMixin, UpdateMixin, ListingMixin, DestroyMixin):
    data = []
    def save(self):
        self.data.append(self.objects)
        with open('data.json', 'w') as file:
            json.dump(self.data, file)
    
a = Car()

while True:
    i = input('1 - create, 2 - listing, 3 - update, 4 - delet: ')

    if i == '1':
        a.create_product()
        a.save()
    elif i == '2':
        a.listing()
    elif i == '3':
        a.update_product()
    elif i == '4':
        a.delete_product()
        a.save()