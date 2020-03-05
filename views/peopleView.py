from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file('views/peopleView.kv')

class PeopleView(Screen):
    def __init__(self, **kwargs):
        super(PeopleView, self).__init__(**kwargs)           

    def on_pre_enter(self):
        self.listPeople()

    def listPeople(self):
        app = App.get_running_app()
        peopleInput = self.ids.peopleInput        
        peopleInput.text = '\n'.join([person.toString() for person in app.data.people])        

    def okButtonClick(self, instance):
        print('People button <%s> clicked.' % instance.text)

        app = App.get_running_app()
        
        peopleInput = self.ids.peopleInput        
        peopleList = peopleInput.text.split('\n')

        app.data.setPeople(peopleList)

        self.manager.transition.direction = 'right'
        self.manager.current = 'bookings'

    def cancelButtonClick(self, instance):
        print('People button <%s> clicked.' % instance.text)        

        self.manager.transition.direction = 'right'
        self.manager.current = 'bookings'
    