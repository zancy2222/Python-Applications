from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.core.window import Window
from kivymd.theming import ThemableBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivymd.theming import ThemeManager
from kivymd.uix.button import MDFloatingActionButtonSpeedDial, MDRectangleFlatButton, MDFloatingActionButton, \
    MDFillRoundFlatButton
from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty, BooleanProperty
from kivymd.uix.button import MDIconButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.card import MDCard
Window.size = (350, 580)

KV = '''
#:import NoTransition kivy.uix.screenmanager.NoTransition
MDFloatLayout:
    md_bg_color: 1, 1, 1, 1
    ScreenManager:
        id : scr
        name: 'screen_manager'
        transition: NoTransition()


#DITO_YUNG_SCREEN!!!

##################################################CASHIER FR -TYF ###########################################





        MDScreen:
            name: "login"


            Image:
                source: 'images/jildocs log in (1).png'
                pos_hint: {"center_x" :.5, "center_y": .7}


            MDLabel:
                text: "Login"
                pos_hint: {"center_x" :.16, "center_y": .74}
                font_size: "30sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Bold.otf" 
            MDLabel:
                text: "Please sign in to continue"
                pos_hint: {"center_x" :.28, "center_y": .69}
                font_size: "15sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, .4
                font_name: "fonts/LTSaeada-Regular.otf"

            MDTextField:
                mode: "line"
                hint_text: "Teacher's Number"
                line_color: 1, 1, 1, 0 
                pos_hint: {"center_x" :.5, "center_y": .5}
                line_width: 1.2
                size_hint: .7, .115
                icon_left: "school"
                font_name_hint_text: "fonts/LTSaeada-Regular.otf"

            MDTextField:
                mode: "line"
                hint_text: "Password"
                line_color: 1, 1, 1, 0 
                pos_hint: {"center_x" :.5, "center_y": .37}
                line_width: 1.2
                size_hint: .7, .115
                icon_left: "lock"
                font_name_hint_text: "fonts/LTSaeada-Regular.otf"

            MDRoundFlatIconButton:
                pos_hint: {"center_x" :.74, "center_y": .22}
                icon: "arrow-right"
                text: "Login"
                theme_text_color: "Custom"
                line_width: 1.06
                font_name: "fonts/LTSaeada-Regular.otf"
                text_color: 0, .1, .3, 1
                line_color: 0, .1, .3, 1
                theme_icon_color: "Custom"
                icon_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                radius: [20]
                elevation: 20



################################## BIODATA - FKK ###########################

        MDScreen:
            id: src6
            name: "ih"
            md_bg_color: 1,1,1,1 

            MDLabel:
                text: "PROGRAM"
                font_size: "25sp"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                halign: "center"   
                pos_hint: {"center_x" :.5, "center_y": .9}
                font_name: "fonts/LTSaeada-Regular.otf"
  
            MDCard:
                pos_hint: {"center_x" :.5, "center_y": .3}
                size_hint: .7, .15
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                ripple_behavior: True
                on_release:
                    scr.current = "grades"
                    
                FitImage:
                    pos_hint: {"center_x" :.5, "center_y": .5}
                    source: "images/class prog (2).png"
                    radius: 18,18,18,18





            MDCard:
                pos_hint: {"center_x" :.5, "center_y": .5}
                size_hint: .7, .15
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                ripple_behavior: True

                on_release:
                    scr.current = "teachers"
                FitImage:
                    pos_hint: {"center_x" :.5, "center_y": .5}
                    source: "images/TC.png"
                    radius: 18,18,18,18

            MDCard:
                pos_hint: {"center_x" :.5, "center_y": .7}
                size_hint: .7, .15
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                ripple_behavior: True

                FitImage:
                    pos_hint: {"center_x" :.5, "center_y": .5}
                    source: "images/org.png"
                    radius: 18,18,18,18

######################################################################################## TEACHERS FR ################################################
        MDScreen
            id: src5
            md_bg_color: 1,1,1,1
            name: "teachers"

            MDLabel:
                text: "Teachers"
                pos_hint: {"center_x" :.5, "center_y": .91}
                font_size: "20sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Regular.otf"

                

            MDFloatLayout:
            
                MDIconButton:
                    icon: "exit-to-app"
                    pos_hint: {"center_x" :.1, "center_y": .93}
                    icon_size: "20sp"
                    theme_icon_color: "Custom"
                    icon_color: app.theme_cls.primary_color
                    on_release:
                        scr.current = "ih"

                MDIconButton:
                    icon: "arrow-right"
                    pos_hint: {"center_x" :.94, "center_y": .93}
                    icon_size: "23sp"
                    theme_icon_color: "Custom"
                    icon_color: app.theme_cls.primary_color
                    on_release:
                        scr.current = "teachers2" 

                        
            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                pos_hint: {"center_x" :.25, "center_y": .80}
                size_hint: .4, .1
                ripple_behavior: True
                on_release:
                    scr.current = "teacher1"
                MDLabel:
                    text: "Ms. Dem Maglaque"
                    pos_hint: {"center_x" : 1, "center_y": .5}
                    font_size: "13sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1


            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                pos_hint: {"center_x" :.25, "center_y": .65}
                size_hint: .4, .1
                ripple_behavior: True
                on_release:
                    scr.current = "teacher2"
                MDLabel:
                    text: "Teacher 2"
                    pos_hint: {"center_x" : 1, "center_y": .5}
                    font_size: "13sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1

                    
            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                pos_hint: {"center_x" :.25, "center_y": .5}
                size_hint: .4, .1
                ripple_behavior: True
                on_release:
                    scr.current = "teacher3"
                MDLabel:
                    text: "Teacher 3"
                    pos_hint: {"center_x" : 1, "center_y": .5}
                    font_size: "13sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1

            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                pos_hint: {"center_x" :.25, "center_y": .35}
                size_hint: .4, .1
                ripple_behavior: True
                on_release:
                    scr.current = "teacher4"
                MDLabel:
                    text: "Teacher 4"
                    pos_hint: {"center_x" : 1, "center_y": .5}
                    font_size: "13sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                pos_hint: {"center_x" :.25, "center_y": .20}
                size_hint: .4, .1
                ripple_behavior: True
                on_release:
                    scr.current = "teacher5"
                MDLabel:
                    text: "Teacher 5"
                    pos_hint: {"center_x" : 1, "center_y": .5}
                    font_size: "13sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                pos_hint: {"center_x" :.75, "center_y": .80}
                size_hint: .4, .1  
                ripple_behavior: True
                on_release:
                    scr.current = "teacher6"
                MDLabel:
                    text: "Teacher 6"
                    pos_hint: {"center_x" : 1, "center_y": .5}
                    font_size: "13sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    
            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                pos_hint: {"center_x" :.75, "center_y": .65}
                size_hint: .4, .1  
                ripple_behavior: True  
                on_release:
                    scr.current = "teacher7"
                MDLabel:
                    text: "Teacher 7"
                    pos_hint: {"center_x" : 1, "center_y": .5}
                    font_size: "13sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1

 
            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                pos_hint: {"center_x" :.75, "center_y": .5}
                size_hint: .4, .1
                ripple_behavior: True
                on_release:
                    scr.current = "teacher8"
                MDLabel:
                    text: "Teacher 8"
                    pos_hint: {"center_x" : 1, "center_y": .5}
                    font_size: "13sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    
            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                pos_hint: {"center_x" :.75, "center_y": .35}
                size_hint: .4, .1
                ripple_behavior: True
                on_release:
                    scr.current = "teacher9"
                MDLabel:
                    text: "Teacher 9"
                    pos_hint: {"center_x" : 1, "center_y": .5}
                    font_size: "13sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                
            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                pos_hint: {"center_x" :.75, "center_y": .20}
                size_hint: .4, .1    
                ripple_behavior: True
                on_release:
                    scr.current = "teacher10"
                MDLabel:
                    text: "Teacher 10"
                    pos_hint: {"center_x" : 1, "center_y": .5}
                    font_size: "13sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1

                    

        MDScreen
            id: src5
            md_bg_color: 1,1,1,1
            name: "teachers2"

            MDLabel:
                text: "Teachers"
                pos_hint: {"center_x" :.5, "center_y": .91}
                font_size: "20sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Regular.otf"

                

            MDFloatLayout:
            
                MDIconButton:
                    icon: "exit-to-app"
                    pos_hint: {"center_x" :.1, "center_y": .93}
                    icon_size: "20sp"
                    theme_icon_color: "Custom"
                    icon_color: app.theme_cls.primary_color
                    on_release:
                        scr.current = "ih"

                MDIconButton:
                    icon: "arrow-right"
                    pos_hint: {"center_x" :.94, "center_y": .93}
                    icon_size: "23sp"
                    theme_icon_color: "Custom"
                    icon_color: app.theme_cls.primary_color
                    on_release:
                        scr.current = "teachers3" 
                MDIconButton:
                    icon: "arrow-left"
                    pos_hint: {"center_x" :.85, "center_y": .93}
                    icon_size: "23sp"
                    theme_icon_color: "Custom"
                    icon_color: app.theme_cls.primary_color
                    on_release:
                        scr.current = "teachers" 

                        
            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                pos_hint: {"center_x" :.25, "center_y": .80}
                size_hint: .4, .1
                ripple_behavior: True
                on_release:
                    scr.current = "teacher11"
                MDLabel:
                    text: "Teacher 11"
                    pos_hint: {"center_x" : 1, "center_y": .5}
                    font_size: "13sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1


            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                pos_hint: {"center_x" :.25, "center_y": .65}
                size_hint: .4, .1
                ripple_behavior: True
                on_release:
                    scr.current = "teacher12"
                MDLabel:
                    text: "Teacher 12"
                    pos_hint: {"center_x" : 1, "center_y": .5}
                    font_size: "13sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1

                    
            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                pos_hint: {"center_x" :.25, "center_y": .5}
                size_hint: .4, .1
                ripple_behavior: True
                on_release:
                    scr.current = "teacher13"
                MDLabel:
                    text: "Teacher 13"
                    pos_hint: {"center_x" : 1, "center_y": .5}
                    font_size: "13sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1

            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                pos_hint: {"center_x" :.25, "center_y": .35}
                size_hint: .4, .1
                ripple_behavior: True
                on_release:
                    scr.current = "teacher14"
                MDLabel:
                    text: "Teacher 14"
                    pos_hint: {"center_x" : 1, "center_y": .5}
                    font_size: "13sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                pos_hint: {"center_x" :.25, "center_y": .20}
                size_hint: .4, .1
                ripple_behavior: True
                on_release:
                    scr.current = "teacher15"
                MDLabel:
                    text: "Teacher 15"
                    pos_hint: {"center_x" : 1, "center_y": .5}
                    font_size: "13sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                pos_hint: {"center_x" :.75, "center_y": .80}
                size_hint: .4, .1  
                ripple_behavior: True
                on_release:
                    scr.current = "teacher16"
                MDLabel:
                    text: "Teacher 16"
                    pos_hint: {"center_x" : 1, "center_y": .5}
                    font_size: "13sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    
            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                pos_hint: {"center_x" :.75, "center_y": .65}
                size_hint: .4, .1  
                ripple_behavior: True  
                on_release:
                    scr.current = "teacher17"
                MDLabel:
                    text: "Teacher 17"
                    pos_hint: {"center_x" : 1, "center_y": .5}
                    font_size: "13sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1

 
            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                pos_hint: {"center_x" :.75, "center_y": .5}
                size_hint: .4, .1
                ripple_behavior: True
                on_release:
                    scr.current = "teacher18"
                MDLabel:
                    text: "Teacher 18"
                    pos_hint: {"center_x" : 1, "center_y": .5}
                    font_size: "13sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    
            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                pos_hint: {"center_x" :.75, "center_y": .35}
                size_hint: .4, .1
                ripple_behavior: True
                on_release:
                    scr.current = "teacher19"
                MDLabel:
                    text: "Teacher 19"
                    pos_hint: {"center_x" : 1, "center_y": .5}
                    font_size: "13sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                
            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                pos_hint: {"center_x" :.75, "center_y": .20}
                size_hint: .4, .1    
                ripple_behavior: True
                on_release:
                    scr.current = "teacher10"
                MDLabel:
                    text: "Teacher 20"
                    pos_hint: {"center_x" : 1, "center_y": .5}
                    font_size: "13sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1

        MDScreen
            id: src5
            md_bg_color: 1,1,1,1
            name: "teachers3"

            MDLabel:
                text: "Teachers"
                pos_hint: {"center_x" :.5, "center_y": .91}
                font_size: "20sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Regular.otf"

                

            MDFloatLayout:
            
                MDIconButton:
                    icon: "exit-to-app"
                    pos_hint: {"center_x" :.1, "center_y": .93}
                    icon_size: "20sp"
                    theme_icon_color: "Custom"
                    icon_color: app.theme_cls.primary_color
                    on_release:
                        scr.current = "ih"


                MDIconButton:
                    icon: "arrow-left"
                    pos_hint: {"center_x" :.85, "center_y": .93}
                    icon_size: "23sp"
                    theme_icon_color: "Custom"
                    icon_color: app.theme_cls.primary_color
                    on_release:
                        scr.current = "teachers2" 

                        
            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                pos_hint: {"center_x" :.25, "center_y": .80}
                size_hint: .4, .1
                ripple_behavior: True
                on_release:
                    scr.current = "teacher21"
                MDLabel:
                    text: "Teacher 21"
                    pos_hint: {"center_x" : 1, "center_y": .5}
                    font_size: "13sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1


            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                pos_hint: {"center_x" :.25, "center_y": .65}
                size_hint: .4, .1
                ripple_behavior: True
                on_release:
                    scr.current = "teacher22"
                MDLabel:
                    text: "Teacher 22"
                    pos_hint: {"center_x" : 1, "center_y": .5}
                    font_size: "13sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1

                    
            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                pos_hint: {"center_x" :.25, "center_y": .5}
                size_hint: .4, .1
                ripple_behavior: True
                on_release:
                    scr.current = "teacher23"
                MDLabel:
                    text: "Teacher 23"
                    pos_hint: {"center_x" : 1, "center_y": .5}
                    font_size: "13sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1

            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                pos_hint: {"center_x" :.25, "center_y": .35}
                size_hint: .4, .1
                ripple_behavior: True
                on_release:
                    scr.current = "teacher24"
                MDLabel:
                    text: "Teacher 24"
                    pos_hint: {"center_x" : 1, "center_y": .5}
                    font_size: "13sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                pos_hint: {"center_x" :.25, "center_y": .20}
                size_hint: .4, .1
                ripple_behavior: True
                on_release:
                    scr.current = "teacher25"
                MDLabel:
                    text: "Teacher 25"
                    pos_hint: {"center_x" : 1, "center_y": .5}
                    font_size: "13sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                pos_hint: {"center_x" :.75, "center_y": .80}
                size_hint: .4, .1  
                ripple_behavior: True
                on_release:
                    scr.current = "teacher26"
                MDLabel:
                    text: "Teacher 26"
                    pos_hint: {"center_x" : 1, "center_y": .5}
                    font_size: "13sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    
            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                pos_hint: {"center_x" :.75, "center_y": .65}
                size_hint: .4, .1  
                ripple_behavior: True  
                on_release:
                    scr.current = "teacher27"
                MDLabel:
                    text: "Teacher 27"
                    pos_hint: {"center_x" : 1, "center_y": .5}
                    font_size: "13sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1

 
            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                pos_hint: {"center_x" :.75, "center_y": .5}
                size_hint: .4, .1
                ripple_behavior: True
                on_release:
                    scr.current = "teacher28"
                MDLabel:
                    text: "Teacher 28"
                    pos_hint: {"center_x" : 1, "center_y": .5}
                    font_size: "13sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    
            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                pos_hint: {"center_x" :.75, "center_y": .35}
                size_hint: .4, .1
                ripple_behavior: True
                on_release:
                    scr.current = "teacher29"
                MDLabel:
                    text: "Teacher 29"
                    pos_hint: {"center_x" : 1, "center_y": .5}
                    font_size: "13sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                
            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                pos_hint: {"center_x" :.75, "center_y": .20}
                size_hint: .4, .1    
                ripple_behavior: True
                on_release:
                    scr.current = "teacher30"
                MDLabel:
                    text: "Teacher 30"
                    pos_hint: {"center_x" : 1, "center_y": .5}
                    font_size: "13sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1




####################################### LEVEL - JJJ #############################



        MDScreen
            id: src5
            md_bg_color: 1,1,1,1
            name: "grades"
            
            MDLabel:
                text: "Grade level"
                pos_hint: {"center_x" :.5, "center_y": .91}
                font_size: "20sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Regular.otf"
         

            MDFloatLayout:
                MDIconButton:
                    icon: "arrow-left"
                    pos_hint: {"center_x" :.1, "center_y": .93}
                    icon_size: "20sp"
                    theme_icon_color: "Custom"
                    icon_color: app.theme_cls.primary_color
                    on_release:
                        scr.current = "ih"
            MDCard:
                pos_hint: {"center_x" :.5, "center_y": .7}
                size_hint: .8, .3
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                ripple_behavior: True
                on_release:
                    scr.current = "grade11"
                MDLabel:
                    text: "Grade 11"
                    font_size: "17sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center" 
                    font_name: "fonts/LTSaeada-Regular.otf"
  
            MDCard:
                pos_hint: {"center_x" :.5, "center_y": .3}
                size_hint: .8, .3
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                ripple_behavior: True
                on_release:
                    scr.current = "grade12"
                MDLabel:
                    text: "Grade 12"
                    font_size: "17sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center" 
                    font_name: "fonts/LTSaeada-Regular.otf"
  
                


    

########################################################### GRADE 11 STRANDS - FFF ##########################
        MDScreen
            id: src5
            md_bg_color: 1,1,1,1
            name: "grade11"
    
            MDLabel:
                text: "Grade 11 Strands"
                pos_hint: {"center_x" :.5, "center_y": .87}
                font_size: "20sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Regular.otf"
  

            MDFloatLayout:
            
                MDIconButton:
                    icon: "arrow-left"
                    pos_hint: {"center_x" :.1, "center_y": .93}
                    icon_size: "20sp"
                    theme_icon_color: "Custom"
                    icon_color: app.theme_cls.primary_color
                    on_release:
                        scr.current = "grades"
                MDCard:
                    pos_hint: {"center_x" :.25, "center_y": .39}
                    size_hint: .4, .2
                    line_color: 0, .1, .3, 1
                    md_bg_color: 1,.839215, 0, .7
                    line_width: 1.2
                    ripple_behavior: True
                    on_release:
                        scr.current = "11stem"
                    FitImage:
                        source: "images/STEM (2).png"
                        pos_hint: {"center_x" :.5, "center_y": .5}
                        size_hint: 1,1
                        radius: 18,18,18,18

                    
                


            MDCard:
                pos_hint: {"center_x" :.25, "center_y": .65}
                size_hint: .4, .2
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                ripple_behavior: True
                on_release:
                    scr.current = "11abm"
                FitImage:
                    source: "images/ABM (1).png"
                    pos_hint: {"center_x" :.5, "center_y": .5}
                    size_hint: 1,1
                    radius: 18,18,18,18
      
                    

            MDCard:
                pos_hint: {"center_x" :.75, "center_y": .39}
                size_hint: .4, .2
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                ripple_behavior: True
                on_release:
                    scr.current = "11tvl"
                FitImage:
                    source: "images/TVL (1).png"
                    pos_hint: {"center_x" :.5, "center_y": .5}
                    size_hint: 1,1
                    radius: 18,18,18,18
                    
                
            MDCard:
                pos_hint: {"center_x" :.75, "center_y": .65}
                size_hint: .4, .2
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                ripple_behavior: True
                on_release:
                    scr.current = "11humss"
                FitImage:
                    source: "images/HUMSS (1).png"
                    pos_hint: {"center_x" :.5, "center_y": .5}
                    size_hint: 1,1
                    radius: 18,18,18,18
############################################################################ 11 TVL SECTIONS #####################################################
        MDScreen
            id: src5
            md_bg_color: 1,1,1,1
            name: "11tvl"
            MDLabel:
                text: "Grade 11 TVL"
                pos_hint: {"center_x" :.5, "center_y": .91}
                font_size: "20sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                

            MDFloatLayout:
            
                MDIconButton:
                    icon: "arrow-left"
                    pos_hint: {"center_x" :.1, "center_y": .93}
                    icon_size: "20sp"
                    theme_icon_color: "Custom"
                    icon_color: app.theme_cls.primary_color
                    on_release:
                        scr.current = "grade11"
                        
            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                pos_hint: {"center_x" :.25, "center_y": .80}
                size_hint: .4, .1
                ripple_behavior: True
                on_release:
                    scr.current = "11tvla"
                MDLabel:
                    text: "TVL A"
                    pos_hint: {"center_x" : 1, "center_y": .5}
                    font_size: "13sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1


            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                pos_hint: {"center_x" :.25, "center_y": .65}
                size_hint: .4, .1
                ripple_behavior: True
                on_release:
                    scr.current = "11tvlb"
                MDLabel:
                    text: "TVL B"
                    pos_hint: {"center_x" : 1, "center_y": .5}
                    font_size: "13sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1

                    
            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                pos_hint: {"center_x" :.25, "center_y": .5}
                size_hint: .4, .1
                ripple_behavior: True
                on_release:
                    scr.current = "11tvlc"
                MDLabel:
                    text: "TVL C"
                    pos_hint: {"center_x" : 1, "center_y": .5}
                    font_size: "13sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1

            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                pos_hint: {"center_x" :.25, "center_y": .35}
                size_hint: .4, .1
                ripple_behavior: True
                on_release:
                    scr.current = "11tvld"
                MDLabel:
                    text: "TVL D"
                    pos_hint: {"center_x" : 1, "center_y": .5}
                    font_size: "13sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
            #MDCard:
                #line_color: 0, .1, .3, 1
                #md_bg_color: 1,.839215, 0, .7
                #line_width: 1.2
                #pos_hint: {"center_x" :.25, "center_y": .20}
                #size_hint: .4, .1
                #ripple_behavior: True
                #on_release:
                    #scr.current = "11tvle"
                #MDLabel:
                    #text: "TVL E"
                    #pos_hint: {"center_x" : 1, "center_y": .5}
                    #font_size: "13sp"
                    #halign: "center"
                    #theme_text_color: "Custom"
                    #text_color: 0, .1, .3, 1


###################################################### program #####################################################


##################################### ANNOUNCEMENTS FR FRRRRRRRRR ##################

        MDScreen:
            name: "announcements"
            md_bg_color: 1,1,1,1

            MDLabel:
                text: "Announcements"
                pos_hint: {"center_x" :.5, "center_y": .9}
                font_size: "20sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Bold.otf" 

            MDIconButton:
                icon: "calendar"
                theme_icon_color: "Custom"
                icon_color: 0, .1, .3, 1
                pos_hint: {"center_x": .07, "center_y": .96}
                on_release:
                    scr.current = "favorite"

            MDIconButton:
                icon: "arrow-right"
                theme_icon_color: "Custom"
                icon_color: 0, .1, .3, 1
                pos_hint: {"center_x": .93, "center_y": .96}
                on_release:
                    scr.current = "announcements_2"
 
            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: "white"
                line_width: 1.2
                pos_hint: {"center_x" :.5, "center_y": .7}
                size_hint: .7, .25
                ripple_behavior: True
                radius: [0]
                on_release:
                    scr.current = "textannouncement1"


            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: "white"
                line_width: 1.2
                pos_hint: {"center_x" :.5, "center_y": .4}
                size_hint: .7, .25
                ripple_behavior: True
                radius: [0]
                on_release: 
                    scr.current = "textannouncement2"

        MDScreen:
            name: "announcements_2"
            md_bg_color: 1,1,1,1

            MDLabel:
                text: "Announcements"
                pos_hint: {"center_x" :.5, "center_y": .9}
                font_size: "20sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Bold.otf" 

            MDIconButton:
                icon: "calendar"
                theme_icon_color: "Custom"
                icon_color: 0, .1, .3, 1
                pos_hint: {"center_x": .07, "center_y": .96}
                on_release:
                    scr.current = "favorite"

            MDIconButton:
                icon: "arrow-left"
                theme_icon_color: "Custom"
                icon_color: 0, .1, .3, 1
                pos_hint: {"center_x": .78, "center_y": .96}
                on_release:
                    scr.current = "announcements"

            MDIconButton:
                icon: "arrow-right"
                theme_icon_color: "Custom"
                icon_color: 0, .1, .3, 1
                pos_hint: {"center_x": .93, "center_y": .96}
                on_release:
                    scr.current = "announcements_3"
 
            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: "white"
                line_width: 1.2
                pos_hint: {"center_x" :.5, "center_y": .7}
                size_hint: .7, .25
                ripple_behavior: True
                radius: [0]
                on_release: 
                    scr.current = "textannouncement3"

            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: "white"
                line_width: 1.2
                pos_hint: {"center_x" :.5, "center_y": .4}
                size_hint: .7, .25
                ripple_behavior: True
                radius: [0]
                on_release: 
                    scr.current = "textannouncement4"
            MDLabel:
                text: "2"
                pos_hint: {"center_x" :.5, "center_y": .15}
                font_size: "20sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Bold.otf" 


        MDScreen:
            name: "announcements_3"
            md_bg_color: 1,1,1,1

            MDLabel:
                text: "Announcements"
                pos_hint: {"center_x" :.5, "center_y": .9}
                font_size: "20sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Bold.otf" 

            MDIconButton:
                icon: "calendar"
                theme_icon_color: "Custom"
                icon_color: 0, .1, .3, 1
                pos_hint: {"center_x": .07, "center_y": .96}
                on_release:
                    scr.current = "favorite"

            MDIconButton:
                icon: "arrow-left"
                theme_icon_color: "Custom"
                icon_color: 0, .1, .3, 1
                pos_hint: {"center_x": .78, "center_y": .96}
                on_release:
                    scr.current = "announcements_2"

            MDIconButton:
                icon: "arrow-right"
                theme_icon_color: "Custom"
                icon_color: 0, .1, .3, 1
                pos_hint: {"center_x": .93, "center_y": .96}
                on_release:
                    scr.current = "announcements_4"
 
            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: "white"
                line_width: 1.2
                pos_hint: {"center_x" :.5, "center_y": .7}
                size_hint: .7, .25
                ripple_behavior: True
                radius: [0]
                on_release: 
                    scr.current = "textannouncement5"

            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: "white"
                line_width: 1.2
                pos_hint: {"center_x" :.5, "center_y": .4}
                size_hint: .7, .25
                ripple_behavior: True
                radius: [0]
                on_release: 
                    scr.current = "textannouncement6"
            MDLabel:
                text: "3"
                pos_hint: {"center_x" :.5, "center_y": .15}
                font_size: "20sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Bold.otf" 


        MDScreen:
            name: "announcements_4"
            md_bg_color: 1,1,1,1

            MDLabel:
                text: "Announcements"
                pos_hint: {"center_x" :.5, "center_y": .9}
                font_size: "20sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Bold.otf" 

            MDIconButton:
                icon: "calendar"
                theme_icon_color: "Custom"
                icon_color: 0, .1, .3, 1
                pos_hint: {"center_x": .07, "center_y": .96}
                on_release:
                    scr.current = "favorite"

            MDIconButton:
                icon: "arrow-left"
                theme_icon_color: "Custom"
                icon_color: 0, .1, .3, 1
                pos_hint: {"center_x": .78, "center_y": .96}
                on_release:
                    scr.current = "announcements_3"

            MDIconButton:
                icon: "arrow-right"
                theme_icon_color: "Custom"
                icon_color: 0, .1, .3, 1
                pos_hint: {"center_x": .93, "center_y": .96}
                on_release:
                    scr.current = "announcements_5"
 
            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: "white"
                line_width: 1.2
                pos_hint: {"center_x" :.5, "center_y": .7}
                size_hint: .7, .25
                ripple_behavior: True
                radius: [0]
                on_release: 
                    scr.current = "textannouncement7"

            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: "white"
                line_width: 1.2
                pos_hint: {"center_x" :.5, "center_y": .4}
                size_hint: .7, .25
                ripple_behavior: True
                radius: [0]
                on_release: 
                    scr.current = "textannouncement8"
            MDLabel:
                text: "4"
                pos_hint: {"center_x" :.5, "center_y": .15}
                font_size: "20sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Bold.otf" 



        MDScreen:
            name: "announcements_5"
            md_bg_color: 1,1,1,1

            MDLabel:
                text: "Announcements"
                pos_hint: {"center_x" :.5, "center_y": .9}
                font_size: "20sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Bold.otf" 

            MDIconButton:
                icon: "calendar"
                theme_icon_color: "Custom"
                icon_color: 0, .1, .3, 1
                pos_hint: {"center_x": .07, "center_y": .96}
                on_release:
                    scr.current = "favorite"

            MDIconButton:
                icon: "arrow-left"
                theme_icon_color: "Custom"
                icon_color: 0, .1, .3, 1
                pos_hint: {"center_x": .78, "center_y": .96}
                on_release:
                    scr.current = "announcements_4"

            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: "white"
                line_width: 1.2
                pos_hint: {"center_x" :.5, "center_y": .7}
                size_hint: .7, .25
                ripple_behavior: True
                radius: [0]
                on_release: 
                    scr.current = "textannouncement9"

            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: "white"
                line_width: 1.2
                pos_hint: {"center_x" :.5, "center_y": .4}
                size_hint: .7, .25
                ripple_behavior: True
                radius: [0]
                on_release: 
                    scr.current = "textannouncement10"

            MDLabel:
                text: "5"
                pos_hint: {"center_x" :.5, "center_y": .15}
                font_size: "20sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Bold.otf" 


####################################################### TEXT FIELDS FOR ANNOUNCEMENTS ##################################
        MDScreen:
            name: "textannouncement1"
            md_bg_color: 1,1,1,1
            MDLabel:
                text: "Announcement #1"
                font_size: "26sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"


            MDTextField:
                id: announcement1
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                multiline: True

            MDIconButton:
                icon: "check"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "announcements"     
        MDScreen:
            name: "textannouncement2"
            md_bg_color: 1,1,1,1
            MDLabel:
                text: "Announcement #2"
                font_size: "26sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"


            MDTextField:
                id: announcement2
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                multiline: True
            MDIconButton:
                icon: "check"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "announcements"    

        MDScreen:
            name: "textannouncement3"
            md_bg_color: 1,1,1,1
            MDLabel:
                text: "Announcement #3"
                font_size: "26sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"



            MDTextField:
                id: announcement3
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                multiline: True
            MDIconButton:
                icon: "check"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "announcements_2"     
        MDScreen:
            name: "textannouncement4"
            md_bg_color: 1,1,1,1
            MDLabel:
                text: "Announcement #4"
                font_size: "26sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"


            MDTextField:
                id: announcement4
                mode: "rectangle"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                multiline: True

            MDIconButton:
                icon: "check"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "announcements_2"    

        MDScreen:
            name: "textannouncement5"
            md_bg_color: 1,1,1,1
            MDLabel:
                text: "Announcement #5"
                font_size: "26sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"


            MDTextField:
                id: announcement5
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                multiline: True

            MDIconButton:
                icon: "check"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "announcements_3"     
        MDScreen:
            name: "textannouncement6"
            md_bg_color: 1,1,1,1
            MDLabel:
                text: "Announcement #6"
                font_size: "26sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"


            MDTextField:
                id: announcement6
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                multiline: True
            MDIconButton:
                icon: "check"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "announcements_3"    


        MDScreen:
            name: "textannouncement7"
            md_bg_color: 1,1,1,1
            MDLabel:
                text: "Announcement #7"
                font_size: "26sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"


            MDTextField:
                id: announcement7
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                multiline: True

            MDIconButton:
                icon: "check"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "announcements_4"     
        MDScreen:
            name: "textannouncement8"
            md_bg_color: 1,1,1,1
            MDLabel:
                text: "Announcement #8"
                font_size: "26sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"


            MDTextField:
                id: announcement8
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                multiline: True
            MDIconButton:
                icon: "check"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "announcements_4"    

        MDScreen:
            name: "textannouncement9"
            md_bg_color: 1,1,1,1
            MDLabel:
                text: "Announcement #1"
                font_size: "26sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                


            MDTextField:
                id: announcement9
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                multiline: True

            MDIconButton:
                icon: "check"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "announcements_5"  


        MDScreen:
            name: "textannouncement10"
            md_bg_color: 1,1,1,1
            MDLabel:
                text: "Announcement #1"
                font_size: "26sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"


            MDTextField:
                id: announcement10
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                multiline: True
            MDIconButton:
                icon: "check"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "announcements_5"    
##################################### calendarteachers ##################
############################## FOR MARCH - AHHHJK ############################################
        MDScreen:
            id : scr3
            md_bg_color: 1,1,1,1
            name: "favorite"


            MDIconButton:
                icon: "bullhorn-variant"
                theme_icon_color: "Custom"
                icon_color: 0, .1, .3, 1
                pos_hint: {"center_x": .07, "center_y": .96}
                on_release:
                    scr.current = "announcements"

            MDIconButton:
                icon: "arrow-right"
                theme_icon_color: "Custom"
                icon_color: 0, .1, .3, 1
                pos_hint: {"center_x": .93, "center_y": .96}
                on_release:
                    scr.current = "april"

            
            MDLabel:
                text: "MARCH"
                pos_hint: {"center_x": .5, "center_y": .96}
                font_size: "30sp"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                halign: "center"
                font_name: "fonts/LTSaeada-Regular.otf"
  
                
                
            MDCard:
                pos_hint: {"center_x": 0.08, "center_y": .89}
                size_hint: .14, .05
                md_bg_color: 1,1,1,1
                MDLabel:
                    text: "S"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}

            MDCard:
                pos_hint: {"center_x": 0.22, "center_y": .89}
                size_hint: .14, .05
                md_bg_color: 1,1,1,1
                MDLabel:
                    text: "M"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
            MDCard:
                pos_hint: {"center_x": 0.36, "center_y": .89}
                size_hint: .14, .05
                md_bg_color: 1,1,1,1
                MDLabel:
                    text: "T"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
            MDCard:
                pos_hint: {"center_x": 0.50, "center_y": .89}
                size_hint: .14, .05
                md_bg_color: 1,1,1,1
                MDLabel:
                    text: "W"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
            MDCard:
                pos_hint: {"center_x": 0.64, "center_y": .89}
                size_hint: .14, .05
                md_bg_color: 1,1,1,1
                MDLabel:
                    text: "Th"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
            MDCard:
                pos_hint: {"center_x": 0.78, "center_y": .89}
                size_hint: .14, .05
                md_bg_color: 1,1,1,1
                MDLabel:
                    text: "F"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
            MDCard:
                pos_hint: {"center_x": 0.92, "center_y": .89}
                size_hint: .14, .05
                md_bg_color: 1,1,1,1
                MDLabel:
                    text: "S"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                    
##################### NUMBERS ###########################

            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": 0.08, "center_y": .8}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "feb25"
                MDLabel:
                    text: "25"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, .5
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}


                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
   
                        
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": 0.22, "center_y": .8}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "feb26"
                MDLabel:
                    text: "26"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, .5
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": 0.36, "center_y": .8}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "feb27"
                MDLabel:
                    text: "27"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, .5
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": 0.50, "center_y": .8}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "feb28"
                MDLabel:
                    text: "28"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, .5
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": 0.64, "center_y": .8}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "feb29"
                MDLabel:
                    text: "29"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, .5
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": 0.78, "center_y": .8}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "march1"
                MDLabel:
                    text: "1"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 


            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .92, "center_y": .8}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "march2"
                MDLabel:
                    text: "2"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": 0.08, "center_y": .65}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "march3"
                MDLabel:
                    text: "3"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": 0.22, "center_y": .65}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "march4"
                MDLabel:
                    text: "4"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": 0.36, "center_y": .65}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "march5"
                MDLabel:
                    text: "5"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": 0.50, "center_y": .65}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "march6"
                MDLabel:
                    text: "6"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": 0.64, "center_y": .65}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "march7"
                MDLabel:
                    text: "7"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text:
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
    
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": 0.78, "center_y": .65}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "march8"
                MDLabel:
                    text: "8"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .92, "center_y": .65}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "march9"
                MDLabel:
                    text: "9"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .08, "center_y": .50}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "march10"
                MDLabel:
                    text: "10"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .22, "center_y": .50}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "march11"
                MDLabel:
                    text: "11"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .36, "center_y": .50}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "march12"
                MDLabel:
                    text: "12"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2}
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .50, "center_y": .50}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "march13"
                MDLabel:
                    text: "13"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text:
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2}  
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .64, "center_y": .50}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "march14"
                MDLabel:
                    text: "14"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .78, "center_y": .50}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "march15"
                MDLabel:
                    text: "15"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .92, "center_y": .50}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "march16"
                MDLabel:
                    text: "16"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .08, "center_y": .35}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "march17"
                MDLabel:
                    text: "17"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .22, "center_y": .35}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "march18"
                MDLabel:
                    text: "18"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .36, "center_y": .35}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "march19"
                MDLabel:
                    text: "19"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2}
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .50, "center_y": .35}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "march20"
                MDLabel:
                    text: "20"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2}  
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .64, "center_y": .35}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "march21"
                MDLabel:
                    text: "21"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .78, "center_y": .35}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "march22"
                MDLabel:
                    text: "22"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .92, "center_y": .35}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "march23"
                MDLabel:
                    text: "23"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 

            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .08, "center_y": .20}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "march24"
                MDLabel:
                    text: "24/31"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .22, "center_y": .20}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "march25"
                MDLabel:
                    text: "25"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .36, "center_y": .20}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "march26"
                MDLabel:
                    text: "26"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2}
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .50, "center_y": .20}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "march27"
                MDLabel:
                    text: "27"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2}  
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .64, "center_y": .20}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "march28"
                MDLabel:
                    text: "28"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .78, "center_y": .20}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "march29"
                MDLabel:
                    text: "29"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .92, "center_y": .20}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "march30"
                MDLabel:
                    text: "30"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 

############################################################################# SCREENS FOR TEXT FIELDS, MARCH - CFM ########################################                   
        MDScreen:
            name: "feb25"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"
            MDLabel:
                text: "FEB 25"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idfeb25
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"               
        MDScreen:
            name: "feb26"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"           
            MDLabel:
                text: "FEB 26"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idfeb26
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                
        MDScreen:
            name: "feb27"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"
            
            MDLabel:
                text: "FEB 27"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idfeb27
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                
        MDScreen:
            name: "feb28"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"           
            MDLabel:
                text: "FEB 28"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idfeb28
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "feb29"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"            
            MDLabel:
                text: "FEB 29"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False
                
            MDTextField:
                id: idfeb29
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5    

        MDScreen:
            name: "march1"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"            
            MDLabel:
                text: "MARCH 1"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmarch1
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                
        MDScreen:
            name: "march2"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"            
            MDLabel:
                text: "MARCH 2"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmarch2
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "march3"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"            
            MDLabel:
                text: "MARCH 3"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmarch3
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                
        MDScreen:
            name: "march4"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"            
            MDLabel:
                text: "MARCH 4"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmarch4
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "march5"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"            
            MDLabel:
                text: "MARCH 5"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmarch5
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                
        MDScreen:
            name: "march6"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"            
            MDLabel:
                text: "MARCH 6"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmarch6
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "march7"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"            
            MDLabel:
                text: "MARCH 7"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmarch7
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                
                
        MDScreen:
            name: "march8"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"            
            MDLabel:
                text: "MARCH 8"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmarch8
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "march9"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"            
            MDLabel:
                text: "MARCH 9"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmarch9
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                
                
        MDScreen:
            name: "march10"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"            
            MDLabel:
                text: "MARCH 10"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmarch10
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "march11"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"            
            MDLabel:
                text: "MARCH 11"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmarch11
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5        

        MDScreen:
            name: "march12"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"            
            MDLabel:
                text: "MARCH 12"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmarch12
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "march13"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"            
            MDLabel:
                text: "MARCH 13"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmarch13
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5                
        MDScreen:
            name: "march14"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"            
            MDLabel:
                text: "MARCH 14"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmarch14
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "march15"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"            
            MDLabel:
                text: "MARCH 15"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmarch15
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                
        MDScreen:
            name: "march16"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"            
            MDLabel:
                text: "MARCH 16"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmarch16
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "march17"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"            
            MDLabel:
                text: "MARCH 17"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmarch17
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
        MDScreen:
            name: "march18"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"            
            MDLabel:
                text: "MARCH 18"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmarch18
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "march19"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"            
            MDLabel:
                text: "MARCH 19"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmarch19
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                
        MDScreen:
            name: "march20"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"            
            MDLabel:
                text: "MARCH 20"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmarch20
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "march21"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"            
            MDLabel:
                text: "MARCH 21"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmarch21
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                
        MDScreen:
            name: "march22"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"            
            MDLabel:
                text: "MARCH 22"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmarch22
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "march23"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"     
            MDLabel:
                text: "MARCH 23"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
            MDTextField:
                id: idmarch23
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
        MDScreen:
            name: "march24"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"         
            MDLabel:
                text: "MARCH 24/31"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"


            MDTextField:
                id: idmarch24
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                
        MDScreen:
            name: "march25"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"            
            MDLabel:
                text: "MARCH 25"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmarch25
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "march26"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"            
            MDLabel:
                text: "MARCH 26"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmarch26
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                
                
        MDScreen:
            name: "march27"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"            
            MDLabel:
                text: "MARCH 27"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmarch27
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "march28"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"            
            MDLabel:
                text: "MARCH 28"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmarch28
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                
                
        MDScreen:
            name: "march29"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"            
            MDLabel:
                text: "MARCH 29"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmarch29
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "march30"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"            
            MDLabel:
                text: "MARCH 30"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmarch30
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                
        MDScreen:
            name: "march31"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"            
            MDLabel:
                text: "MARCH 31"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmarch31
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
############################# FOR APRIL - TTKH #########################################################################################################

        MDScreen:
            name: "april1"
            md_bg_color: 1,1,1,1
            MDLabel:
                text: "APRIL 1"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"


            MDTextField:
                id: idapril1
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "april"               
        MDScreen:
            name: "april2"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "april"           
            MDLabel:
                text: "APRIL 2"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idapril2
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                
        MDScreen:
            name: "april3"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "april"
            
            MDLabel:
                text: "APRIL 3"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idapril3
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                
        MDScreen:
            name: "april4"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "april"           
            MDLabel:
                text: "APRIL 4"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idapril4
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "april5"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "april"            
            MDLabel:
                text: "APRIL5"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False
                
            MDTextField:
                id: idapril5
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5    

        MDScreen:
            name: "april6"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "april"            
            MDLabel:
                text: "APRIL 6"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idapril6
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                
        MDScreen:
            name: "april7"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "april"            
            MDLabel:
                text: "APRIL 7"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idapril7
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "april8"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "april"            
            MDLabel:
                text: "APRIL8"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idapril8
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                
        MDScreen:
            name: "april9"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "april"            
            MDLabel:
                text: "APRIL 9"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idapril9
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "april10"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "april"            
            MDLabel:
                text: "APRIL 10"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idapril10
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                
        MDScreen:
            name: "april11"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "april"            
            MDLabel:
                text: "APRIL 11"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idapril11
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "april12"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "april"            
            MDLabel:
                text: "APRIL 12"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idapril12
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                
                
        MDScreen:
            name: "april13"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "april"            
            MDLabel:
                text: "APRIL 13"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idapril13
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "april14"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "april"            
            MDLabel:
                text: "APRIL 14"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idapril14
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                
                
        MDScreen:
            name: "april15"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "april"            
            MDLabel:
                text: "APRIL 15"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idapril15
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "april16"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "april"            
            MDLabel:
                text: "APRIL 16"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idapril16
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5        

        MDScreen:
            name: "april17"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "april"            
            MDLabel:
                text: "APRIL 17"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idapril17
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "april18"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "april"            
            MDLabel:
                text: "APRIL 18"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idapril18
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5                
        MDScreen:
            name: "april19"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "april"            
            MDLabel:
                text: "APRIL 19"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idapril19
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "april20"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "april"            
            MDLabel:
                text: "APRIL 20"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idapril20
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                
        MDScreen:
            name: "april21"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "april"            
            MDLabel:
                text: "APRIL 21"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idapril21
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "april22"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "april"            
            MDLabel:
                text: "APRIL 22"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idapril22
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
        MDScreen:
            name: "april23"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "april"            
            MDLabel:
                text: "APRIL 23"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idapril23
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "april24"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "april"            
            MDLabel:
                text: "APRIL 24"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idapril24
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                
        MDScreen:
            name: "april25"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "april"            
            MDLabel:
                text: "APRIL 25"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idapril25
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "april26"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"            
            MDLabel:
                text: "APRIL 26"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idapril26
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                
        MDScreen:
            name: "april27"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "april"            
            MDLabel:
                text: "APRIL 27"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idapril27
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "april28"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "april"     
            MDLabel:
                text: "APRIL 28"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
            MDTextField:
                id: idapril28
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
        MDScreen:
            name: "april29"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "april"         
            MDLabel:
                text: "APRIL 29"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"


            MDTextField:
                id: idapril29
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                
        MDScreen:
            name: "april30"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "april"            
            MDLabel:
                text: "APRIL 30"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idapril30
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "april31"
            md_bg_color: 1,1,1,1
            MDLabel:
                text: "APRIL 31"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"


            MDTextField:
                id: idapril31
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "april"  



                
                
        MDScreen:
            name: "march27"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"            
            MDLabel:
                text: "MARCH 27"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmarch27
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "march28"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"            
            MDLabel:
                text: "MARCH 28"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmarch28
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                
                
        MDScreen:
            name: "march29"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"            
            MDLabel:
                text: "MARCH 29"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmarch29
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "march30"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"            
            MDLabel:
                text: "MARCH 30"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmarch30
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                
        MDScreen:
            name: "march31"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "favorite"            
            MDLabel:
                text: "MARCH 31"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmarch31
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

#################################################################### FOR APRILLLL- HJGK z############################################
        MDScreen:
            id : scr3
            md_bg_color: 1,1,1,1
            name: "april"
            MDIconButton:
                icon: "arrow-left"
                theme_icon_color: "Custom"
                icon_color: 0, .1, .3, 1
                pos_hint: {"center_x": .78, "center_y": .96}
                on_release:
                    scr.current = "favorite"

            MDIconButton:
                icon: "bullhorn-variant"
                theme_icon_color: "Custom"
                icon_color: 0, .1, .3, 1
                pos_hint: {"center_x": .07, "center_y": .96}
                on_release:
                    scr.current = "announcements"
            MDIconButton:
                icon: "arrow-right"
                theme_icon_color: "Custom"
                icon_color: 0, .1, .3, 1
                pos_hint: {"center_x": .93, "center_y": .96}
                on_release:
                    scr.current = "may"

            MDLabel:
                text: "APRIL"
                pos_hint: {"center_x": .5, "center_y": .96}
                font_size: "30sp"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                halign: "center"
                font_name: "fonts/LTSaeada-Regular.otf"
  
                
                
            MDCard:
                pos_hint: {"center_x": 0.08, "center_y": .89}
                size_hint: .14, .05
                md_bg_color: 1,1,1,1
                MDLabel:
                    text: "S"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}

            MDCard:
                pos_hint: {"center_x": 0.22, "center_y": .89}
                size_hint: .14, .05
                md_bg_color: 1,1,1,1
                MDLabel:
                    text: "M"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
            MDCard:
                pos_hint: {"center_x": 0.36, "center_y": .89}
                size_hint: .14, .05
                md_bg_color: 1,1,1,1
                MDLabel:
                    text: "T"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
            MDCard:
                pos_hint: {"center_x": 0.50, "center_y": .89}
                size_hint: .14, .05
                md_bg_color: 1,1,1,1
                MDLabel:
                    text: "W"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
            MDCard:
                pos_hint: {"center_x": 0.64, "center_y": .89}
                size_hint: .14, .05
                md_bg_color: 1,1,1,1
                MDLabel:
                    text: "Th"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
            MDCard:
                pos_hint: {"center_x": 0.78, "center_y": .89}
                size_hint: .14, .05
                md_bg_color: 1,1,1,1
                MDLabel:
                    text: "F"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
            MDCard:
                pos_hint: {"center_x": 0.92, "center_y": .89}
                size_hint: .14, .05
                md_bg_color: 1,1,1,1
                MDLabel:
                    text: "S"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
######################################################################################################
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": 0.08, "center_y": .8}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "march31"
                MDLabel:
                    text: "31"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, .5
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}


                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
   
                        
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": 0.22, "center_y": .8}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "april1"
                MDLabel:
                    text: "1"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": 0.36, "center_y": .8}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "april2"
                MDLabel:
                    text: "2"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text:
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": 0.50, "center_y": .8}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "april3"
                MDLabel:
                    text: "3"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": 0.64, "center_y": .8}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "april4"
                MDLabel:
                    text: "4"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": 0.78, "center_y": .8}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "april5"
                MDLabel:
                    text: "5"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text:
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 


            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .92, "center_y": .8}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "april6"
                MDLabel:
                    text: "6"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": 0.08, "center_y": .65}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "april7"
                MDLabel:
                    text: "7"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text:
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": 0.22, "center_y": .65}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "april8"
                MDLabel:
                    text: "8"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": 0.36, "center_y": .65}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "april9"
                MDLabel:
                    text: "9"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": 0.50, "center_y": .65}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "april10"
                MDLabel:
                    text: "10"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": 0.64, "center_y": .65}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "april11"
                MDLabel:
                    text: "11"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
    
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": 0.78, "center_y": .65}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "april12"
                MDLabel:
                    text: "12"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .92, "center_y": .65}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "april13"
                MDLabel:
                    text: "13"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .08, "center_y": .50}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "april14"
                MDLabel:
                    text: "14"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .22, "center_y": .50}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "april15"
                MDLabel:
                    text: "15"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .36, "center_y": .50}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "april16"
                MDLabel:
                    text: "16"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2}
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .50, "center_y": .50}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "april17"
                MDLabel:
                    text: "17"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2}  
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .64, "center_y": .50}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "april18"
                MDLabel:
                    text: "18"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .78, "center_y": .50}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "april19"
                MDLabel:
                    text: "19"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .92, "center_y": .50}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "april20"
                MDLabel:
                    text: "20"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .08, "center_y": .35}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "april21"
                MDLabel:
                    text: "21"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text:
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .22, "center_y": .35}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "april22"
                MDLabel:
                    text: "22"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .36, "center_y": .35}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "april23"
                MDLabel:
                    text: "23"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2}
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .50, "center_y": .35}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "april24"
                MDLabel:
                    text: "24"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2}  
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .64, "center_y": .35}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "april25"
                MDLabel:
                    text: "25"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .78, "center_y": .35}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "april26"
                MDLabel:
                    text: "26"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .92, "center_y": .35}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "april27"
                MDLabel:
                    text: "27"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 

            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .08, "center_y": .20}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "april28"
                MDLabel:
                    text: "28"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .22, "center_y": .20}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "april29"
                MDLabel:
                    text: "29"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .36, "center_y": .20}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "april30"
                MDLabel:
                    text: "30"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2}

            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .5, "center_y": .20}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "may1"
                MDLabel:
                    text: "1"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, .5
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2}
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .64, "center_y": .20}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                MDLabel:
                    text: "2"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, .5
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2}
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .78, "center_y": .20}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"

                MDLabel:
                    text: "3"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, .5
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2}

            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .92, "center_y": .20}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"

                MDLabel:
                    text: "4"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, .5
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2}
###################################################################### MAYYY - KHF #############################################################
        MDScreen:
            id : scr3
            md_bg_color: 1,1,1,1
            name: "may"
            MDIconButton:
                icon: "arrow-left"
                theme_icon_color: "Custom"
                icon_color: 0, .1, .3, 1
                pos_hint: {"center_x": .78, "center_y": .96}
                on_release:
                    scr.current = "april"


            MDIconButton:
                icon: "bullhorn-variant"
                theme_icon_color: "Custom"
                icon_color: 0, .1, .3, 1
                pos_hint: {"center_x": .07, "center_y": .96}
                on_release:
                    scr.current = "announcements"

            MDLabel:
                text: "MAY"
                pos_hint: {"center_x": .5, "center_y": .96}
                font_size: "30sp"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                halign: "center"
                font_name: "fonts/LTSaeada-Regular.otf"
  
                
                
            MDCard:
                pos_hint: {"center_x": 0.08, "center_y": .89}
                size_hint: .14, .05
                md_bg_color: 1,1,1,1
                MDLabel:
                    text: "S"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}

            MDCard:
                pos_hint: {"center_x": 0.22, "center_y": .89}
                size_hint: .14, .05
                md_bg_color: 1,1,1,1
                MDLabel:
                    text: "M"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
            MDCard:
                pos_hint: {"center_x": 0.36, "center_y": .89}
                size_hint: .14, .05
                md_bg_color: 1,1,1,1
                MDLabel:
                    text: "T"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
            MDCard:
                pos_hint: {"center_x": 0.50, "center_y": .89}
                size_hint: .14, .05
                md_bg_color: 1,1,1,1
                MDLabel:
                    text: "W"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
            MDCard:
                pos_hint: {"center_x": 0.64, "center_y": .89}
                size_hint: .14, .05
                md_bg_color: 1,1,1,1
                MDLabel:
                    text: "Th"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
            MDCard:
                pos_hint: {"center_x": 0.78, "center_y": .89}
                size_hint: .14, .05
                md_bg_color: 1,1,1,1
                MDLabel:
                    text: "F"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
            MDCard:
                pos_hint: {"center_x": 0.92, "center_y": .89}
                size_hint: .14, .05
                md_bg_color: 1,1,1,1
                MDLabel:
                    text: "S"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
##############################################################################################################################################
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": 0.08, "center_y": .8}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "april28"
                MDLabel:
                    text: "28"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, .5
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}


                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, .5
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
   
                        
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": 0.22, "center_y": .8}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "april29"
                MDLabel:
                    text: "29"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, .5
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": 0.36, "center_y": .8}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "april30"
                MDLabel:
                    text: "30"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, .5
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, .5
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": 0.50, "center_y": .8}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "may1"
                MDLabel:
                    text: "1"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": 0.64, "center_y": .8}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "may2"
                MDLabel:
                    text: "2"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": 0.78, "center_y": .8}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "may3"
                MDLabel:
                    text: "3"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 


            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .92, "center_y": .8}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "may4"
                MDLabel:
                    text: "4"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": 0.08, "center_y": .65}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "may5"
                MDLabel:
                    text: "5"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": 0.22, "center_y": .65}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "may6"
                MDLabel:
                    text: "6"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": 0.36, "center_y": .65}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "may7"
                MDLabel:
                    text: "7"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": 0.50, "center_y": .65}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "may8"
                MDLabel:
                    text: "8"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": 0.64, "center_y": .65}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "may9"
                MDLabel:
                    text: "9"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
    
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": 0.78, "center_y": .65}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "may10"
                MDLabel:
                    text: "10"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .92, "center_y": .65}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "may11"
                MDLabel:
                    text: "11"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .08, "center_y": .50}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "may12"
                MDLabel:
                    text: "12"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .22, "center_y": .50}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "may13"
                MDLabel:
                    text: "13"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text:
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .36, "center_y": .50}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "may14"
                MDLabel:
                    text: "14"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2}
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .50, "center_y": .50}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "may15"
                MDLabel:
                    text: "15"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2}  
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .64, "center_y": .50}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "may16"
                MDLabel:
                    text: "16"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text:
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .78, "center_y": .50}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "may17"
                MDLabel:
                    text: "17"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .92, "center_y": .50}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "may18"
                MDLabel:
                    text: "18"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .08, "center_y": .35}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "may19"
                MDLabel:
                    text: "19"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text:
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .22, "center_y": .35}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "may20"
                MDLabel:
                    text: "20"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .36, "center_y": .35}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "may21"
                MDLabel:
                    text: "21"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2}
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .50, "center_y": .35}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "may22"
                MDLabel:
                    text: "22"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2}  
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .64, "center_y": .35}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "may23"
                MDLabel:
                    text: "23"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .78, "center_y": .35}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "may24"
                MDLabel:
                    text: "24"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .92, "center_y": .35}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "may25"
                MDLabel:
                    text: "25"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 

            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .08, "center_y": .20}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "may26"
                MDLabel:
                    text: "26"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .22, "center_y": .20}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "may27"
                MDLabel:
                    text: "27"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text:
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2} 
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .36, "center_y": .20}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "may28"
                MDLabel:
                    text: "28"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2}

            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .5, "center_y": .20}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "may29"
                MDLabel:
                    text: "29"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text:
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2}
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .64, "center_y": .20}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "may30"

                MDLabel:
                    text: "30"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2}
             
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .78, "center_y": .20}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"
                on_release:
                    scr.current = "may31"

                MDLabel:
                    text: "31"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                MDLabel:
                    text: 
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .2}
            MDCard:
                size_hint: .14, .15
                pos_hint: {"center_x": .92, "center_y": .20}
                md_bg_color: 1,1,1,1
                line_color: 0, .1, .3, 1
                radius: [0]
                orientation: "vertical"



############################# FOR MAY - SSBS #########################################################################################################

        MDScreen:
            name: "may1"
            md_bg_color: 1,1,1,1
            MDLabel:
                text: "MAY 1"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"


            MDTextField:
                id: idmay1
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "may"               
        MDScreen:
            name: "may2"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "may"           
            MDLabel:
                text: "MAY 2"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmay2
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                
        MDScreen:
            name: "may3"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "may"
            
            MDLabel:
                text: "MAY 3"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmay3
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                
        MDScreen:
            name: "may4"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "may"           
            MDLabel:
                text: "MAY 4"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmay4
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "may5"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "may"            
            MDLabel:
                text: "MAY 5"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False
                
            MDTextField:
                id: idmay5
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5    

        MDScreen:
            name: "may6"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "may"            
            MDLabel:
                text: "MAY 6"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmay6
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                
        MDScreen:
            name: "may7"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "may"            
            MDLabel:
                text: "MAY 7"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmay7
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "may8"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "may"            
            MDLabel:
                text: "MAY 8"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmay8
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                
        MDScreen:
            name: "may9"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "may"            
            MDLabel:
                text: "MAY 9"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmay9
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "may10"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "may"            
            MDLabel:
                text: "MAY 10"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmay10
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                
        MDScreen:
            name: "may11"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "may"            
            MDLabel:
                text: "MAY 11"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmay11
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "may12"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "may"            
            MDLabel:
                text: "MAY 12"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmay12
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                
                
        MDScreen:
            name: "may13"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "may"            
            MDLabel:
                text: "MAY 13"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmay13
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "may14"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "may"            
            MDLabel:
                text: "MAY 14"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmay14
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                
                
        MDScreen:
            name: "may15"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "may"            
            MDLabel:
                text: "MAY 15"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmay15
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "may16"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "may"            
            MDLabel:
                text: "MAY 16"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmay16
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5        

        MDScreen:
            name: "may17"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "may"            
            MDLabel:
                text: "MAY 17"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmay17
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "may18"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "may"            
            MDLabel:
                text: "MAY 18"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmay18
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5                
        MDScreen:
            name: "may19"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "may"            
            MDLabel:
                text: "MAY 19"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmay19
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "may20"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "may"            
            MDLabel:
                text: "MAY 20"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmay20
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                
        MDScreen:
            name: "may21"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "may"            
            MDLabel:
                text: "MAY 21"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmay21
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "may22"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "may"            
            MDLabel:
                text: "MAY 22"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmay22
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
        MDScreen:
            name: "may23"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "may"            
            MDLabel:
                text: "MAY 23"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmay23
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "may24"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "may"            
            MDLabel:
                text: "MAY 24"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmay24
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                
        MDScreen:
            name: "may25"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "may"            
            MDLabel:
                text: "MAY 25"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmay25
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "may26"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "may"            
            MDLabel:
                text: "MAY 26"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmay26
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                
        MDScreen:
            name: "may27"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "may"            
            MDLabel:
                text: "MAY 27"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmay27
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "may28"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "may"     
            MDLabel:
                text: "MAY 28"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
            MDTextField:
                id: idmay28
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
        MDScreen:
            name: "may29"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "may"         
            MDLabel:
                text: "MAY 29"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"


            MDTextField:
                id: idmay29
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
                
        MDScreen:
            name: "may30"
            md_bg_color: 1,1,1,1
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "may"            
            MDLabel:
                text: "MAY 30"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"
                multiline: False


            MDTextField:
                id: idmay30
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5

        MDScreen:
            name: "may31"
            md_bg_color: 1,1,1,1
            MDLabel:
                text: "MAY 31"
                font_size: "50sp"
                pos_hint: {"center_x": .5, "center_y": .9}
                text_color: 0, .1, .3, 1
                theme_text_color: "Custom"
                halign: "center"


            MDTextField:
                id: idmay31
                mode: "rectangle"
                hint_text: "Announce something!!"
                helper_text: "Calendar"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: .8,.5
            MDIconButton:
                icon: "keyboard-backspace"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .1, "center_y": .8} 
                on_release:
                    scr.current = "may"  

                
            

            
        MDScreen:
            name: "elib"
            md_bg_color: 1,1,1,1


            MDCard:
                pos_hint: {"center_x" :.5, "center_y": .5}
                size_hint: .7, .15
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                ripple_behavior: True
                on_release:
                    scr.current = "practical_research"
                MDLabel:
                    text: "Practical Research"
                    pos_hint: {"center_x" :.5, "center_y": .5}
                    font_size: "20sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    font_name: "fonts/LTSaeada-Bold.otf" 
            
                
            MDCard:
                pos_hint: {"center_x" :.5, "center_y": .7}
                size_hint: .7, .15
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                ripple_behavior: True
                on_release:
                    scr.current = "business_plan"
                MDLabel:
                    text: "Business Plan"
                    pos_hint: {"center_x" :.5, "center_y": .5}
                    font_size: "20sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    font_name: "fonts/LTSaeada-Bold.otf" 
            
            MDCard:
                pos_hint: {"center_x" :.5, "center_y": .3}
                size_hint: .7, .15
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                ripple_behavior: True
                on_release:
                    scr.current = "capstone_research"
                MDLabel:
                    text: "Capstone Research"
                    pos_hint: {"center_x" :.5, "center_y": .5}
                    font_size: "20sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    font_name: "fonts/LTSaeada-Bold.otf" 
            
                
            MDLabel:
                text: "E-Library"
                pos_hint: {"center_x" :.5, "center_y": .9}
                font_size: "30sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Bold.otf"
                
                
        MDScreen:
            name: "practical_research"
            md_bg_color: 1,1,1,1

            MDLabel:
                text: "Practical Research"
                pos_hint: {"center_x" :.5, "center_y": .9}
                font_size: "20sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Bold.otf" 
            MDIconButton:
                icon: "arrow-left"
                pos_hint: {"center_x" :.1, "center_y": .93}
                icon_size: "20sp"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                on_release:
                    scr.current = "elib"

        MDScreen:
            name: "business_plan"
            md_bg_color: 1,1,1,1
            
            MDLabel:
                text: "Business Plan"
                pos_hint: {"center_x" :.5, "center_y": .9}
                font_size: "20sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Bold.otf"
            MDIconButton:
                icon: "arrow-left"
                pos_hint: {"center_x" :.1, "center_y": .93}
                icon_size: "20sp"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                on_release:
                    scr.current = "elib"

            
        MDScreen:
            name: "capstone_research"
            md_bg_color: 1,1,1,1
            
            MDLabel:
                text: "Capstone Research"
                pos_hint: {"center_x" :.5, "center_y": .9}
                font_size: "20sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Bold.otf"
            MDIconButton:
                icon: "arrow-left"
                pos_hint: {"center_x" :.1, "center_y": .93}
                icon_size: "20sp"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                on_release:
                    scr.current = "elib"
            

#################################### PROFILE ####################################


            
        MDScreen:
            name: "profile"
            md_bg_color: 1,1,1,1
            
            MDLabel:
                text: "Gyv Jered L. Dimacali"
                pos_hint: {"center_x" :.56, "center_y": .77}
                font_size: "20sp"
                halign: "left"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Bold.otf"
                
            MDLabel:
                text: "12 STEM F"
                pos_hint: {"center_x" :.563, "center_y": .735}
                font_size: "14sp"
                halign: "left"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Regular.otf"
                
            MDLabel:
                text: "10-00076"
                pos_hint: {"center_x" :.563, "center_y": .71}
                font_size: "14sp"
                halign: "left"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Regular.otf"
            
            MDCard:
                pos_hint: {"center_x" :.5, "center_y": .35}
                size_hint: .8, .2
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                ripple_behavior: True
                orientation: "vertical"
                on_release:
                    scr.current = "verseinput"

                MDLabel:
                    text: ""
                    pos_hint: {"center_x" :.55, "center_y": .95}
                    halign: "left"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    font_name: "fonts/LTSaeada-Regular.otf"
                    size_hint: 1,.25

                MDLabel:
                    text: ""
                    pos_hint: {"center_x" :.5, "center_y": .65}
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    font_name: "fonts/LTSaeada-Regular.otf"
                    size_hint: 1,.75


            MDCard:
                pos_hint: {"center_x" :.25, "center_y": .17}
                size_hint: .4, .09
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                ripple_behavior: True
                on_release:
                    scr.current = "dailydevotioninput"

                MDIconButton:
                    icon: "notebook-heart"
                    theme_icon_color: "Custom"
                    icon_color: 0, .1, .3, 1
                    pos_hint: {"center_x": .5, "center_y": .5}

            
                MDLabel:
                    text: "Daily Devotion"
                    pos_hint: {"center_x" :.5, "center_y": .5}
                    font_size: "14sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    font_name: "fonts/LTSaeada-Regular.otf"

            MDCard:
                pos_hint: {"center_x" :.75, "center_y": .17}
                size_hint: .4, .09
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                ripple_behavior: True
                on_release:
                    scr.current = "prayerboxinput"


                MDIconButton:
                    icon: "hands-pray"
                    theme_icon_color: "Custom"
                    icon_color: 0, .1, .3, 1
                    pos_hint: {"center_x": .5, "center_y": .5}

            
                MDLabel:
                    text: "Prayer Box"
                    pos_hint: {"center_x" :.5, "center_y": .5}
                    font_size: "14sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    font_name: "fonts/LTSaeada-Regular.otf"
                        

            NavBar:
                id: navbar
                size_hint: 1, .25
                pos_hint: {"center_x": .5, "center_y": .97}
                elevation: 5
                md_bg_color: 1,1,1,1
                width: self.width

        MDScreen:
            name: "verseinput"
            md_bg_color: 1,1,1,1


            NavBar:
                id: navbar
                size_hint: 1, .25
                pos_hint: {"center_x": .5, "center_y": .97}
                elevation: 5
                md_bg_color: 1,1,1,1
                width: self.width

                Image:
                    source: "images/verse.png"
                    size_hint: 1,1
                    pos_hint: {"center_x": .5, "center_y": .3}
                    


            MDLabel:
                text: "Verse Input"
                pos_hint: {"center_x" :.5, "center_y": .77}
                font_size: "20sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Bold.otf"

            MDLabel:
                text: "Your inputs will be seen by all the students"
                pos_hint: {"center_x" :.5, "center_y": .735}
                font_size: "14sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, .5
                font_name: "fonts/LTSaeada-Regular.otf"

            MDTextField:
                id: dailydevotion
                mode: "rectangle"
                pos_hint: {"center_x": .5, "center_y": .45}
                size_hint: .8,.4
                multiline: True
                max_text_length: 150

            MDRoundFlatButton:
                text: "Send"
                text_color: 0, .1, .3, 1
                line_color: 0, .1, .3, 1
                pos_hint: {"center_x": .82, "center_y": .17}
                line_width: 1.1
                md_bg_color: "gold"
                on_release:
                    scr.current = "profile"

            MDIconButton:
                icon: "exit-to-app"
                pos_hint: {"center_x" :.06, "center_y": .78}
                icon_size: "23sp"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                on_release:
                    scr.current = "profile" 


        MDScreen:
            name: "prayerboxinput"
            md_bg_color: 1,1,1,1

            NavBar:
                id: navbar
                size_hint: 1, .25
                pos_hint: {"center_x": .5, "center_y": .97}
                elevation: 5
                md_bg_color: 1,1,1,1
                width: self.width

                Image:
                    source: "images/verse.png"
                    size_hint: 1,1
                    pos_hint: {"center_x": .5, "center_y": .3}


            MDIconButton:
                icon: "arrow-right"
                pos_hint: {"center_x" :.94, "center_y": .78}
                icon_size: "23sp"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                on_release:
                    scr.current = "prayerboxinput2" 

            MDIconButton:
                icon: "exit-to-app"
                pos_hint: {"center_x" :.06, "center_y": .78}
                icon_size: "23sp"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                on_release:
                    scr.current = "profile" 


            MDLabel:
                text: "Prayer Box"
                pos_hint: {"center_x" :.5, "center_y": .77}
                font_size: "20sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Bold.otf"

            MDLabel:
                text: "These are the prayers that the students sent."
                pos_hint: {"center_x" :.5, "center_y": .735}
                font_size: "14sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, .5
                font_name: "fonts/LTSaeada-Regular.otf"

            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: "white"
                line_width: 1.2
                pos_hint: {"center_x" :.5, "center_y": .6}
                size_hint: .7, .15
                ripple_behavior: True
                radius: [15]


            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: "white"
                line_width: 1.2
                pos_hint: {"center_x" :.5, "center_y": .4}
                size_hint: .7, .15
                ripple_behavior: True
                radius: [15]
                
            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: "white"
                line_width: 1.2
                pos_hint: {"center_x" :.5, "center_y": .2}
                size_hint: .7, .15
                ripple_behavior: True
                radius: [15]

        MDScreen:
            name: "prayerboxinput2"
            md_bg_color: 1,1,1,1

            NavBar:
                id: navbar
                size_hint: 1, .25
                pos_hint: {"center_x": .5, "center_y": .97}
                elevation: 5
                md_bg_color: 1,1,1,1
                width: self.width

                Image:
                    source: "images/verse.png"
                    size_hint: 1,1
                    pos_hint: {"center_x": .5, "center_y": .3}


            MDIconButton:
                icon: "arrow-right"
                pos_hint: {"center_x" :.94, "center_y": .78}
                icon_size: "23sp"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                on_release:
                    scr.current = "prayerboxinput3" 
            MDIconButton:
                icon: "arrow-left"
                pos_hint: {"center_x" :.85, "center_y": .78}
                icon_size: "23sp"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                on_release:
                    scr.current = "prayerboxinput" 

            MDLabel:
                text: "2"
                pos_hint: {"center_x" :.06, "center_y": .78}
                font_size: "15sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Bold.otf"




            MDLabel:
                text: "Prayer Box"
                pos_hint: {"center_x" :.5, "center_y": .77}
                font_size: "20sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Bold.otf"

            MDLabel:
                text: "These are the prayers that the students sent."
                pos_hint: {"center_x" :.5, "center_y": .735}
                font_size: "14sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, .5
                font_name: "fonts/LTSaeada-Regular.otf"

            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: "white"
                line_width: 1.2
                pos_hint: {"center_x" :.5, "center_y": .6}
                size_hint: .7, .15
                ripple_behavior: True
                radius: [15]


            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: "white"
                line_width: 1.2
                pos_hint: {"center_x" :.5, "center_y": .4}
                size_hint: .7, .15
                ripple_behavior: True
                radius: [15]

            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: "white"
                line_width: 1.2
                pos_hint: {"center_x" :.5, "center_y": .2}
                size_hint: .7, .15
                ripple_behavior: True
                radius: [15]

                
        MDScreen:
            name: "prayerboxinput3"
            md_bg_color: 1,1,1,1

            NavBar:
                id: navbar
                size_hint: 1, .25
                pos_hint: {"center_x": .5, "center_y": .97}
                elevation: 5
                md_bg_color: 1,1,1,1
                width: self.width

                Image:
                    source: "images/verse.png"
                    size_hint: 1,1
                    pos_hint: {"center_x": .5, "center_y": .3}


            MDIconButton:
                icon: "arrow-right"
                pos_hint: {"center_x" :.94, "center_y": .78}
                icon_size: "23sp"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                on_release:
                    scr.current = "prayerboxinput4" 
            MDIconButton:
                icon: "arrow-left"
                pos_hint: {"center_x" :.85, "center_y": .78}
                icon_size: "23sp"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                on_release:
                    scr.current = "prayerboxinput2" 

            MDLabel:
                text: "3"
                pos_hint: {"center_x" :.06, "center_y": .78}
                font_size: "15sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Bold.otf"




            MDLabel:
                text: "Prayer Box"
                pos_hint: {"center_x" :.5, "center_y": .77}
                font_size: "20sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Bold.otf"

            MDLabel:
                text: "These are the prayers that the students sent."
                pos_hint: {"center_x" :.5, "center_y": .735}
                font_size: "14sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, .5
                font_name: "fonts/LTSaeada-Regular.otf"

            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: "white"
                line_width: 1.2
                pos_hint: {"center_x" :.5, "center_y": .6}
                size_hint: .7, .15
                ripple_behavior: True
                radius: [15]


            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: "white"
                line_width: 1.2
                pos_hint: {"center_x" :.5, "center_y": .4}
                size_hint: .7, .15
                ripple_behavior: True
                radius: [15]

            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: "white"
                line_width: 1.2
                pos_hint: {"center_x" :.5, "center_y": .2}
                size_hint: .7, .15
                ripple_behavior: True
                radius: [15]


                
        MDScreen:
            name: "prayerboxinput4"
            md_bg_color: 1,1,1,1

            NavBar:
                id: navbar
                size_hint: 1, .25
                pos_hint: {"center_x": .5, "center_y": .97}
                elevation: 5
                md_bg_color: 1,1,1,1
                width: self.width

                Image:
                    source: "images/verse.png"
                    size_hint: 1,1
                    pos_hint: {"center_x": .5, "center_y": .3}


            MDIconButton:
                icon: "arrow-right"
                pos_hint: {"center_x" :.94, "center_y": .78}
                icon_size: "23sp"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                on_release:
                    scr.current = "prayerboxinput5" 
            MDIconButton:
                icon: "arrow-left"
                pos_hint: {"center_x" :.85, "center_y": .78}
                icon_size: "23sp"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                on_release:
                    scr.current = "prayerboxinput3" 

            MDLabel:
                text: "4"
                pos_hint: {"center_x" :.06, "center_y": .78}
                font_size: "15sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Bold.otf"




            MDLabel:
                text: "Prayer Box"
                pos_hint: {"center_x" :.5, "center_y": .77}
                font_size: "20sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Bold.otf"

            MDLabel:
                text: "These are the prayers that the students sent."
                pos_hint: {"center_x" :.5, "center_y": .735}
                font_size: "14sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, .5
                font_name: "fonts/LTSaeada-Regular.otf"

            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: "white"
                line_width: 1.2
                pos_hint: {"center_x" :.5, "center_y": .6}
                size_hint: .7, .15
                ripple_behavior: True
                radius: [15]


            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: "white"
                line_width: 1.2
                pos_hint: {"center_x" :.5, "center_y": .4}
                size_hint: .7, .15
                ripple_behavior: True
                radius: [15]

            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: "white"
                line_width: 1.2
                pos_hint: {"center_x" :.5, "center_y": .2}
                size_hint: .7, .15
                ripple_behavior: True
                radius: [15]


                
        MDScreen:
            name: "prayerboxinput5"
            md_bg_color: 1,1,1,1

            NavBar:
                id: navbar
                size_hint: 1, .25
                pos_hint: {"center_x": .5, "center_y": .97}
                elevation: 5
                md_bg_color: 1,1,1,1
                width: self.width

                Image:
                    source: "images/verse.png"
                    size_hint: 1,1
                    pos_hint: {"center_x": .5, "center_y": .3}


            MDIconButton:
                icon: "arrow-right"
                pos_hint: {"center_x" :.94, "center_y": .78}
                icon_size: "23sp"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                on_release:
                    scr.current = "prayerboxinput6" 
            MDIconButton:
                icon: "arrow-left"
                pos_hint: {"center_x" :.85, "center_y": .78}
                icon_size: "23sp"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                on_release:
                    scr.current = "prayerboxinput4" 

            MDLabel:
                text: "5"
                pos_hint: {"center_x" :.06, "center_y": .78}
                font_size: "15sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Bold.otf"




            MDLabel:
                text: "Prayer Box"
                pos_hint: {"center_x" :.5, "center_y": .77}
                font_size: "20sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Bold.otf"

            MDLabel:
                text: "These are the prayers that the students sent."
                pos_hint: {"center_x" :.5, "center_y": .735}
                font_size: "14sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, .5
                font_name: "fonts/LTSaeada-Regular.otf"

            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: "white"
                line_width: 1.2
                pos_hint: {"center_x" :.5, "center_y": .6}
                size_hint: .7, .15
                ripple_behavior: True
                radius: [15]


            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: "white"
                line_width: 1.2
                pos_hint: {"center_x" :.5, "center_y": .4}
                size_hint: .7, .15
                ripple_behavior: True
                radius: [15]

            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: "white"
                line_width: 1.2
                pos_hint: {"center_x" :.5, "center_y": .2}
                size_hint: .7, .15
                ripple_behavior: True
                radius: [15]

        MDScreen:
            name: "prayerboxinput6"
            md_bg_color: 1,1,1,1

            NavBar:
                id: navbar
                size_hint: 1, .25
                pos_hint: {"center_x": .5, "center_y": .97}
                elevation: 5
                md_bg_color: 1,1,1,1
                width: self.width

                Image:
                    source: "images/verse.png"
                    size_hint: 1,1
                    pos_hint: {"center_x": .5, "center_y": .3}


            MDIconButton:
                icon: "arrow-right"
                pos_hint: {"center_x" :.94, "center_y": .78}
                icon_size: "23sp"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                on_release:
                    scr.current = "prayerboxinput7" 
            MDIconButton:
                icon: "arrow-left"
                pos_hint: {"center_x" :.85, "center_y": .78}
                icon_size: "23sp"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                on_release:
                    scr.current = "prayerboxinput5" 

            MDLabel:
                text: "6"
                pos_hint: {"center_x" :.06, "center_y": .78}
                font_size: "15sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Bold.otf"




            MDLabel:
                text: "Prayer Box"
                pos_hint: {"center_x" :.5, "center_y": .77}
                font_size: "20sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Bold.otf"

            MDLabel:
                text: "These are the prayers that the students sent."
                pos_hint: {"center_x" :.5, "center_y": .735}
                font_size: "14sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, .5
                font_name: "fonts/LTSaeada-Regular.otf"

            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: "white"
                line_width: 1.2
                pos_hint: {"center_x" :.5, "center_y": .6}
                size_hint: .7, .15
                ripple_behavior: True
                radius: [15]


            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: "white"
                line_width: 1.2
                pos_hint: {"center_x" :.5, "center_y": .4}
                size_hint: .7, .15
                ripple_behavior: True
                radius: [15]

            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: "white"
                line_width: 1.2
                pos_hint: {"center_x" :.5, "center_y": .2}
                size_hint: .7, .15
                ripple_behavior: True
                radius: [15]

        MDScreen:
            name: "prayerboxinput7"
            md_bg_color: 1,1,1,1

            NavBar:
                id: navbar
                size_hint: 1, .25
                pos_hint: {"center_x": .5, "center_y": .97}
                elevation: 5
                md_bg_color: 1,1,1,1
                width: self.width

                Image:
                    source: "images/verse.png"
                    size_hint: 1,1
                    pos_hint: {"center_x": .5, "center_y": .3}



            MDIconButton:
                icon: "arrow-left"
                pos_hint: {"center_x" :.85, "center_y": .78}
                icon_size: "23sp"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                on_release:
                    scr.current = "prayerboxinput6" 

            MDLabel:
                text: "7"
                pos_hint: {"center_x" :.06, "center_y": .78}
                font_size: "15sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Bold.otf"




            MDLabel:
                text: "Prayer Box"
                pos_hint: {"center_x" :.5, "center_y": .77}
                font_size: "20sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Bold.otf"

            MDLabel:
                text: "These are the prayers that the students sent."
                pos_hint: {"center_x" :.5, "center_y": .735}
                font_size: "14sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, .5
                font_name: "fonts/LTSaeada-Regular.otf"

            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: "white"
                line_width: 1.2
                pos_hint: {"center_x" :.5, "center_y": .6}
                size_hint: .7, .15
                ripple_behavior: True
                radius: [15]


            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: "white"
                line_width: 1.2
                pos_hint: {"center_x" :.5, "center_y": .4}
                size_hint: .7, .15
                ripple_behavior: True
                radius: [15]

            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: "white"
                line_width: 1.2
                pos_hint: {"center_x" :.5, "center_y": .2}
                size_hint: .7, .15
                ripple_behavior: True
                radius: [15]


        MDScreen:
            name: "dailydevotioninput"
            md_bg_color: 1,1,1,1

            NavBar:
                id: navbar
                size_hint: 1, .25
                pos_hint: {"center_x": .5, "center_y": .97}
                elevation: 5
                md_bg_color: 1,1,1,1
                width: self.width

                Image:
                    source: "images/verse.png"
                    size_hint: 1,1
                    pos_hint: {"center_x": .5, "center_y": .3}
                    


            MDLabel:
                text: "Daily Devotion"
                pos_hint: {"center_x" :.5, "center_y": .77}
                font_size: "20sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Bold.otf"

            MDLabel:
                text: "Your inputs will be stored for yours only."
                pos_hint: {"center_x" :.5, "center_y": .735}
                font_size: "14sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, .5
                font_name: "fonts/LTSaeada-Regular.otf"

            MDTextField:
                id: dailydevotion
                mode: "rectangle"
                pos_hint: {"center_x": .5, "center_y": .45}
                size_hint: .8,.4
                multiline: True

            MDRoundFlatButton:
                text: "Send"
                text_color: 0, .1, .3, 1
                line_color: 0, .1, .3, 1
                pos_hint: {"center_x": .82, "center_y": .17}
                line_width: 1.1
                md_bg_color: "gold"
                on_release:
                    scr.current = "profile"




    MDCard:
        size_hint: 1.5, .11
        pos_hint: {"center_x": .5, "center_y": .02}
        border_radius: 0
        radius: [0]
        line_color: 0, .1, .3, 1
        line_width: 1.1



    MDIconButton:
        icon: "human-greeting-variant"
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .2, "center_y": .035}
        elevation: 0
        on_release:
            scr.current = "ih"

    MDIconButton:
        icon: "book-education"
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .6, "center_y": .035}
        elevation: 0

        on_release:
            scr.current = "elib"
    MDIconButton:
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        icon: "human-male-board-poll"
        pos_hint: {"center_x": .8, "center_y": .035}
        elevation: 0

        on_release:
            scr.current = "profile"
    MDIconButton:
        icon: "calendar"
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .4, "center_y": .035}
        elevation: 0

        on_release:
            scr.current = "favorite"

















    '''


class NavBar(FakeRectangularElevationBehavior, MDFloatLayout):
    pass


class ContentNavigationDrawer(BoxLayout):
    pass


class MDFloatlayout:
    pass


class Example(MDApp):
    title = "omai"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "900"


        return Builder.load_string(KV)





    def on_touch(self, instance):
        pass
        # for instance in self.root.ids.scr.children:
        # current_id = list(self.root.ids.values()).index(instance)


Example().run()