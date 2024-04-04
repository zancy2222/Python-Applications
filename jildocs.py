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
                hint_text: "Student Number"
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





                    
        
        MDScreen:
            id : scr4
            md_bg_color: 0,0,0,0
            name: "home"


                
            Image:
                source: "images/output-onlinepngtools (1).png"
                pos_hint: {"center_x" :.5, "center_y": .355}
                size_hint: .74,.74


            
            
            MDLabel:
                text: "JESUS IS LORD"
                pos_hint: {"center_x" :.5, "center_y": .93}
                font_size: "15sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1

        

            MDLabel:
                text: "COLLEGES FOUNDATION, INC."
                pos_hint: {"center_x" :.5, "center_y": .90}
                font_size: "15sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1

            MDLabel:
                text: "BUSINESS OF AFFAIRS"
                pos_hint: {"center_x" :.5, "center_y": .87}
                font_size: "15sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                
            MDCard:
                size_hint: .9, .05
                pos_hint: {"center_x" :.5, "center_y": .805}
                md_bg_color: 1,.839215, 0, .7
                line_color: 0, .1, .3, 1
                orientation: "vertical"
                line_width: 1.2
                orientation: "horizontal"

                MDLabel:
                    text: "Gyv Jered L. Dimacali"
                    pos_hint: {"center_x" : 1, "center_y": .5}
                    font_size: "11.5sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1

                MDLabel:
                    text: "12 STEM F"
                    pos_hint: {"center_x" : .5, "center_y": .5}
                    font_size: "11.5sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1

                    
                    
                


            MDCard:
                size_hint: .9, .15
                pos_hint: {"center_x" :.5, "center_y": .68}
                md_bg_color: 1,.839215, 0, .7
                orientation: "vertical"
                line_color: 0, .1, .3, 1
                line_width: 1.5
                
                MDLabel:
                    text: "Your remaining balance:"
                    pos_hint: {"center_x" :.55, "center_y": .5}
                    font_size: "10sp"
                    halign: "left"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1

                MDLabel:
                    text: "11111111"
                    pos_hint: {"center_x" :.5, "center_y": .9}
                    font_size: "25sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center"
                MDLabel:
                    text: "Plan _"
                    pos_hint: {"center_x" :.5, "center_y": .9}
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center" 
                
            MDCard:
                pos_hint: {"center_x" :.275, "center_y": .55}
                size_hint: .45, .07
                line_color: 0, .1, .3, 1
                radius: [0]
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                MDLabel:
                    text: "Particulars"
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center" 
                    
                
            MDCard:
                pos_hint: {"center_x" :.6125, "center_y": .55}
                size_hint: .225, .07
                line_color: 0, .1, .3, 1
                radius: [0]
                line_width: 1.2
                md_bg_color: 1,.839215, 0, .7
                

                MDLabel:
                    text: "Amount"
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center" 
                    
            MDCard:
                pos_hint: {"center_x" :.8375, "center_y": .55}
                size_hint: .225, .07
                line_color: 0, .1, .3, 1
                radius: [0]
                line_width: 1.2
                md_bg_color: 1,.839215, 0, .7

                MDLabel:
                    text: "Due Date"
                    font_size: "12sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center" 
                        
