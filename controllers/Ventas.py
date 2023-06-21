from datetime import datetime
from controllers.Productos import Products
from controllers.Vendedor import Sellers
from validations.decorators import get_atributes

class Sales:
    _sales_db = {}
    def __init__(self, **kwargs):
        self.__id = self.get_id
        if len(kwargs) > 0:
            products = Products()
            seller = Sellers()
            self.__date = f"{kwargs.get('day')}/{kwargs.get('month')}/{kwargs.get('year')}"
            self.__date = str(datetime.strptime(self.__date, "%d/%m/%Y"))
            self.__id_product = kwargs.get('id_product') if products.request_id(kwargs.get('id_product')) else -1
            if self.__id_product == -1:
                raise Exception('El producto no existe')

            self.__cantidity = kwargs.get('cantidity')
            
            self.__id_seller = kwargs.get('id_seller') if seller.request_id(kwargs.get('id_seller')) else -1

            if self.__id_seller == -1:
                raise Exception('El vendedor no existe')
            
            self.validate_cantidity(self.__id_product, products, self.__cantidity)
            self.__set_atributes
            
    @property
    def get_id(self):
        keys = list(self._sales_db.keys())
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
        self._sales_db[id] = data
        print(f"Su id de venta es {id}")

    def verify_id(self, id_sale):
        if id_sale not in self._sales_db.keys():
            raise Exception('No existe dicho id')

    def change_atribute(self, id, atribute):
        match atribute:
            case 'date':
                d_i = lambda message: int(input(f"Ingrese el {message}: "))
                try:
                    fecha = datetime.strptime(f"{d_i('dia')}/{d_i('mes')}/{d_i('año')}", "%d/%m/%Y")
                    self._sales_db[id]['date'] = fecha
                    print('Se modifico la fecha correctamente')
                except Exception as e:
                    print(e)
            case 'id_product':
                id_product = int(input("Digite el id del producto a cambiar: "))
                if Products().request_id(id_product):
                    try:
                        product = Products()
                        cantidity = product._products_db[id_product]['cantidity']
                        cantidity_before = self._sales_db[id]['cantidity']
                        product_before = self._sales_db[id]['id_product']
                        if id_product == product_before:
                            raise Exception('Ese es el producto registrado')
                        if cantidity_before > cantidity:
                            raise Exception('La cantidad del nuevo produco es insuficiente')
                        Sales.validate_cantidity(id_product, product, cantidity)
                        # devolvemos las existencias
                        Products()._products_db[product_before]['cantidity'] += cantidity_before
                        self._sales_db[id]['id_product'] = id_product
                        # retiramos existencias del nuevo producto
                        Products()._products_db[id_product]['cantidity'] = cantidity - cantidity_before
                        print('Cambio exitoso')
                    except Exception as e:
                        print(e)
            case 'cantidity':
                try:
                    cantidity_new = int(input('Ingrese la nueva cantidad: '))
                    cantidity_before = self._sales_db[id]['cantidity']
                    product_current = self._sales_db[id]['id_product']
                    # retornamos la cantidad al producto
                    cantidity_stock = Products()._products_db[product_current]['cantidity'] + cantidity_before
                    if cantidity_stock >= cantidity_new:
                        Products()._products_db[product_current]['cantidity'] += cantidity_before
                        self._sales_db[id]['cantidity'] = cantidity_new
                        Products()._products_db[product_current]['cantidity'] -= cantidity_new
                        print('Cambio exitoso')
                    else:
                        raise Exception('Esa cantidad pasa el limite hasta en el stock')
                except Exception as e:
                    print(e)

            case 'id_seller':
                id_seller = int(input("Digite el id del vendedor a cambiar: "))
                if Sellers().request_id(id_seller):
                    self._sales_db[id]['id_seller'] = id_seller
                    print('Cambio exitoso')
                print('El id digitado no existe')
        
    @staticmethod
    def validate_cantidity(id_product, instrance_product: Products, cantidity):
        if cantidity <= 0:
            raise Exception("La cantidad debe ser mayor a cero.")
        cantidity_product = instrance_product.list_all_data().get(id_product).get('cantidity')
        if cantidity > cantidity_product:
            raise Exception('Verifique las existencias de ese producto, cambio no exitoso')
        instrance_product.list_all_data().get(id_product)['cantidity'] -= cantidity


    def show_data(self, **kwargs):
        organize_to = kwargs.get('filter')
        order_by = kwargs.get('order')
        for i, j in self._sales_db.items():
            if j.get(organize_to) == order_by:
                id_product = j.get('id_product')
                data_spanish = ['fecha', 'id producto', 'cantidad', 'id vendedor']
                values = j.values()
                structure = dict(zip(data_spanish, values))
                print(f"""\n
    id venta -> {i}
    {data_spanish[0]} -> {structure[data_spanish[0]]}
    {data_spanish[1]} -> {structure[data_spanish[1]]}
    {data_spanish[2]} -> {structure[data_spanish[2]]}
    {data_spanish[3]} -> {structure[data_spanish[3]]}
    total -> {Products()._products_db.get(id_product).get('unit_price') * j.get('cantidity')}
                """)