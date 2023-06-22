from menus.tienda_vendedor import SellerMenu
from menus.tienda_productos import ProductsMenu
from menus.tienda_ventas import SalesMenu

class Menu:
    def __init__(self):
        while True:
            try:
                letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'}
                self.seller
                give_option = input('Digite opción: ').lower()
                if give_option not in letters:
                    print('Opción no valida')
                    continue
                Menu.get_option_seller(give_option)
                Menu.get_option_product(give_option)
                Menu.get_option_sales(give_option)
            except Exception as e:
                print(e)
                break
    @property
    def seller(self):
        print("""
    a. Registrar vendedor.
    b. Listar vendedores.
    c. Modificar vendedor.
    d. Eliminar vendedor. 
    e. Registrar producto.
    f. Listar productos.
    g. Modificar productos.
    h. Eliminar productos. 
    i. Registrar venta.
    j. Modificar venta.
    k. filtrar por producto
    l. filtrar por fecha
    m. filtrar por vededor
    n. salir""")
    
    @staticmethod
    def get_option_seller(give_option):
        seller = SellerMenu()
        seller.set_option(give_option)
    
    @staticmethod
    def get_option_product(give_option):
        products = ProductsMenu()
        products.set_option(give_option)
    
    @staticmethod
    def get_option_sales(give_option):
        sales = SalesMenu()
        sales.set_option(give_option)

if __name__ == "__main__":
    menu = Menu()