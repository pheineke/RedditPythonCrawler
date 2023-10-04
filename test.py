from kivy.app import App
from kivy.uix.image import AsyncImage
from kivy.uix.boxlayout import BoxLayout

class MyBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(AsyncImage(source='https://i.redd.it/cmmlfmiyv4sb1.jpg'))
class MyApp(App):
    def build(self):
        return MyBoxLayout()

if __name__ == '__main__':
    MyApp().run()