################################## editable ####################################

            MDCard:
                pos_hint: {"center_x" :.275, "center_y": .32}
                size_hint: .45, .39
                line_color: 0, .1, .3, 1
                radius: [0]
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                orientation: "vertical"
                MDLabel:
                    text: "Christmas Party"
                    font_size: "11sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center" 
                MDLabel:
                    text: "Christmas Party"
                    font_size: "11sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center" 
                MDLabel:
                    text: "Christmas Party"
                    font_size: "11sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center" 
                MDLabel:
                    text: "Christmas Party"
                    font_size: "11sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center" 
                MDLabel:
                    text: "Christmas Party"
                    font_size: "11sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center" 
                MDLabel:
                    text: "Christmas Party"
                    font_size: "11sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center" 
                MDLabel:
                    text: "Christmas Party"
                    font_size: "11sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center" 
                MDLabel:
                    text: "Christmas Party"
                    font_size: "11sp"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    halign: "center" 
            MDCard:
                pos_hint: {"center_x" :.725, "center_y": .32}
                size_hint: .45, .39
                line_color: 0, .1, .3, 1
                radius: [0]
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                MDCard:
                    line_color: 0, .1, .3, 1
                    radius: [0]
                    md_bg_color: 1,1,1,.05
                    line_width: 1.2
                    orientation: "vertical"
                    MDLabel:
                        text: "111111"
                        font_size: "11sp"
                        theme_text_color: "Custom"
                        text_color: 0, .1, .3, 1
                        halign: "center" 
                    MDLabel:
                        text: "111111"
                        font_size: "11sp"
                        theme_text_color: "Custom"
                        text_color: 0, .1, .3, 1
                        halign: "center" 
                    MDLabel:
                        text: "111111"
                        font_size: "11sp"
                        theme_text_color: "Custom"
                        text_color: 0, .1, .3, 1
                        halign: "center" 
                    MDLabel:
                        text: "111111"
                        font_size: "11sp"
                        theme_text_color: "Custom"
                        text_color: 0, .1, .3, 1
                        halign: "center" 
                    MDLabel:
                        text: "111111"
                        font_size: "11sp"
                        theme_text_color: "Custom"
                        text_color: 0, .1, .3, 1
                        halign: "center" 
                    MDLabel:
                        text: "111111"
                        font_size: "11sp"
                        theme_text_color: "Custom"
                        text_color: 0, .1, .3, 1
                        halign: "center" 
                    MDLabel:
                        text: "111111"
                        font_size: "11sp"
                        theme_text_color: "Custom"
                        text_color: 0, .1, .3, 1
                        halign: "center" 
                    MDLabel:
                        text: "111111"
                        font_size: "11sp"
                        theme_text_color: "Custom"
                        text_color: 0, .1, .3, 1
                        halign: "center" 


                MDCard:
                    line_color: 0, .1, .3, 1
                    radius: [0]
                    md_bg_color: 1,1,1,.05
                    line_width: 1.2
                    orientation: "vertical"
    
                    MDLabel:
                        text: "13/03/24"
                        font_size: "11sp"
                        theme_text_color: "Custom"
                        text_color: 0, .1, .3, 1
                        halign: "center" 
                    MDLabel:
                        text: "13/03/24"
                        font_size: "11sp"
                        theme_text_color: "Custom"
                        text_color: 0, .1, .3, 1
                        halign: "center" 
                    MDLabel:
                        text: "13/03/24"
                        font_size: "11sp"
                        theme_text_color: "Custom"
                        text_color: 0, .1, .3, 1
                        halign: "center" 
                    MDLabel:
                        text: "13/03/24"
                        font_size: "11sp"
                        theme_text_color: "Custom"
                        text_color: 0, .1, .3, 1
                        halign: "center" 
                    MDLabel:
                        text: "13/03/24"
                        font_size: "11sp"
                        theme_text_color: "Custom"
                        text_color: 0, .1, .3, 1
                        halign: "center" 
                    MDLabel:
                        text: "13/03/24"
                        font_size: "11sp"
                        theme_text_color: "Custom"
                        text_color: 0, .1, .3, 1
                        halign: "center" 
                    MDLabel:
                        text: "13/03/24"
                        font_size: "11sp"
                        theme_text_color: "Custom"
                        text_color: 0, .1, .3, 1
                        halign: "center" 
                    MDLabel:
                        text: "13/03/24"
                        font_size: "11sp"
                        theme_text_color: "Custom"
                        text_color: 0, .1, .3, 1
                        halign: "center" 
    
                
                
                
                
                
                
                
                
                
                
                
            

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
                FitImage:
                    pos_hint: {"center_x" :.5, "center_y": .5}
                    source: "images/org.png"
                    radius: 18,18,18,18
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

############################################# progstudents ###########################################################











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


            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: "white"
                line_width: 1.2
                pos_hint: {"center_x" :.5, "center_y": .4}
                size_hint: .7, .25
                ripple_behavior: True
                radius: [0]


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


            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: "white"
                line_width: 1.2
                pos_hint: {"center_x" :.5, "center_y": .4}
                size_hint: .7, .25
                ripple_behavior: True
                radius: [0]

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


            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: "white"
                line_width: 1.2
                pos_hint: {"center_x" :.5, "center_y": .4}
                size_hint: .7, .25
                ripple_behavior: True
                radius: [0]

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


            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: "white"
                line_width: 1.2
                pos_hint: {"center_x" :.5, "center_y": .4}
                size_hint: .7, .25
                ripple_behavior: True
                radius: [0]

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


            MDCard:
                line_color: 0, .1, .3, 1
                md_bg_color: "white"
                line_width: 1.2
                pos_hint: {"center_x" :.5, "center_y": .4}
                size_hint: .7, .25
                ripple_behavior: True
                radius: [0]

            MDLabel:
                text: "5"
                pos_hint: {"center_x" :.5, "center_y": .15}
                font_size: "20sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Bold.otf" 


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




                
            


