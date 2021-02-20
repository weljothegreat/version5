from kivy.network.urlrequest import UrlRequest
from kivy.properties import  ListProperty
from kivy.event import EventDispatcher


class News(EventDispatcher):
    headlines = ListProperty([('Uninitialized', 'Uninitialized', 'No news is good news!')])

    def get_news(self, *args):
        url = ('http://newsapi.org/v2/top-headlines?'
               'country=ph&category=health&'
               'apiKey=0a2a06f5a843426ca8384f89111bfe99')
        req = UrlRequest(url, self._got_news, on_failure=self.fail, on_error=self.fail)

    def _got_news(self, req, news):
        print(news)
        self.headlines.clear()
        for content in news['articles']:
            self.headlines.append((content['title'], content['urlToImage'], content['description']))

    def fail(self, instance, value):
        print('you loose')
        print(f'Error: {instance}, {value}')


if __name__ == '__main__':
    from kivy.app import App
    from kivy.clock import Clock
    from kivy.lang import Builder
    from kivy.properties import StringProperty
    from kivy.uix.screenmanager import Screen
    from kivy.core.window import Window

    import itertools
    import pprint
    from textwrap import dedent
    kv = dedent("""
    <NewsScreen>:
        BoxLayout:
            orientation: 'vertical'
            Label:
                size_hint_y: .25
                text: root.headline
                text_size: self.size
                valign: 'center'
                halign: 'center'
                shorten: True
                shorten_from: 'right'
                font_size: 30
                padding: 20,20
                bold: True
            GridLayout:
                cols: 2
                padding: 20
                AsyncImage:
                    source: root.headline_image
                    anim_delay: .03334  # 15fps, for gif videos
                    nocache: True
                Label:
                    padding_x: 30
                    text: root.description
                    text_size: self.size
                    font_size: 25
                    valign: 'center'

    BoxLayout:  # This is the root widget
        orientation: 'vertical'
        ScreenManager:
            id: sm
            NewsScreen:
                name: 'news'
                next: 'weather'
                duration: 30
    """)


    class NewsScreen(Screen):
        headline = StringProperty('')
        headline_image = StringProperty('')
        description = StringProperty('')

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.app = App.get_running_app()
            self.story = itertools.cycle(self.app.news.headlines)
            Clock.schedule_once(self.initial_news, 5)
            self.refresh = Clock.schedule_interval(self.news_next, 15)

        def initial_news(self, *args):
            self.headline = self.app.news.headlines[0][0] if self.app.news.headlines[0][0] else 'junk'
            self.headline_image = self.app.news.headlines[0][1] if self.app.news.headlines[0][1] else 'junk'
            self.description = self.app.news.headlines[0][2] if self.app.news.headlines[0][2] else 'No Description'
            print(self.headline)

        def news_next(self, *args):
            n = next(self.story)
            self.headline = n[0]
            self.headline_image = n[1] if n[1] is not None else ''
            self.description = n[2]

        # def on_pre_enter(self, *args):
        #     self.refresh()  # start the news refresh schedule
        #
        # def on_leave(self, *args):
        #     self.refresh.cancel()  # cancel the schedule when we leave the screen


    class TestNewsApp(App):
        news = News()

        def build(self):
            Window.size = 1500, 303
            Window.top = 100
            Window.left = 10
            return Builder.load_string(kv)

        def on_start(self):
            self.news.get_news()
            Clock.schedule_once(self.print_news, 5)  # wait for site..
            print('waiting 5 seconds...')

        def print_news(self, dt):
            pp = pprint.PrettyPrinter(width=80, compact=True)
            pp.pprint(self.news.headlines)


    TestNewsApp().run()
