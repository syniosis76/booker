from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

Builder.load_file('views/bookingListView.kv')

class BookingListView(Screen):
    def __init__(self, **kwargs):        
        super(BookingListView, self).__init__(**kwargs)                   
        self.version = 0

    def on_pre_enter(self):
        app = App.get_running_app()
        if app.data.hasUpdated(self.version):
            self.buildUi()
        self.listBookings(self.ids.bookings)
        self.updateVersion = app.data.version  

    def buildUi(self):
        bookings = self.ids.bookings
        bookings.clear_widgets()        

        app = App.get_running_app()

        rowHeight = 40
        
        for product in app.data.products:
            grid = GridLayout()
            grid.cols = 1                       
            grid.add_widget(Label(text=product.name, size_hint_y=0.075))            

            scrollView = ScrollView()
            scrollView.do_scroll_x = False

            innerGrid = GridLayout()
            innerGrid.cols = 1								
            innerGrid.size_hint_y = None            
            innerGrid.row_default_height = rowHeight

            for timeslot in app.data.timeslots:                       
                button = Button()
                button.booker_product = product.name
                button.booker_timeslot = timeslot.time
                button.text = timeslot.time              
                button.bind(on_press = self.buttonClick)                
                innerGrid.add_widget(button)

            innerGrid.height = rowHeight * len(app.data.timeslots)
            scrollView.add_widget(innerGrid)
            grid.add_widget(scrollView)
            bookings.add_widget(grid)

        self.version = app.data.version          

    def listBookings(self, widgets):
        app = App.get_running_app()
        
        for widget in widgets.children:
            if isinstance(widget, Button):
                person = app.data.getBooking(widget.booker_product, widget.booker_timeslot)
                if person:
                    widget.text = widget.booker_timeslot + ' ' + person.name
                else:
                    widget.text = widget.booker_timeslot
            else:
                self.listBookings(widget)

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

    def timeslotsButtonClick(self, instance):
        print('Booking button <%s> clicked.' % instance.text)
        self.manager.transition.direction = 'left'
        self.manager.current = 'timeslots'
    