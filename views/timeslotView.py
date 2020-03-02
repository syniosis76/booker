from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file('views/timeslotView.kv')

class TimeslotView(Screen):
    def __init__(self, **kwargs):
        super(TimeslotView, self).__init__(**kwargs)           

    def on_pre_enter(self):
        self.listTimeslots()

    def listTimeslots(self):
        app = App.get_running_app()
        timeslotsInput = self.ids.timeslotsInput        
        timeslotsInput.text = '\n'.join([timeslot.time for timeslot in app.data.timeslots])        

    def okButtonClick(self, instance):
        print('Timeslots button <%s> clicked.' % instance.text)

        app = App.get_running_app()
        
        timeslotsInput = self.ids.timeslotsInput        
        productList = timeslotsInput.text.split('\n')

        app.data.setTimeslots(productList)

        self.manager.transition.direction = 'right'
        self.manager.current = 'bookings'

    def cancelButtonClick(self, instance):
        print('Timeslots button <%s> clicked.' % instance.text)        

        self.manager.transition.direction = 'right'
        self.manager.current = 'bookings'
    