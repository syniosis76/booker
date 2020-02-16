from models.product import Product
from models.person import Person
from models.timeslot import Timeslot

class Data():    
    def __init__(self):
        self.products = []
        self.loadProducts()
        
        self.people = []
        self.loadPeople()

    def loadProducts(self):
        product = Product()
        product.name = 'Hitman XS'
        self.products.append(product)

        product = Product()
        product.name = 'Hitman S'
        self.products.append(product)

        product = Product()
        product.name = 'Hitman M'
        self.products.append(product)

        product = Product()
        product.name = 'Hitman L'
        self.products.append(product)

    def loadPeople(self):
        person = Person()
        person.name = 'Stacey Verner'
        person.nick_name = 'Stacey V'
        person.email_address = 'stacey@verner.co.nz'
        person.mobile_number = '021 074 7965'        
        self.people.append(person)

        person = Person()
        person.name = 'Anna Verner'
        person.nick_name = 'Anna V'
        person.email_address = 'anna@verner.co.nz'
        person.mobile_number = '021 298 4390'        
        self.people.append(person)