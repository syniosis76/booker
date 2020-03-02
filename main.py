import kivy
kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager\

from models.data import Data

from views.bookingListView import BookingListView
from views.peopleListView import PeopleListView
from views.productView import ProductView
from views.timeslotView import TimeslotView

class BookerApp(App):    
    def build(self):
        self.data = Data()
        
        self.screenManager = ScreenManager()
        self.screenManager.add_widget(BookingListView(name='bookings'))
        self.screenManager.add_widget(PeopleListView(name='people')) 
        self.screenManager.add_widget(ProductView(name='products')) 
        self.screenManager.add_widget(TimeslotView(name='timeslots'))

        return self.screenManager

if __name__ == '__main__':
    BookerApp().run()