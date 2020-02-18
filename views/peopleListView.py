from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

Builder.load_file('views/peopleListView.kv')

class PeopleListView(Screen):
    def __init__(self, **kwargs):
        super(PeopleListView, self).__init__(**kwargs)   
        self.listPeople()

    def on_pre_enter(self):
        pass

    def listPeople(self):
        people = self.ids.people  
        people.clear_widgets()

        app = App.get_running_app()

        sortedPeople = sorted(app.data.people, key=lambda person: person.name)
        for person in sortedPeople:
            button = Button()
            button.text = person.name
            button.booker_email_address = person.email_address
            button.bind(on_press=self.personButtonClick)
            people.add_widget(button)

        people.add_widget(FloatLayout())

    def personButtonClick(self, instance):
        print('People button <%s> clicked.' % instance.text)

        app = App.get_running_app()
        app.data.setBooking(app.data.currentProduct, app.data.currentTimeslot, instance.booker_email_address)

        self.manager.transition.direction = 'right'
        self.manager.current = 'bookings'

    def cancelButtonClick(self, instance):
        print('People button <%s> clicked.' % instance.text)        

        self.manager.transition.direction = 'right'
        self.manager.current = 'bookings'
    