############################################## LIBRARY #############################

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
                font_name: "fonts/LTSaeada-Regular.otf" 
            MDIconButton:
                icon: "arrow-left"
                pos_hint: {"center_x" :.1, "center_y": .9}
                icon_size: "20sp"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                on_release:
                    scr.current = "elib"

            MDCard:
                pos_hint: {"center_x" :.25, "center_y": .39}
                size_hint: .4, .2
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                ripple_behavior: True
                on_release:
                    scr.current = "practical_research_stem"
                MDLabel:
                    text: "Practical Research | STEM-related"
                    pos_hint: {"center_x" :.5, "center_y": .5}
                    font_size: "15sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    font_name: "fonts/LTSaeada-Regular.otf" 


                


            MDCard:
                pos_hint: {"center_x" :.25, "center_y": .65}
                size_hint: .4, .2
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                ripple_behavior: True
                on_release:
                    scr.current = "practical_research_abm"
                MDLabel:
                    text: "Practical Research | ABM-related"
                    pos_hint: {"center_x" :.5, "center_y": .5}
                    font_size: "15sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    font_name: "fonts/LTSaeada-Regular.otf" 


        
                    

            MDCard:
                pos_hint: {"center_x" :.75, "center_y": .39}
                size_hint: .4, .2
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                ripple_behavior: True
                on_release:
                    scr.current = "practical_research_tvl"
                MDLabel:
                    text: "Practical Research | TVL-related"
                    pos_hint: {"center_x" :.5, "center_y": .5}
                    font_size: "15sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    font_name: "fonts/LTSaeada-Regular.otf" 


            MDCard:
                pos_hint: {"center_x" :.75, "center_y": .65}
                size_hint: .4, .2
                line_color: 0, .1, .3, 1
                md_bg_color: 1,.839215, 0, .7
                line_width: 1.2
                ripple_behavior: True
                on_release:
                    scr.current = "practical_research_humss"
                MDLabel:
                    text: "Practical Research | HUMSS-related"
                    pos_hint: {"center_x" :.5, "center_y": .5}
                    font_size: "15sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    font_name: "fonts/LTSaeada-Regular.otf" 


                
############################################################################# STEM RESEARCHES ###############################################

        MDScreen:
            name: "practical_research_stem"
            md_bg_color: 1,1,1,1
            MDBoxLayout:
                orientation: "vertical"

                MDBoxLayout:
                    orientation: "horizontal"
                    size_hint: 1, .1
                    NavBar:
                        id: navbar
                        pos_hint: {"center_x": .5, "center_y": .5}
                        elevation: 5
                        md_bg_color: 1,1,1,1
                        width: self.width
                        MDLabel:
                            text: "Practical Research | STEM"
                            pos_hint: {"center_x" :.5, "center_y": .5}
                            font_size: "20sp"
                            halign: "center"
                            theme_text_color: "Custom"
                            text_color: 0, .1, .3, 1
                            font_name: "fonts/LTSaeada-Regular.otf" 
                        MDIconButton:
                            icon: "arrow-left"
                            pos_hint: {"center_x" :.1, "center_y": .5}
                            icon_size: "20sp"
                            theme_icon_color: "Custom"
                            icon_color: app.theme_cls.primary_color
                            on_release:
                                scr.current = "practical_research"

                MDScrollView:
                    size_hint: 1, .88
                    MDList:
                        id: container
                        ThreeLineListItem:
                                        ########################## FIRST LINE #################
                            text: "[size=10sp][color=0E2144]The Relationship of Sleep Deprivation to the Academic Performance of[/color][/size]"
                                        ######################### SECOND LINE #######################
                            secondary_text: "[size=10sp][color=0E2144]Grade 12 Science, Technology, Engineering and Mathematics (STEM)[/color][/size]"
                                        ######################### THIRD LINE ###############################
                            tertiary_text:"[size=10sp][color=0E2144]Students in Jesus Is Lord Colleges Foundation, Inc. (JILCF)[/color][/size]"                            
                            markup: True
                            on_release:
                                import webbrowser
                                webbrowser.open('https://drive.google.com/file/d/1eNPOEQyFuXIfP8V6g8V2FeUOnFvmYd9o/view?usp=sharing')

                        ThreeLineListItem:
                                        ########################## FIRST LINE #################
                            text: "[size=10sp][color=0E2144]The Relationship of Sleep Deprivation to the Academic Performance of[/color][/size]"
                                        ######################### SECOND LINE #######################
                            secondary_text: "[size=10sp][color=0E2144]Grade 12 Science, Technology, Engineering and Mathematics (STEM)[/color][/size]"
                                        ######################### THIRD LINE ###############################
                            tertiary_text:"[size=10sp][color=0E2144]Students in Jesus Is Lord Colleges Foundation, Inc. (JILCF)[/color][/size]"                            
                            markup: True
                            on_release:
                                import webbrowser
                                webbrowser.open('https://drive.google.com/file/d/1eNPOEQyFuXIfP8V6g8V2FeUOnFvmYd9o/view?usp=sharing')

                MDCard:
                    size_hint: 1, .07
                    pos_hint: {"center_x": .5, "center_y": .02}
                    border_radius: 0
                    radius: [0]
                    line_color: 0, .1, .3, 1
                    line_width: 1.1
