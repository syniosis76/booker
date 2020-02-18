from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button

Builder.load_file('views/bookingListView.kv')

class BookingListView(Screen):
    def __init__(self, **kwargs):        
        super(BookingListView, self).__init__(**kwargs)                   
        self.version = 0

    def on_pre_enter(self):
        app = App.get_running_app()
        if app.data.hasUpdated(self.version):
            self.buildUi()
        self.listBookings()
        self.updateVersion = app.data.version  

    def buildUi(self):
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
                button = Button()
                button.booker_product = product.name
                button.booker_timeslot = timeslot.time                
                button.bind(on_press=self.buttonClick)
                self.bookings.add_widget(button)

    def listBookings(self):
        app = App.get_running_app()

        self.bookings = self.ids.bookings
        for widget in self.bookings.children:
            if isinstance(widget, Button):
                person = app.data.getBooking(widget.booker_product, widget.booker_timeslot)
                if person:
                    widget.text = person.name
                else:
                    widget.text = ''

    def buttonClick(self, instance):
        print('Booking button <%s> clicked.' % instance.text)
        app = App.get_running_app()
        app.data.currentProduct = instance.booker_product
        app.data.currentTimeslot = instance.booker_timeslot

        self.manager.transition.direction = 'left'
        self.manager.current = 'people'
    
    def productsButtonClick(self, instance):
        print('Booking button <%s> clicked.' % instance.text)
        self.manager.transition.direction = 'left'
        self.manager.current = 'products'
    