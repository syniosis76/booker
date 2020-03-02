from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

Builder.load_file('views/peopleListView.kv')

class PeopleListView(Screen):
    def __init__(self, **kwargs):
        super(PeopleListView, self).__init__(**kwargs)   
        self.popup = None
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

    def selectPerson(self, emailAddress):
        app = App.get_running_app()
        app.data.setBooking(app.data.currentProduct, app.data.currentTimeslot, emailAddress)

        self.manager.transition.direction = 'right'
        self.manager.current = 'bookings'

    def personButtonClick(self, instance):
        print('People button <%s> clicked.' % instance.text)

        self.selectPerson(instance.booker_email_address)        

    def addButtonClick(self, instance):
        print('People button <%s> clicked.' % instance.text)

        nameInput = TextInput()
        emailInput = TextInput()
        mobileInput = TextInput()
        addButton = Button(text='Add')
        addButton.bind(on_press=self.popupButtonClick)
        cancelButton = Button(text='Cancel')
        cancelButton.bind(on_press=self.popupButtonClick)

        content = GridLayout()
        content.cols = 2        
        content.add_widget(Label(text = 'Name'))
        content.add_widget(nameInput)
        content.add_widget(Label(text = 'Email'))
        content.add_widget(emailInput)
        content.add_widget(Label(text = 'Mobile'))
        content.add_widget(mobileInput)
        content.add_widget(addButton)
        content.add_widget(cancelButton)        

        self.popup = Popup(content=content, auto_dismiss=False)
        self.popup.nameInput = nameInput
        self.popup.emailInput = emailInput
        self.popup.mobileInput = mobileInput

        # open the popup
        self.popup.open()

    def cancelButtonClick(self, instance):
        print('People button <%s> clicked.' % instance.text)        

        self.manager.transition.direction = 'right'
        self.manager.current = 'bookings'

    def popupButtonClick(self, instance):
        if self.popup:
            popup = self.popup
            if instance.text == 'Add':
                app = App.get_running_app()
                app.data.addPerson(popup.nameInput.text, popup.emailInput.text, popup.mobileInput.text)
                app.data.setBooking(app.data.currentProduct, app.data.currentTimeslot, popup.emailInput.text)
                self.selectPerson(popup.emailInput.text)
                self.listPeople()
            popup.dismiss()
            self.popup = None