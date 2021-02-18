from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import IRightBodyTouch, MDList
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelTwoLine
import json
import sqlite3 as sql
import datetime
import time
import requests



class Content(MDList):
    pass


class RecordLine(MDBoxLayout):
    text = StringProperty()


class InformationDialog(MDDialog):
    pass


class DemoApp(MDApp):
    class MainMenuScreen(Screen):
        pass

    class InputScreen(Screen):
        pass

    class RestingHeartRateScreen(Screen):
        pass

    class ResultObeseScreen(Screen):
        pass

    class ResultNormalScreen(Screen):
        pass

    class ResultOverweightScreen(Screen):
        pass

    class ResultUnderweightScreen(Screen):
        pass

    class LocationSearchScreen(Screen):
        pass

    class LocationResultScreen(Screen):
        pass

    class HistoryScreen(Screen):
        pass

    # conn = sql.connect('USERINFO.db')
    # cur = conn.cursor()
    # cur.execute(""" CREATE TABLE IF NOT EXISTS results (
    #             UID INTEGER PRIMARY KEY AUTOINCREMENT,
    #             NAME VARCHAR(50),
    #             RESULT INT,
    #             DATE_TIME TEXT DEFAULT CURRENT_TIMESTAMP)
    #          """)
    # cur.execute(""" CREATE TABLE IF NOT EXISTS information (
    #              id INTEGER PRIMARY KEY AUTOINCREMENT,
    #              fname  VARCHAR(50),
    #              height INT,
    #              weight INT,
    #              age INT,
    #              heartrate INT)
    #              """)
    # conn.commit()
    # conn.close()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.list_items = []  # Dictionary where the items is stored
        self.counter = 0
        self.counting = {'Item counter': self.counter}
        self.dialog = None
        self.selected_category = None
        self.selected_rec = None
        self.card_file = \
            [{'Category': 'Barangay ALABANG',
              'Record': [
                  {'title': 'Alabang Medical Clinic ( MAIN )',
                   'Details': [
                       ' ADDRESS: \n 297 Montillano St, Alabang, Muntinlupa \n TELEPHONE NUMBER: \n (02) 8842 0680']},
                  {'title': 'Alabang Medical Center, Alabang Zapote road',
                   'Details': [
                       ' ADDRESS: \n Ayala Life-FGU Center, Zapote Road Corner Acacia Avenue Madrigal Business Park, Ayala Alabang, Muntinlupa \n TELEPHONE NUMBER: \n 0998 855 9221']},
                  {'title': 'Asian Hospital and Medical Center',
                   'Details': [
                       ' ADDRESS: \n 2205 Civic Dr, Alabang, Muntinlupa \n TELEPHONE NUMBER: \n (02) 8771 9000']},
                  {'title': 'Aventus Medical Care, Inc. - Alabang Clinic',
                   'Details': [
                       ' ADDRESS: \n 2/F Sycamore ARCS 1 Building Buencamino Street corner Alabang - Zapote Road Madrigal Business Park, Alabang, Muntinlupa \n TELEPHONE NUMBER: \n (02) 8556 3598']},
                  {'title': 'Healthway Medical Festival Mall',
                   'Details': [
                       ' ADDRESS: \n 2nd Floor, Pixie Forest Entrance, Filinvest Ave, Filinvest City, Muntinlupa \n TELEPHONE NUMBER: \n (02) 751 4929']},
                  {'title': 'Healthfirst clinic ALABANG',
                   'Details': [
                       ' ADDRESS: \n G/F, South Supermarket, Filinvest Ave., Filinvest Corporate City  \n TELEPHONE NUMBER: \n (+632) 8 821 1423 | 0917 842 8214']},
                  {'title': 'Ospital ng Muntinlupa ( OSMUN )',
                   'Details': [
                       ' ADDRESS: \n Civic Dr, Alabang, Muntinlupa \n TELEPHONE NUMBER: \n (02) 8771 0457']},
                  {'title': 'St. Michaels Medical Center',
                   'Details': [
                       ' ADDRESS: \n Starmall Alabang, South Super Hwy, Alabang, Muntinlupa\n TELEPHONE NUMBER: \n 0921 624 4418']},
                  {'title': 'San Roque Medical Clinic',
                   'Details': [' ADDRESS: \n Alabang, Muntinlupa \n TELEPHONE NUMBER: \n (02) 8842 2950']},
                  {'title': 'Megason Diagnostic Clinic',
                   'Details': [' ADDRESS: \nAlabang, Muntinlupa \n TELEPHONE NUMBER: \n (02) 8809 9044']},
                  {'title': 'Tokyo Healthlink 東京ヘルスリンク - Alabang',
                   'Details': [
                       ' ADDRESS: \n Molito Complex, Madrigal Ave, Ayala Alabang, Muntinlupa \n TELEPHONE NUMBER: \n (02) 8772 2678']},
                  {'title': 'Research Institute for Tropical Medicine',
                   'Details': [
                       ' ADDRESS: \n Filinvest Corporate City, 9002 Research Dr, Alabang, Muntinlupa \n TELEPHONE NUMBER: \n (02) 8807 2631']},
              ]},
             {'Category': 'Barangay BAYANAN',
              'Record': [
                  {'title': 'Silverio Medical Clinic',
                   'Details': [
                       ' ADDRESS: \n 233g National Road, Muntinlupa \n TELEPHONE NUMBER: \n  (02) 8862 0223']},
                  {'title': 'Bayanan Health Center (Annex)',
                   'Details': [
                       ' ADDRESS: \n Block 2, Purok 1, 292 M Dolleton St, Muntinlupa \n TELEPHONE NUMBER: \n (02) 8862 0124']},
                  {'title': 'Bayanan Medical Clinic, X-Ray and Laboratory Services',
                   'Details': [
                       ' ADDRESS: \n 231 National Road, Bayanan, Muntinlupa \n TELEPHONE NUMBER: \n (02) 8861 5861']},
                  {'title': 'El Natividad Medical And Maternity Clinic',
                   'Details': [
                       ' ADDRESS: \n 214 National Road, Muntinlupa \n TELEPHONE NUMBER: \n 0923 701 5164']},
              ]},
             {'Category': 'Barangay CUPANG',
              'Record': [
                  {'title': 'Hillside General Hospital',
                   'Details': [
                       ' ADDRESS: \n Km. 23, West Service Road, Cupang, Muntinlupa \n TELEPHONE NUMBER: \n  (02) 8842 3958']},
                  {'title': 'Alabang Medical Center',
                   'Details': [
                       ' ADDRESS: \n 8 Corregidor, Cupang, Muntinlupa \n TELEPHONE NUMBER: \n (02) 8850 8719']},
                  {'title': 'Cupang Health Center',
                   'Details': [
                       ' ADDRESS: \n Barangay Hall, Beside Cupang, Manuel L. Quezon, Cupang, Muntinlupa \n TELEPHONE NUMBER: \n --']},
              ]},
             {'Category': 'Barangay POBLACION',
              'Record': [
                  {'title': 'Albia Medical & Diagnostic Clinic',
                   'Details': [
                       ' ADDRESS: \n 93 Rizal St, Poblacion, Muntinlupa \n TELEPHONE NUMBER: \n (02)8461204']},
                  {'title': 'Babaran Echavez Medical And Psychiatric Clinic',
                   'Details': [
                       ' ADDRESS: \n 1125 Amparo Corner Sto Nino Street, Poblacion, Muntinlupa \n TELEPHONE NUMBER: \n (02) 8861 3066']},
                  {'title': 'MCC De La Merced Maternity And Childrens Clinic',
                   'Details': [
                       ' ADDRESS: \n 92 Rizal St, Poblacion, Muntinlupa \n TELEPHONE NUMBER: \n (02) 8861 3944']},
                  {'title': 'Mauricestela Medical Clinic',
                   'Details': [
                       ' ADDRESS: \n 212 Pedro Diaz St, Poblacion, Muntinlupa, 1776 Metro Manila \n TELEPHONE NUMBER: \n (02) 8862 2117']},
                  {'title': 'Poblacion Health Center Main',
                   'Details': [
                       ' ADDRESS: \n Poblacion, Muntinlupa \n TELEPHONE NUMBER: \n NONE']},
              ]},
             {'Category': 'Barangay PUTATAN',
              'Record': [
                  {'title': 'Alabang Medical Clinic - Muntinlupa Branch',
                   'Details': [
                       ' ADDRESS: \n 1 National Highway, Putatan, Muntinlupa \n TELEPHONE NUMBER: \n (02) 8861 1779']},
                  {'title': 'IMS Wellth Care, Inc.',
                   'Details': [
                       ' ADDRESS: \n 49 National Road, Putatan, Muntinlupa \n TELEPHONE NUMBER: \n (02) 8861 1592']},
                  {'title': 'Medical Center Muntinlupa',
                   'Details': [
                       ' ADDRESS: \n National Road, Putatan, Muntinlupa \n TELEPHONE NUMBER: \n 8620162']},
                  {'title': 'Muntinlupa Doctors Clinic',
                   'Details': [
                       ' ADDRESS: \n 1 National Road, Putatan, Muntinlupa \n TELEPHONE NUMBER: \n (02) 8842 2718']},
                  {'title': 'Medcare Multi Specialty',
                   'Details': [
                       ' ADDRESS: \n 84-I, National Road, Barangay Putatan,  Muntinlupa \n TELEPHONE NUMBER: \n  0922 857 4180']},
              ]},
             {'Category': 'Barangay SUCAT',
              'Record': [
                  {'title': 'Sucat Health Center',
                   'Details': [
                       ' ADDRESS: \n 624 Dir. A. Bunye, Sucat, Muntinlupa \n TELEPHONE NUMBER: \n NONE']},
              ]},
             {'Category': 'Barangay TUNASAN',
              'Record': [
                  {'title': 'Beato-Cauilan Hospital',
                   'Details': [
                       ' ADDRESS: \n Manila S Rd, Tunasan, Muntinlupa \n TELEPHONE NUMBER: \n +632 861-5284']},
              ]}]

    def on_start(self):
        for category in self.card_file:
            panel = MDExpansionPanel(icon="scr2.png", content=Content(),
                                     panel_cls=MDExpansionPanelTwoLine(text=category['Category'],
                                                                       secondary_text="Tap to view Hospitals"))
            self.root.ids.scr_mngr.get_screen('locsearch').ids.rlist.add_widget(panel)
            for rec in category['Record']:
                rw = RecordLine(text=rec['title'])
                print(rec['title'])
                self.root.ids.scr_mngr.get_screen('locsearch').ids.rlist.children[0].content.add_widget(rw)

    def showinfo(self, cat, r):
        close_button = MDFlatButton(text="Done", on_release=self.close_dialog)
        ingredients = self.ingredients_list(cat, r)
        ingredients_text = ''
        for ingredient in ingredients:
            ingredients_text += ingredient
        self.dialog = InformationDialog(size_hint=(0.8, 0.8), text=ingredients_text, auto_dismiss=True,
                                        buttons=[close_button])
        self.dialog.open()

    def ingredients_list(self, selected_cat, selected_r):
        self.selected_rec = selected_r
        self.selected_category = selected_cat
        for category in self.card_file:
            if category['Category'] == selected_cat:
                for rec in category['Record']:
                    if rec['title'] == selected_r:
                        return rec['Details']

    def on_stop(self):  # Event handler that triggers when the application has finished running
        # Creates a json file to saved the all the items in dictionary when closing the app
        with open('saved_list.txt', 'w') as f:
            json.dump(self.list_items, f)

    class Container(IRightBodyTouch, MDBoxLayout):  # This line position widget to the right.
        adaptive_width = True

    def save_data(self):
        conn = sql.connect('USERINFO.db')
        cur = conn.cursor()
        cur.execute(""" INSERT INTO information (fname,height,weight,age,heartrate) VALUES (?,?,?,?,?)""",
                    (self.root.ids.scr_mngr.get_screen('input').ids.fname.text,
                     self.root.ids.scr_mngr.get_screen('input').ids.height.text,
                     self.root.ids.scr_mngr.get_screen('input').ids.weight.text,
                     self.root.ids.scr_mngr.get_screen('input').ids.age.text,
                     self.root.ids.scr_mngr.get_screen('input').ids.heartrate.text))
        conn.commit()
        conn.close()

    def news(self):
        url = ('http://newsapi.org/v2/top-headlines?'
               'country=ph&category=health&'
               'apiKey=0a2a06f5a843426ca8384f89111bfe99')
        response = requests.get(url)
        print(response.json())
        news_json = json.loads(response.text)

        count = 4

        for news in news_json['articles']:
            if count > 0:
                print(str(news['title']), '\n')
                print(str(news['description']), "\n")
                print(str(news['url']), "\n")
                print(str(news['urlToImage']), "\n")
                count -= 1

    def result_condition(self):
        n = int(10000)

        h = int(self.root.ids.scr_mngr.get_screen('input').ids.height.text)

        w = int(self.root.ids.scr_mngr.get_screen('input').ids.weight.text)

        unix = time.time()
        date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
        answer = (w / h / h) * n
        print(answer)

        conn = sql.connect('USERINFO.db')
        cur = conn.cursor()
        cur.execute(""" INSERT INTO results (NAME,RESULT,DATE_TIME) VALUES (?,?,?)""",
                    (
                        self.root.ids.scr_mngr.get_screen('input').ids.fname.text,
                        answer,
                        date
                    ))
        conn.commit()
        conn.close()
        if answer <= 18.5:
            self.root.ids.scr_mngr.current = 'underweight'
        elif 18.6 <= answer <= 24.9:
            self.root.ids.scr_mngr.current = 'normal'
        elif 25.0 <= answer <= 29.9:
            self.root.ids.scr_mngr.current = 'overweight'
        else:
            self.root.ids.scr_mngr.current = 'obese'

    def clear_inputs(self):  # set each of the inputs to an empty string
        self.root.ids.scr_mngr.get_screen('input').ids.fname.text = ""
        self.root.ids.scr_mngr.get_screen('input').ids.heartrate.text = ""
        self.root.ids.scr_mngr.get_screen('input').ids.age.text = ""
        self.root.ids.scr_mngr.get_screen('input').ids.height.text = ""
        self.root.ids.scr_mngr.get_screen('input').ids.weight.text = ""

    def info1_dialog(self):
        close_button = MDFlatButton(text="Okay", on_release=self.close_dialog)
        self.dialog = MDDialog(title="Details",
                               text="Hospitals listed are still operating up-to-date",
                               size_hint=(1, 1),
                               buttons=[close_button])
        self.dialog.open()

    def show_database(self):
        conn = sql.connect('USERINFO.db')
        cur = conn.cursor()
        cur.execute(""" 
        SELECT fname, height, weight, heartrate, RESULT, DATE_TIME
        FROM information INNER JOIN results
        ON information.id = results.UID
        """)
        output = cur.fetchall()
        for data in output:
            print(data)

    def build(self):
        self.theme_cls.primary_palette = "Lime"
        self.theme_cls.theme_style = "Light"  # "Light"
        screen = Builder.load_file("main.kv")
        return screen

    def back_screen6(self, obj):
        self.root.ids.scr_mngr.current = 'menu'
        self.root.ids.scr_mngr.transition.direction = "right"

    def show_alert_dialog(self):
        close_button = MDFlatButton(text="Okay",
                                    on_release=self.okay)
        more_button = MDFlatButton(text="Cancel", on_press=self.close_dialog)

        self.dialog = MDDialog(title="Confirmation", text="Confirm Details?",
                               size_hint=(1, 1),
                               buttons=[close_button, more_button])
        self.dialog.open()

    def result_dialog(self):
        close_button = MDFlatButton(text="Okay", on_release=self.close_dialog)
        self.dialog = MDDialog(title="Where did we get the Results?",
                               text="Results are Determined based on the Details Given by the User",
                               size_hint=(1, 1),
                               buttons=[close_button])
        self.dialog.open()

    def hakdog(self):
        close_button = MDFlatButton(text="Okay", on_release=self.close_dialog)
        self.dialog = MDDialog(title="Instructions",
                               text="Manual Heartbeat check can be used to determine if you have a normal heart rate for your age.                                                                                              "
                                    "If height = feet/inches, Convert to Centimeter (FEET× 30.48 +INCHES× 2.54) ",
                               size_hint=(1, 1),
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
                                   size_hint=(1, 1), buttons=[close_button])
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
        self.result_condition()
        self.clear_inputs()
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
        self.root.ids.scr_mngr.transition.direction = "left"

    def back2_screen(self, obj):
        self.root.ids.scr_mngr.current = 'input'
        self.root.ids.scr_mngr.transition.direction = "right"

    def back3_screen(self, obj):
        self.root.ids.scr_mngr.current = 'menu'
        self.root.ids.scr_mngr.transition.direction = "right"

    def back4_screen(self, obj):
        self.root.ids.scr_mngr.current = 'locsearch'
        self.root.ids.scr_mngr.transition.direction = "right"


DemoApp().run()