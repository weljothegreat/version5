from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.uix.screenmanager import Screen, ScreenManager

Window.size = (300, 500)


class DemoApp(MDApp):
    class MainMenuScreen(Screen):
        pass

    class InputScreen(Screen):
        pass

    class RestingHeartRateScreen(Screen):
        pass

    class ResultScreen(Screen):
        pass

    class LocationSearchScreen(Screen):
        pass

    class LocationResultScreen(Screen):
        pass

    class HistoryScreen(Screen):
        pass

    sm = ScreenManager()
    sm.add_widget(MainMenuScreen(name="menu"))
    sm.add_widget(InputScreen(name="input"))
    sm.add_widget(RestingHeartRateScreen(name="heartrate"))
    sm.add_widget(ResultScreen(name="result"))
    sm.add_widget(LocationSearchScreen(name="locsearch"))
    sm.add_widget(LocationResultScreen(name="locresult"))
    sm.add_widget(HistoryScreen(name="history"))

    class ContentNavigationDrawer(BoxLayout):
        screen_manager = ObjectProperty()
        nav_drawer = ObjectProperty()

    class DrawerList(ThemableBehavior, MDList):
        pass

    def build(self):
        self.theme_cls.primary_palette = "Lime"
        screen = Builder.load_file("main.kv")
        return screen

    def show_alert_dialog(self):
        close_button = MDFlatButton(text="Okay",
                                    on_press=self.hatdog)
        more_button = MDFlatButton(text="Cancel", on_press=self.close_dialog)
        self.dialog = MDDialog(title="Confirmation", text="Confirm Details?",
                               size_hint=(0.7, 1),
                               buttons=[close_button, more_button])
        self.dialog.open()

    def result_dialog(self):
        close_button = MDFlatButton(text="Okay", on_release = self.close_dialog)
        self.dialog = MDDialog(title="Where did we get the Results?", text="Results are Determined based on the Details Given by the User",
                               size_hint=(0.7, 1),
                               buttons = [close_button])
        self.dialog.open()

    def hakdog(self):
        close_button = MDFlatButton(text="Okay", on_release=self.close_dialog)
        self.dialog = MDDialog(title="Resting Heart Rate",
                               text="Manual Heartbeat check can be used to determine if you have a normal heart rate for your age",
                               size_hint=(0.7, 1),
                               buttons=[close_button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def hatdog(self, obj):
        self.root.ids.scr_mngr.current = 'heartrate'
        self.dialog.dismiss()

    def history_screen(self, obj):
        self.root.ids.scr_mngr.current = 'history'
        self.root.ids.scr_mngr.transition.direction = "left"

    def location_screen(self, obj):
        self.root.ids.scr_mngr.current = 'locsearch'
        self.root.ids.scr_mngr.transition.direction = "left"

    def back_screen(self, obj):
        self.root.ids.scr_mngr.current = 'menu'
        self.root.ids.scr_mngr.transition.direction = "right"

    def back2_screen(self, obj):
        self.root.ids.scr_mngr.current = 'input'
        self.root.ids.scr_mngr.transition.direction = "right"

    def back3_screen(self, obj):
        self.root.ids.scr_mngr.current = 'menu'
        self.root.ids.scr_mngr.transition.direction = "right"

    def back4_screen(self, obj):
        self.root.ids.scr_mngr.current = 'locsearch'
        self.root.ids.scr_mngr.transition.direction = "right"

    def on_start(self):
        pass


DemoApp().run()
