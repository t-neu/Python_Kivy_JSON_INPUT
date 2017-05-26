from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.storage.jsonstore import JsonStore
from kivy.uix.textinput import TextInput

store = JsonStore('save.json')

if store.exists('settings'):
    print('Settings exists:', store.get('settings'))
else:
    store.put('settings', currentSoundLevel='7', currentUsername='Aaron007', CurrentSeconds=90)


if store.exists('user'):
    print('User exists:', store.get('user'))
else:
    store.put('user', soundLevel='7', username='Default', seconds=90)

class Username(TextInput):

    def __init__(self,**kwargs):
        super(Username,self).__init__(**kwargs)
        self.text = store.get('user')['username']

    def insert_text(self, substring, from_undo=False):
        if(len(self.text) <= 12):
            s = substring
        else:
            s = ''
            root.ids.error.color = (1.0, 0.0, 0.0, 1.0)
        return super(Username, self).insert_text(s, from_undo=from_undo)


root = Builder.load_string('''

BoxLayout:
    orientation: 'vertical'
    Username:                        
        multiline: False
        size_hint: (.2, 1)
        foreground_color: (1.0, 1.0, 1.0, 1.0)
        background_color: (0.0, 0.0, 0.0, 1.0)
        id: username
    Label:
        text:'Only 12 Characters'
        size_hint: (.2, 1)                       
        font_size: '14sp'
        color: (1.0, 0.0, 0.0, 0.0)
        id: error
                
 ''')


class MyApp(App):

    def build(self):
        return root

MyApp().run()