##################################################################### ABM RESEARCHES #################################################

        MDScreen:
            name: "practical_research_abm"
            md_bg_color: 1,1,1,1
            MDBoxLayout:
                orientation: "vertical"

                MDBoxLayout:
                    orientation: "horizontal"
                    size_hint: 1, .1
                    NavBar:
                        id: navbar
                        pos_hint: {"center_x": .5, "center_y": .5}
                        elevation: 5
                        md_bg_color: 1,1,1,1
                        width: self.width
                        MDLabel:
                            text: "Practical Research | ABM"
                            pos_hint: {"center_x" :.5, "center_y": .5}
                            font_size: "20sp"
                            halign: "center"
                            theme_text_color: "Custom"
                            text_color: 0, .1, .3, 1
                            font_name: "fonts/LTSaeada-Regular.otf" 
                        MDIconButton:
                            icon: "arrow-left"
                            pos_hint: {"center_x" :.1, "center_y": .5}
                            icon_size: "20sp"
                            theme_icon_color: "Custom"
                            icon_color: app.theme_cls.primary_color
                            on_release:
                                scr.current = "practical_research"

                MDScrollView:
                    size_hint: 1, .88
                    MDList:
                        id: container
                        ThreeLineListItem:
                                        ########################## FIRST LINE #################
                            text: "[size=10sp][color=0E2144]The Relationship of Sleep Deprivation to the Academic Performance of[/color][/size]"
                                        ######################### SECOND LINE #######################
                            secondary_text: "[size=10sp][color=0E2144]Grade 12 Science, Technology, Engineering and Mathematics (STEM)[/color][/size]"
                                        ######################### THIRD LINE ###############################
                            tertiary_text:"[size=10sp][color=0E2144]Students in Jesus Is Lord Colleges Foundation, Inc. (JILCF)[/color][/size]"                            
                            markup: True
                            on_release:
                                import webbrowser
                                webbrowser.open('https://drive.google.com/file/d/1eNPOEQyFuXIfP8V6g8V2FeUOnFvmYd9o/view?usp=sharing')

                        ThreeLineListItem:
                                        ########################## FIRST LINE #################
                            text: "[size=10sp][color=0E2144]The Relationship of Sleep Deprivation to the Academic Performance of[/color][/size]"
                                        ######################### SECOND LINE #######################
                            secondary_text: "[size=10sp][color=0E2144]Grade 12 Science, Technology, Engineering and Mathematics (STEM)[/color][/size]"
                                        ######################### THIRD LINE ###############################
                            tertiary_text:"[size=10sp][color=0E2144]Students in Jesus Is Lord Colleges Foundation, Inc. (JILCF)[/color][/size]"                            
                            markup: True
                            on_release:
                                import webbrowser
                                webbrowser.open('https://drive.google.com/file/d/1eNPOEQyFuXIfP8V6g8V2FeUOnFvmYd9o/view?usp=sharing')

                MDCard:
                    size_hint: 1, .07
                    pos_hint: {"center_x": .5, "center_y": .02}
                    border_radius: 0
                    radius: [0]
                    line_color: 0, .1, .3, 1
                    line_width: 1.1


