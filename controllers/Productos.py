from validations.decorators import get_atributes


class Products:
    _products_db = {}
    def __init__(self, **kwargs):
        if len(kwargs) > 0:
            self.__id = self.get_id
            self.__name = kwargs.get('name')
            self.__cantidity = kwargs.get('cantidity')
            self.__unit_price = kwargs.get('unit_price')
            self.__set_atributes
        
    @property
    def get_id(self):
        keys = list(self._products_db.keys())
        keys = 0 if len(keys) == 0 else keys[-1]
        return keys + 1
    
    @get_atributes
    def get_atributes(self, data: dict):
        return data
    
    @property
    def __set_atributes(self):
        data = self.get_atributes(self).copy()
        id = data.get('id')
        data.pop('id')
        self._products_db[id] = data
        print(f"El id para {data.get('name')} es {id}")
    
    @property
    def get_db_products(self):
        print(f"\n{'id': ^4}|{'nombre': ^30}|{'cantidad': ^10}|{'precio unitario': ^15}")
        if not(len(self._products_db) > 0):
            print('No existe ningun producto aún\n')
            return None
        for keys, values in self._products_db.items():
            dato = lambda key: values.get(key)
            print(f"{keys: <4}|{dato('name')[:30]: <30}|{str(dato('cantidity'))[:15]: <10}|{str(dato('unit_price'))[:15]: <15}")
        else:
            print("\n")
        
    def change_atributes(self, id, *args):
        for i in args:
            if self._products_db.get(id) == None:
                print('Ese producto no existe')
                return None
            elif self._products_db.get(id).get(i) == None:
                print(f'Usted no tiene el dato "{i}"')
                continue
            new_value = input(f"Digite el nuevo dato para {i}: ")
            self._products_db[id][i] = new_value
            print('Cambio exitoso')
    
    def drop_products_db(self, id):
        if self._products_db.get(id) == None:
                print(f'Ese id no existe')
                return None
        self._products_db.pop(id)
        print('Se elimino exitosamente')
    
    def request_id(self, id):
        return id in list(self._products_db.keys())
    
    def list_all_data(self):
        return self._products_db