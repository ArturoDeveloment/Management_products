from controllers.Productos import Products

class Products_menu:
    def set_option(self, give_option):
        match give_option:
            case 'e':
                self.option_e()
            case 'f':
                self.option_f()
            case 'g':
                self.option_g()
            case 'h':
                self.option_h()
    
    def option_e(self):
        try:
            print('\n')
            message = lambda key: input(f'Digite el {key} del producto: ')
            data = dict([
                (key, message(key) if key not in ['cantidad', 'precio unitario'] else int(message(key)) if key != 'precio unitario' else float(message(key))) for key in ['nombre', 'cantidad', 'precio unitario']
            ])
            data = dict(zip(['name', 'cantidity', 'unit_price'], data.values()))
            if data.get('name').isnumeric() or str(data.get('name')).isdigit() or str(data.get('name')).isdecimal():
                raise Exception('El nombre es un número')
            if not(data.get('name').replace(' ', '').isalpha()):
                raise Exception('Formato de nombre no es valido')
            if data.get('cantidity') < 0:
                raise ValueError("Cantidad no puede ser negativa")
            product = Products(**data)
        except Exception as e:
            print(e)
    
    def option_f(self):
        Products().get_db_products
        
    def option_g(self):
        id = int(input('Digite su id: '))
        data = {1: 'nombre', 2: 'cantidad', 3: 'precio unitario'}
        for key, value in data.items():
            print(f"{key} - {value}")
        try:
            option = (int(input('Digite opción: ')))
        except Exception as e:
            print(e)
            return None
        data_modifier = data.get(option)
        paramts = {'nombre': 'name', 'cantidad': 'cantidity', 'precio unitario': 'unit_price'}
        data_modifier = paramts.get(data_modifier)
        Products().change_atributes(id, data_modifier)
    
    def option_h(self):
        id = int(input('Digite el id que desea eliminar: '))
        Products().drop_products_db(id)