######################################################## TVL RESEARCHES ###################################
        MDScreen:
            name: "practical_research_tvl"
            md_bg_color: 1,1,1,1
            MDBoxLayout:
                orientation: "vertical"

                MDBoxLayout:
                    orientation: "horizontal"
                    size_hint: 1, .1
                    NavBar:
                        id: navbar
                        pos_hint: {"center_x": .5, "center_y": .5}
                        elevation: 5
                        md_bg_color: 1,1,1,1
                        width: self.width
                        MDLabel:
                            text: "Practical Research | TVL"
                            pos_hint: {"center_x" :.5, "center_y": .5}
                            font_size: "20sp"
                            halign: "center"
                            theme_text_color: "Custom"
                            text_color: 0, .1, .3, 1
                            font_name: "fonts/LTSaeada-Regular.otf" 
                        MDIconButton:
                            icon: "arrow-left"
                            pos_hint: {"center_x" :.1, "center_y": .5}
                            icon_size: "20sp"
                            theme_icon_color: "Custom"
                            icon_color: app.theme_cls.primary_color
                            on_release:
                                scr.current = "practical_research"

                MDScrollView:
                    size_hint: 1, .88
                    MDList:
                        id: container
                        ThreeLineListItem:
                                        ########################## FIRST LINE #################
                            text: "[size=10sp][color=0E2144]The Relationship of Sleep Deprivation to the Academic Performance of[/color][/size]"
                                        ######################### SECOND LINE #######################
                            secondary_text: "[size=10sp][color=0E2144]Grade 12 Science, Technology, Engineering and Mathematics (STEM)[/color][/size]"
                                        ######################### THIRD LINE ###############################
                            tertiary_text:"[size=10sp][color=0E2144]Students in Jesus Is Lord Colleges Foundation, Inc. (JILCF)[/color][/size]"                            
                            markup: True
                            on_release:
                                import webbrowser
                                webbrowser.open('https://drive.google.com/file/d/1eNPOEQyFuXIfP8V6g8V2FeUOnFvmYd9o/view?usp=sharing')

                        ThreeLineListItem:
                                        ########################## FIRST LINE #################
                            text: "[size=10sp][color=0E2144]The Relationship of Sleep Deprivation to the Academic Performance of[/color][/size]"
                                        ######################### SECOND LINE #######################
                            secondary_text: "[size=10sp][color=0E2144]Grade 12 Science, Technology, Engineering and Mathematics (STEM)[/color][/size]"
                                        ######################### THIRD LINE ###############################
                            tertiary_text:"[size=10sp][color=0E2144]Students in Jesus Is Lord Colleges Foundation, Inc. (JILCF)[/color][/size]"                            
                            markup: True
                            on_release:
                                import webbrowser
                                webbrowser.open('https://drive.google.com/file/d/1eNPOEQyFuXIfP8V6g8V2FeUOnFvmYd9o/view?usp=sharing')

                MDCard:
                    size_hint: 1, .07
                    pos_hint: {"center_x": .5, "center_y": .02}
                    border_radius: 0
                    radius: [0]
                    line_color: 0, .1, .3, 1
                    line_width: 1.1


