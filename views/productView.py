from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file('views/productView.kv')

class ProductView(Screen):
    def __init__(self, **kwargs):
        super(ProductView, self).__init__(**kwargs)           

    def on_pre_enter(self):
        self.listProducts()

    def listProducts(self):
        app = App.get_running_app()
        productsInput = self.ids.productsInput        
        productsInput.text = '\n'.join([product.name for product in app.data.products])        

    def okButtonClick(self, instance):
        print('Products button <%s> clicked.' % instance.text)

        app = App.get_running_app()
        
        productsInput = self.ids.productsInput        
        productList = productsInput.text.split('\n')

        app.data.setProducts(productList)

        self.manager.transition.direction = 'right'
        self.manager.current = 'bookings'

    def cancelButtonClick(self, instance):
        print('Products button <%s> clicked.' % instance.text)        

        self.manager.transition.direction = 'right'
        self.manager.current = 'bookings'
    