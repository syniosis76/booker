from models.product import Product
from models.person import Person
from models.timeslot import Timeslot
from models.booking import Booking
from datetime import datetime
import os.path
import pickle

class Data():    
  def __init__(self):
    self.filename = 'data.data'

    self.products = []
    self.people = []
    self.timeslots = []
    self.bookings = []
    
    self.version = 0
    self.currentTimeslot = None
    self.currentProduct = None 

    self.loadData()     

  def loadData(self):
    self.load()

    self.updateVersion()    

  def load(self):
    if os.path.exists(self.filename):
      with open(self.filename, 'rb') as filehandle:            
        data = pickle.load(filehandle)
        self.products = data['products']
        self.people = data['people']
        self.timeslots = data['timeslots']
        self.bookings = data['bookings']

  def save(self):
    data = {}
    data['products'] = self.products
    data['people'] = self.people
    data['timeslots'] = self.timeslots
    data['bookings'] = self.bookings

    with open(self.filename, 'wb') as filehandle:            
      pickle.dump(data, filehandle)

  def setProducts(self, products):
    self.products.clear()

    for productName in products:
      product = Product()
      product.name = productName
      self.products.append(product)
    
    self.updateVersion()

  def setTimeslots(self, timeslots):
    self.timeslots.clear()

    for timeslotTime in timeslots:
      timeslot = Timeslot(timeslotTime)
      self.timeslots.append(timeslot)
    
    self.updateVersion()

  def setPeople(self, people):    
    pass

  def getBooking(self, product, timeslot):
    booking = next((booking for booking in self.bookings if booking.product == product and booking.timeslot == timeslot), None)
    if booking:
      return next((person for person in self.people if person.email_address == booking.email_address), None)

    return None

  def setBooking(self, product, timeslot, email_address):
    booking = next((booking for booking in self.bookings if booking.product == product and booking.timeslot == timeslot), None)
    if booking:
      self.bookings.remove(booking)

    if email_address:
      booking = Booking()
      booking.product = product
      booking.timeslot = timeslot
      booking.email_address = email_address
      self.bookings.append(booking)

    self.save()    

  def updateVersion(self):
    self.version += 1
    self.save()

  def hasUpdated(self, version):
    return self.version > version

  def addPerson(self, name, emailAddress, mobileNumber):
    person = Person()
    person.name = name
    person.email_address = emailAddress
    person.mobile_number = mobileNumber
    self.people.append(person)

  def defaultProducts(self):
    if len(self.products) == 0:        
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