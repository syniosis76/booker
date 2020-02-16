from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.uix.button import Button

Builder.load_file('views/peopleListView.kv')

class PeopleListView(Screen):
    def __init__(self, **kwargs):
        super(PeopleListView, self).__init__(**kwargs)
        Clock.schedule_once(lambda dt: self.prepare(), 0)        

    def prepare(self):
        print('Preparing PeopleListView...')

        self.listPeople()

    def listPeople(self):
        self.people = self.ids.people
        self.people.clear_widgets()

        app = App.get_running_app()

        for person in app.data.people:
            button = Button(text=person.name)
            button.bind(on_press=self.buttonClick)
            self.people.add_widget(button)

    def buttonClick(self, instance):
        print('People button <%s> clicked.' % instance.text)
        self.manager.transition.direction = 'right'
        self.manager.current = 'bookings'
    