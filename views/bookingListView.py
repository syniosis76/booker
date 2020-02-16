from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock

Builder.load_file('views/bookingListView.kv')

class BookingListView(Screen):
    def __init__(self, **kwargs):
        super(BookingListView, self).__init__(**kwargs)
        Clock.schedule_once(lambda dt: self.prepare(), 0)        

    def prepare(self):
        print('Preparing BookingListView...')

    def buttonClick(self, instance):
        print('Booking button <%s> clicked.' % instance.text)
        self.manager.transition.direction = 'left'
        self.manager.current = 'people'
    