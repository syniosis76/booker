from models.product import Product
from models.person import Person
from models.timeslot import Timeslot
from models.booking import Booking
from datetime import datetime

class Data():    
    def __init__(self):
        self.products = []
        self.people = []
        self.timeslots = []
        self.bookings = []
        
        self.version = 0
        self.currentTimeslot = None
        self.currentProduct = None 

        self.loadData() 

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

    def loadTimeslots(self):
        timeslot = Timeslot()
        timeslot.time = '08:00'
        self.timeslots.append(timeslot)

        timeslot = Timeslot()
        timeslot.time = '08:30'
        self.timeslots.append(timeslot)

        timeslot = Timeslot()
        timeslot.time = '09:00'
        self.timeslots.append(timeslot)

    def loadBookings(self):
        self.bookings.clear()

        booking = Booking()
        booking.product = 'Hitman S'
        booking.timeslot = '08:00'
        booking.email_address = 'anna@verner.co.nz'
        self.bookings.append(booking)        

    def loadData(self):
        self.loadProducts()
        self.loadPeople()
        self.loadTimeslots()
        self.loadBookings()

        self.updateVersion()

    def getBooking(self, product, timeslot):
        booking = next((booking for booking in self.bookings if booking.product == product and booking.timeslot == timeslot), None)
        if booking:
          return next((person for person in self.people if person.email_address == booking.email_address), None)

        return None

    def setBooking(self, product, timeslot, email_address):
        booking = next((booking for booking in self.bookings if booking.product == product and booking.timeslot == timeslot), None)
        if booking:
            del(self.bookings, booking)

        booking = Booking()
        booking.product = product
        booking.timeslot = timeslot
        booking.email_address = email_address
        self.bookings.append(booking)

    def setProducts(self, products):
      self.products.clear()

      for productName in products:
        product = Product()
        product.name = productName
        self.products.append(product)
      
      self.updateVersion()

    def updateVersion(self):
      self.version += 1

    def hasUpdated(self, version):
      return self.version > version