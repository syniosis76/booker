from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

Builder.load_file('views/bookingListView.kv')

def sizeCallback(obj, value):
    obj.text_size = (value[0] - 30, 20)

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
        
        for productIndex in range(len(app.data.products)):
            product = app.data.products[productIndex]
            
            grid = GridLayout()
            grid.cols = 1

            headerGrid = GridLayout()
            headerGrid.cols = 3
            headerGrid.size_hint_y=0.1

            button = Button()
            button.background_normal = ''
            button.background_color = [0, 0, 0, 1]
            button.bind(on_press=self.previousButtonClick)
            if productIndex >= 1:
                button.text = '<  ' + app.data.products[productIndex - 1].name                                   
            headerGrid.add_widget(button)            

            label = Label()
            label.text = product.name            
            label.font_size = 24
            label.bold = True
            headerGrid.add_widget(label)

            button = Button()
            button.background_normal = ''
            button.background_color = [0, 0, 0, 1]
            button.bind(on_press=self.nextButtonClick)
            if productIndex < len(app.data.products) - 1:
                button.text = app.data.products[productIndex + 1].name + '  >'                                  
            headerGrid.add_widget(button)

            grid.add_widget(headerGrid)

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
                button.background_color = [0.0, 0.435, 0.698, 1.0]
                button.markup = True              
                button.halign = 'left'                                                
                button.bind(size = sizeCallback)
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
            if isinstance(widget, Button) and hasattr(widget, 'booker_product'):
                person = app.data.getBooking(widget.booker_product, widget.booker_timeslot)
                if person:
                    widget.text = widget.booker_timeslot + '    [b]' + person.name + '[/b]'
                    widget.background_color = [0.137, 0.658, 0.949, 1.0]
                else:
                    widget.text = widget.booker_timeslot
                    widget.background_color = [0.0, 0.435, 0.698, 1.0]
            else:
                self.listBookings(widget)

    def buttonClick(self, instance):
        print('Booking button <%s> clicked.' % instance.text)
        app = App.get_running_app()
        app.data.currentProduct = instance.booker_product
        app.data.currentTimeslot = instance.booker_timeslot

        self.manager.transition.direction = 'left'
        self.manager.current = 'people'
    
    def nextButtonClick(self, instance):
        carousel = self.ids.bookings
        carousel.load_next()

    def previousButtonClick(self, instance):
        carousel = self.ids.bookings
        carousel.load_previous()
    
    def productsButtonClick(self, instance):
        print('Booking button <%s> clicked.' % instance.text)
        self.manager.transition.direction = 'left'
        self.manager.current = 'products'

    def timeslotsButtonClick(self, instance):
        print('Booking button <%s> clicked.' % instance.text)
        self.manager.transition.direction = 'left'
        self.manager.current = 'timeslots'
    