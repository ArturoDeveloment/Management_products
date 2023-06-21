from controllers.Ventas import Sales
from datetime import datetime

class Sales_menu:
    def set_option(self, option):
        match option:
            case 'i':
                self.option_i()
            case 'j':
                self.option_j()
            case 'k':
                self.option_k()
            case 'l':
                self.option_l()
            case 'm':
                self.option_m()
            case 'n':
                raise Exception('Adios')
    
    def option_i(self):
        try:
            print('\n')
            message = lambda key: input(f'Digite su {key}: ')
            data = dict([
                (key, int(message(key))) for key in ['dia', 'mes', 'año', 'id producto', 'cantidad', 'id vendedor']
            ])
            data = dict(zip(['day', 'month', 'year', 'id_product', 'cantidity', 'id_seller'], data.values()))
            sales = Sales(**data)
        except Exception as e:
            print(e)
    
    def option_j(self):
        try:
            id = int(input('Digite el id de la venta a modificar: '))
            Sales().verify_id(id)
            data = {1: 'fecha', 2: 'cantidad', 3: 'id producto', 4: 'id vendedor'}
            for key, value in data.items():
                print(f"{key} - {value}")
            option = (int(input('Digite opción: ')))
            data_modifier = data.get(option)
            if data_modifier == None:
                raise Exception('Opción no valida')
        except Exception as e:
            print(e)
            return None
        
        paramts = {'fecha': 'date', 'cantidad': 'cantidity', 'id producto': 'id_product', 'id vendedor': 'id_seller'}
        data_modifier = paramts.get(data_modifier)
        Sales().change_atribute(id, data_modifier)
    
    def option_k(self):
        # mostrar por producto
        id_products = int(input('Digite el id del producto: '))
        Sales().show_data(filter = 'id_product', order = id_products)
    
    def option_l(self):
        # mostrar por pfecha
        day = int(input('Ingrese el día: '))
        month = int(input('Ingrese el mes: '))
        year = int(input('Ingrese el año: '))
        try:
            date = datetime.strptime(f"{day}/{month}/{year}", "%d/%m/%Y")
            Sales().show_data(filter = 'date', order = str(date))
        except Exception as e:
            print(e)

    def option_m(self):
        id_seller = int(input('Digite el id del vendedor: '))
        Sales().show_data(filter = 'id_seller', order = id_seller)