##################################################### HUMSS RESEARCHES ##############################################
        MDScreen:
            name: "practical_research_humss"
            md_bg_color: 1,1,1,1
            MDBoxLayout:
                orientation: "vertical"

                MDBoxLayout:
                    orientation: "horizontal"
                    size_hint: 1, .1
                    NavBar:
                        id: navbar
                        pos_hint: {"center_x": .5, "center_y": .5}
                        elevation: 5
                        md_bg_color: 1,1,1,1
                        width: self.width
                        MDLabel:
                            text: "Practical Research | HUMSS"
                            pos_hint: {"center_x" :.5, "center_y": .5}
                            font_size: "20sp"
                            halign: "center"
                            theme_text_color: "Custom"
                            text_color: 0, .1, .3, 1
                            font_name: "fonts/LTSaeada-Regular.otf" 
                        MDIconButton:
                            icon: "arrow-left"
                            pos_hint: {"center_x" :.1, "center_y": .5}
                            icon_size: "20sp"
                            theme_icon_color: "Custom"
                            icon_color: app.theme_cls.primary_color
                            on_release:
                                scr.current = "practical_research"

                MDScrollView:
                    size_hint: 1, .88
                    MDList:
                        id: container
                        ThreeLineListItem:
                                        ########################## FIRST LINE #################
                            text: "[size=10sp][color=0E2144]The Relationship of Sleep Deprivation to the Academic Performance of[/color][/size]"
                                        ######################### SECOND LINE #######################
                            secondary_text: "[size=10sp][color=0E2144]Grade 12 Science, Technology, Engineering and Mathematics (STEM)[/color][/size]"
                                        ######################### THIRD LINE ###############################
                            tertiary_text:"[size=10sp][color=0E2144]Students in Jesus Is Lord Colleges Foundation, Inc. (JILCF)[/color][/size]"                            
                            markup: True
                            on_release:
                                import webbrowser
                                webbrowser.open('https://drive.google.com/file/d/1eNPOEQyFuXIfP8V6g8V2FeUOnFvmYd9o/view?usp=sharing')

                        ThreeLineListItem:
                                        ########################## FIRST LINE #################
                            text: "[size=10sp][color=0E2144]The Relationship of Sleep Deprivation to the Academic Performance of[/color][/size]"
                                        ######################### SECOND LINE #######################
                            secondary_text: "[size=10sp][color=0E2144]Grade 12 Science, Technology, Engineering and Mathematics (STEM)[/color][/size]"
                                        ######################### THIRD LINE ###############################
                            tertiary_text:"[size=10sp][color=0E2144]Students in Jesus Is Lord Colleges Foundation, Inc. (JILCF)[/color][/size]"                            
                            markup: True
                            on_release:
                                import webbrowser
                                webbrowser.open('https://drive.google.com/file/d/1eNPOEQyFuXIfP8V6g8V2FeUOnFvmYd9o/view?usp=sharing')

                MDCard:
                    size_hint: 1, .07
                    pos_hint: {"center_x": .5, "center_y": .02}
                    border_radius: 0
                    radius: [0]
                    line_color: 0, .1, .3, 1
                    line_width: 1.1




        MDScreen:
            name: "business_plan"
            md_bg_color: 1,1,1,1
            
            NavBar:
                id: navbar
                size_hint: 1, .1
                pos_hint: {"center_x": .5, "center_y": .97}
                elevation: 5
                md_bg_color: 1,1,1,1
                width: self.width
                MDLabel:
                    text: "Business Plan"
                    pos_hint: {"center_x" :.5, "center_y": .4}
                    font_size: "20sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    font_name: "fonts/LTSaeada-Bold.otf" 
                MDIconButton:
                    icon: "arrow-left"
                    pos_hint: {"center_x" :.1, "center_y": .4}
                    icon_size: "20sp"
                    theme_icon_color: "Custom"
                    icon_color: app.theme_cls.primary_color
                    on_release:
                        scr.current = "elib"

            
        MDScreen:
            name: "capstone_research"
            md_bg_color: 1,1,1,1

            NavBar:
                id: navbar
                size_hint: 1, .1
                pos_hint: {"center_x": .5, "center_y": .97}
                elevation: 5
                md_bg_color: 1,1,1,1
                width: self.width
                MDLabel:
                    text: "Capstone Research"
                    pos_hint: {"center_x" :.5, "center_y": .4}
                    font_size: "20sp"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, .1, .3, 1
                    font_name: "fonts/LTSaeada-Bold.otf" 
                MDIconButton:
                    icon: "arrow-left"
                    pos_hint: {"center_x" :.1, "center_y": .4}
                    icon_size: "20sp"
                    theme_icon_color: "Custom"
                    icon_color: app.theme_cls.primary_color
                    on_release:
                        scr.current = "elib"


            
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

                    


            MDLabel:
                text: "Prayer Box"
                pos_hint: {"center_x" :.5, "center_y": .77}
                font_size: "20sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, 1
                font_name: "fonts/LTSaeada-Bold.otf"

            MDLabel:
                text: "Your personal prayers will be sent to the teachers."
                pos_hint: {"center_x" :.5, "center_y": .735}
                font_size: "14sp"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0, .1, .3, .5
                font_name: "fonts/LTSaeada-Regular.otf"

            MDTextField:
                id: prayerbox
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
                text: "Daily Deovtion"
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
        icon: "account-cash"
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .1, "center_y": .035}
        elevation: 0

        on_release:
            scr.current = "home"
    MDIconButton:
        icon: "human-greeting-variant"
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .3, "center_y": .035}
        elevation: 0

        on_release:
            scr.current = "ih"
    MDIconButton:
        icon: "book-education"
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .7, "center_y": .035}
        elevation: 0

        on_release:
            scr.current = "elib"
    MDIconButton:
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        icon: "account-school"
        pos_hint: {"center_x": .9, "center_y": .035}
        elevation: 0

        on_release:
            scr.current = "profile"
    MDIconButton:
        icon: "calendar"
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .5, "center_y": .035}
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