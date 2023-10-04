from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.video import Video
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
import main

class ScrollableField(BoxLayout):
    def __init__(self, title, content, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint_y = None
        self.height = Window.height / 6
        self.padding = [10, 0, 10, 0]
        with self.canvas:
            Color(0, 0, 0, 0.8)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_rect, size=self.update_rect)
        ####TITLE
        self.add_widget(Label(text=title, size_hint=(0.1, 0.2), font_size=16, color=[1, 1, 1, 1]))
        if content.endswith('.mp4'):
            with self.canvas:
                Color(0, 0, 0, 0.8)
                self.rect = Rectangle(pos=self.pos, size=self.size)
            self.bind(pos=self.update_rect, size=self.update_rect)
            video = Video(source=content, state='play', options={'allow_stretch': True})
            self.add_widget(video)
        else:
            with self.canvas:
                Color(47, 48, 69, 0.1)
                self.rect = Rectangle(pos=self.pos, size=self.size)
            self.bind(pos=self.update_rect, size=self.update_rect)
        ####CONTENT
            self.add_widget(Label(text=content, size_hint=(0.1, 0.8)))

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class ScrollablePage(ScrollView):
    def __init__(self, fields, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, 1)
        self.bar_width = 10
        self.do_scroll_x = False
        layout = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        for title, content in fields:
            field = ScrollableField(title=title, content=content)
            layout.add_widget(field)
        self.add_widget(layout)


class MyApp(App):
    def build(self):
        return ScrollablePage(fields=main.fields)


if __name__ == '__main__':
    MyApp().run()
