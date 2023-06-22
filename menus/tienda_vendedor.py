from controllers.Vendedor import Sellers

class SellerMenu:
    def set_option(self, give_option):
        match give_option:
            case 'a':
                self.option_a()
            case 'b':
                self.option_b()
            case 'c':
                self.option_c()
            case 'd':
                self.option_d()
    
    def option_a(self):
        try:
            print('\n')
            message = lambda key: input(f'Digite su {key}: ')
            data = dict([
                (key, message(key) if key not in ['numero de telefono', 'edad'] else int(message(key))) for key in ['nombre', 'numero de telefono', 'dirección', 'edad']
            ])
            data = dict(zip(['name', 'phone_number', 'address', 'age'], data.values()))
            if data.get('name').isnumeric() or str(data.get('name')).isdigit() or str(data.get('name')).isdecimal():
                raise Exception('El nombre es un número')
            if not(data.get('name').replace(' ', '').isalpha()):
                raise Exception('Formato de nombre no es valido')
            if data.get('age') < 0 or len(str(data.get('age'))) > 3:
                raise Exception('formato de edad no valido')
            seller = Sellers(**data)
        except Exception as e:
            print(e)
    
    def option_b(self):
        Sellers().get_db_seller
    
    def option_c(self):
        id = int(input('Digite su id: '))
        data = {1: 'nombre', 2: 'numero de telefono', 3: 'dirección', 4: 'edad'}
        for key, value in data.items():
            print(f"{key} - {value}")
        try:
            option = (int(input('Digite opción: ')))
        except Exception as e:
            print(e)
            return None
        data_modifier = data.get(option)
        paramts = {'nombre': 'name', 'numero de telefono': 'phone_number', 'dirección': 'address', 'edad': 'age'}
        data_modifier = paramts.get(data_modifier)
        Sellers().change_atributes(id, data_modifier)
    
    def option_d(self):
        id = int(input('Digite el id que desea eliminar: '))
        Sellers().drop_seller_db(id)