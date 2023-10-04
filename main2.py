from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView  
from kivy.uix.label import Label
from kivy.uix.video import Video
from kivy.loader import Loader
from kivy.uix.image import AsyncImage
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
import getcontent

class ScrollableField(BoxLayout):
    def __init__(self, title, content, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint_y = None
        self.height = Window.height / 4
        self.padding = [10, 0, 10, 0]
        with self.canvas:
            Color(0, 0, 0, 0.8)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_rect, size=self.update_rect)
        ####TITLE
        title_label = Label(text=title, size_hint=(.00001, .00001), text_size=(self.width - self.padding[0] - self.padding[2], None))
        title_label.bind(size=title_label.setter('text_size'))
        self.add_widget(title_label)

        if content.endswith(('.mp4', '.gif', '.jpg', '.jpeg', '.png')):
            with self.canvas:
                Color(0, 0, 0, 0.8)
                self.rect = Rectangle(pos=self.pos, size=self.size)
            self.bind(pos=self.update_rect, size=self.update_rect)
            if content.endswith('.mp4'):
                video = Video(source=content, state='play', options={'allow_stretch': True})
                self.add_widget(video)
            else:
                image = AsyncImage(source=content,
                                   size_hint=(1, 1),
                                   size=(500,500),
                                   keep_ratio=True,
                                   allow_stretch=True)
                self.add_widget(image)
        else:
            with self.canvas:
                Color(47, 48, 69, 0.1)
                self.rect = Rectangle(pos=self.pos, size=self.size)
            self.bind(pos=self.update_rect, size=self.update_rect)
            content_label = Label(text=content, size_hint=(1, 0.8), text_size=(self.width - self.padding[0] - self.padding[2], None))
            content_label.bind(size=content_label.setter('text_size'))
            self.add_widget(content_label)

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
        return ScrollablePage(fields=getcontent.fields)


if __name__ == '__main__':
    MyApp().run()
