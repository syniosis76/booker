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
from kivy.metrics import sp

Builder.load_file('views/peopleListView.kv')

def sizeCallback(obj, value):
    obj.text_size = (value[0] - sp(30), sp(20))

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
            button.background_color = [0.0, 0.435, 0.698, 1.0]
            button.markup = True
            button.text = '[b]' + person.name + '[/b]'
            button.booker_email_address = person.email_address
            button.bind(size = sizeCallback)
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
        addButton = Button(text='Add', background_color = [0.0, 0.435, 0.698, 1.0])
        addButton.bind(on_press=self.popupButtonClick)
        cancelButton = Button(text='Cancel', background_color = [0.0, 0.435, 0.698, 1.0])
        cancelButton.bind(on_press=self.popupButtonClick)

        content = GridLayout()
        content.cols = 1

        formGrid = GridLayout()
        formGrid.cols = 1

        formGrid.row_default_height = 30
        formGrid.row_force_default = True
        
        label = Label(text = 'Name')
        label.bind(size = sizeCallback)
        formGrid.add_widget(label)

        formGrid.add_widget(nameInput)
        
        label = Label(text = 'Email')
        label.bind(size = sizeCallback)
        formGrid.add_widget(label)

        formGrid.add_widget(emailInput)

        label = Label(text = 'Mobile')
        label.bind(size = sizeCallback)
        formGrid.add_widget(label)

        formGrid.add_widget(mobileInput)        

        buttonGrid = GridLayout()
        buttonGrid.cols = 2
        buttonGrid.size_hint_y = 0.2

        buttonGrid.add_widget(addButton)
        buttonGrid.add_widget(cancelButton) 

        content.add_widget(formGrid)
        content.add_widget(GridLayout()) # Spacer
        content.add_widget(buttonGrid)      

        self.popup = Popup(content=content, auto_dismiss=False)
        self.popup.title = 'Add Person'
        self.popup.size_hint = (0.8, 0.8)
        self.popup.nameInput = nameInput
        self.popup.emailInput = emailInput
        self.popup.mobileInput = mobileInput

        # open the popup
        self.popup.open()

    def clearButtonClick(self, instance):
        print('People button <%s> clicked.' % instance.text)        

        self.selectPerson(None)

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