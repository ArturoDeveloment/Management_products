from validations.decorators import get_atributes


class Sellers:
    _seller_db = {1: {'name': 'carlos', 'phone_number': 3207515166, 'address': 'colinas', 'age': 18}, 2: {'name': 'juan', 'phone_number': 3207515166, 'address': 'colinas', 'age': 23}}
    def __init__(self, **kwargs):
        if len(kwargs) > 0:
            self.__id = self.get_id
            self.__name = kwargs.get('name')
            self.__phone_number = kwargs.get('phone_number')
            self.__address = kwargs.get('address')
            self.__age = kwargs.get('age')
            self.__set_atributes
        
    @property
    def get_id(self):
        keys = list(self._seller_db.keys())
        keys = 0 if len(keys) == 0 else keys[-1]
        return keys + 1
    
    @get_atributes
    def get_atributes(self, data: dict)-> dict:
        return data
    
    @property
    def __set_atributes(self):
        data = self.get_atributes(self).copy()
        id = data.get('id')
        data.pop('id')
        self._seller_db[id] = data
        print(f"Su id es {id}")
    
    @property
    def get_db_seller(self):
        print(f"\n{'id': ^5}|{'nombre': ^30}|{'Teléfono': ^15}|{'dirección': ^15}|{'edad':^3}")
        if not(len(self._seller_db) > 0):
            print('No existe ningun registro aún\n')
            return None
        for keys, values in self._seller_db.items():
            dato = lambda key: values.get(key)
            print(f"{keys: <5}|{dato('name')[:30]: <30}|{str(dato('phone_number'))[:15]: <15}|{dato('address')[:15]: <15}|{str(dato('age'))[:3]: <3}")
        else:
            print("\n")
        
    def change_atributes(self, id, *args):
        for i in args:
            if self._seller_db.get(id) == None:
                print('Ese registro no existe')
                return None
            elif self._seller_db.get(id).get(i) == None:
                print(f'Usted no tiene el dato "{i}"')
                continue
            new_value = input(f"Digite el nuevo dato para {i}: ")
            self._seller_db[id][i] = new_value
            print('Cambio exitoso')
    
    def drop_seller_db(self, id):
        if self._seller_db.get(id) == None:
                print(f'Ese id no existe')
                return None
        self._seller_db.pop(id)
        print('Se elimino exitosamente')
        
    def request_id(self, id):
        return id in list(self._seller_db.keys())