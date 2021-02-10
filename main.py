from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.uix.screenmanager import Screen
import sqlite3 as sql

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

    # conn = sql.connect('infouser.db')
    # cur = conn.cursor()
    # cur.execute(""" CREATE TABLE info (
    #         id INTEGER PRIMARY KEY AUTOINCREMENT,
    #         fname VARCHAR(50),
    #         height INT,
    #         weight INT,
    #         age INT,
    #         heartrate INT)
    #         """)
    # conn.commit()
    # conn.close()

    def save_data(self):
        conn = sql.connect('infouser.db')
        cur = conn.cursor()
        cur.execute(""" INSERT INTO info (fname,height,weight,age,heartrate) VALUES (?,?,?,?,?)""",
                    (self.root.ids.scr_mngr.get_screen('input').ids.fname.text,
                     self.root.ids.scr_mngr.get_screen('input').ids.height.text,
                     self.root.ids.scr_mngr.get_screen('input').ids.weight.text,
                     self.root.ids.scr_mngr.get_screen('input').ids.age.text,
                     self.root.ids.scr_mngr.get_screen('input').ids.heartrate.text))
        conn.commit()
        conn.close()

    def build(self):
        self.theme_cls.primary_palette = "Lime"
        self.theme_cls.theme_style = "Light"  # "Light"
        screen = Builder.load_file("main.kv")
        return screen

    def show_alert_dialog(self):
        close_button = MDFlatButton(text="Okay",
                                    on_release=self.okay)
        more_button = MDFlatButton(text="Cancel", on_press=self.close_dialog)

        self.dialog = MDDialog(title="Confirmation", text="Confirm Details?",
                               size_hint=(0.7, 1),
                               buttons=[close_button, more_button])
        self.dialog.open()

    def result_dialog(self):
        close_button = MDFlatButton(text="Okay", on_release=self.close_dialog)
        self.dialog = MDDialog(title="Where did we get the Results?",
                               text="Results are Determined based on the Details Given by the User",
                               size_hint=(0.7, 1),
                               buttons=[close_button])
        self.dialog.open()

    def hakdog(self):
        close_button = MDFlatButton(text="Okay", on_release=self.close_dialog)
        self.dialog = MDDialog(title="Resting Heart Rate",
                               text="Manual Heartbeat check can be used to determine if you have a normal heart rate for your age",
                               size_hint=(0.7, 1),
                               buttons=[close_button])
        self.dialog.open()

    def show_data(self, *args):
        if self.root.ids.scr_mngr.get_screen('input').ids.fname.text == "" \
                or self.root.ids.scr_mngr.get_screen('input').ids.height.text == "" \
                or self.root.ids.scr_mngr.get_screen('input').ids.weight.text == "" \
                or self.root.ids.scr_mngr.get_screen('input').ids.heartrate.text == "" \
                or self.root.ids.scr_mngr.get_screen('input').ids.age.text == "" \
                or self.root.ids.scr_mngr.get_screen('input').ids.heartrate.text == "":
            close_button = MDFlatButton(text="Okay", on_release=self.close_dialog)
            self.dialog = MDDialog(title="Invalid", text="No item added",
                                   size_hint=(0.7, 1), buttons=[close_button])
            self.dialog.open()
        else:
            self.show_alert_dialog()

    def okay(self, *args):
        print(self.root.ids.scr_mngr.get_screen('input').ids.fname.text),
        print(self.root.ids.scr_mngr.get_screen('input').ids.height.text),
        print(self.root.ids.scr_mngr.get_screen('input').ids.weight.text),
        print(self.root.ids.scr_mngr.get_screen('input').ids.age.text),
        print(self.root.ids.scr_mngr.get_screen('input').ids.heartrate.text)
        self.save_data()
        self.root.ids.scr_mngr.current = 'result'
        self.dialog.dismiss()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def history_screen(self, obj):
        self.root.ids.scr_mngr.current = 'history'
        self.root.ids.scr_mngr.transition.direction = "right"

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
