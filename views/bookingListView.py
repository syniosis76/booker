from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.button import Button

Builder.load_file('views/bookingListView.kv')

class BookingListView(Screen):
    def __init__(self, **kwargs):
        super(BookingListView, self).__init__(**kwargs)
        Clock.schedule_once(lambda dt: self.prepare(), 0)        

    def prepare(self):
        print('Preparing BookingListView...')

        self.listBookings()

    def listBookings(self):
        self.bookings = self.ids.bookings
        self.bookings.clear_widgets()

        app = App.get_running_app()

        self.bookings.cols = len(app.data.products) + 1
        self.bookings.add_widget(Label(text=''))
        for product in app.data.products:
            self.bookings.add_widget(Label(text=product.name))

        for timeslot in app.data.timeslots:
            self.bookings.add_widget(Label(text=timeslot.time))
            for product in app.data.products:
                person = app.data.getBooking(product, timeslot)
                button = Button()
                button.booker_product = product
                button.booker_timeslot = timeslot
                if person:
                    button.text = person.name
                button.bind(on_press=self.buttonClick)
                self.bookings.add_widget(button)

    def buttonClick(self, instance):
        print('Booking button <%s> clicked.' % instance.text)
        app = App.get_running_app()
        app.data.currentProduct = instance.booker_product
        app.data.currentTimeslot = instance.booker_timeslot

        self.manager.transition.direction = 'left'
        self.manager.current = 'people'
    