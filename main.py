from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.core.window import Window
from contextvars import ContextVar

Builder.load_file('design.kv')

Window.softinput_mode = "below_target"

flag = ContextVar('flag', default=False)

# show/hide the widgets associated with the button


def show(widget1, widget2, widget3, box, button):
    for widget in (widget1, widget2, widget3):
        if widget.opacity == 0:
            if widget == widget3:
                widget.size_hint = 0.1, 0.7
                widget.color = [0, 0, 0, 1]
            else:
                widget.size_hint = 0.6, 0.7
                widget.color = [0, 0, 0, 1]
            widget.opacity = 1
        else:
            widget.size_hint = 0, 0
            widget.opacity = 0
    
    if box.height == 0:
        box.size_hint_y = 0.5
        flag.set(True)
        # button.background_color = 0, 0.7, 0.7
        # button.background_down = button.background_normal
    else:
        box.size_hint_y = None
        box.height = 0
        flag.set(False)
        # button.background_normal = 'atlas://data/images/defaulttheme/button'
        # button.background_color = 0.25, 0.95, 1


class ImageButton(ButtonBehavior, Image):
    pass


class MainScreen(Screen):
    # when user clicks on TextInput, select its text
    # otherwise add unit names after numbers

    def select(self, instance, n):
        if instance.focus == True:
            if ' ' in instance.text:
                instance.text = instance.text[:-n]
            Clock.schedule_once(lambda dt: instance.select_all())
        else:
            if instance.text != '' and instance.text != '-' and instance.text != '.' and instance.text != '-.':
                instance.text += ' ' + instance.hint_text

    # conversion functions
    # temperature
    def fahrenheit(self, f):
        if self.ids.fahrenheit.focus == True:
            self.ids.celcius.text = ''
            if f != '' and f != '-' and f != '.' and f != '-.':
                self.ids.celcius.text = str(int((float(f) - 32) * 5 / 9)) + ' °C'

    def celcius(self, c):
        if self.ids.celcius.focus == True:
            self.ids.fahrenheit.text = ''
            if c != '' and c != '-' and c != '.' and c != '-.':
                self.ids.fahrenheit.text = str(int((float(c) * 9 / 5) + 32)) + ' °F'

    # mass
    def oz(self, oz):
        if self.ids.oz.focus == True:
            self.ids.gram.text = ''
            if oz != '' and oz != '.' and '-' not in oz:
                self.ids.gram.text = '{:.2f}'.format(float(oz) * 28.3495) + ' g'
    
    def gram(self, g):
        if self.ids.gram.focus == True:
            self.ids.oz.text = ''
            if g != '' and g != '.' and '-' not in g:
                self.ids.oz.text = '{:.2f}'.format(float(g) / 28.3495) + ' oz'


    def ibs(self, ibs):
        if self.ids.ibs.focus == True:
            self.ids.kgs.text = ''
            if ibs != '' and ibs != '.' and '-' not in ibs:
                self.ids.kgs.text = '{:.2f}'.format(float(ibs) / 2.2046226218) + ' kg'
    
    def kgs(self, kgs):
        if self.ids.kgs.focus == True:
            self.ids.ibs.text = ''
            if kgs != '' and kgs != '.' and '-' not in kgs:
                self.ids.ibs.text = '{:.2f}'.format(float(kgs) * 2.2046226218) + ' ibs'

    # volume
    def floz(self, floz):
        if self.ids.floz.focus == True:
            self.ids.ml.text = ''
            if floz != '' and floz != '.' and '-' not in floz:
                self.ids.ml.text = '{:.2f}'.format(float(floz) * 28.41306) + ' ml'

    def ml(self, ml):
        if self.ids.ml.focus == True:
            self.ids.floz.text = ''
            if ml != '' and ml != '.' and '-' not in ml:
                self.ids.floz.text = '{:.2f}'.format(float(ml) / 28.41306) + ' fl oz'

   
    def quart(self, qt):
        if self.ids.quart.focus == True:
            self.ids.litre2.text = ''
            if qt != '' and qt != '.' and '-' not in qt:
                self.ids.litre2.text = '{:.2f}'.format(float(qt) * 1.13652) + ' L'
    
    def litre2(self, l):
        if self.ids.litre2.focus == True:
            self.ids.quart.text = ''
            if l != '' and l != '.' and '-' not in l:
                self.ids.quart.text = '{:.2f}'.format(float(l) / 1.13652) + ' qt'


    def gal(self, gal):
        if self.ids.gallon.focus == True:
            self.ids.litre3.text = ''
            if gal != '' and gal != '.' and '-' not in gal:
                self.ids.litre3.text = '{:.2f}'.format(float(gal) * 4.54609) + ' L'

    def litre3(self, l):
        if self.ids.litre3.focus == True:
            self.ids.gallon.text = ''
            if l != '' and l != '.' and '-' not in l:
                self.ids.gallon.text = '{:.2f}'.format(float(l) / 4.54609) + ' gal'

    # distance
    def inch(self, inch):
        if self.ids.inch.focus == True:
            self.ids.mm.text = ''
            if inch != '' and inch != '.' and '-' not in inch:
                self.ids.mm.text = '{:.2f}'.format(float(inch) * 25.4) + ' mm'
    
    def mm(self, mm):
        if self.ids.mm.focus == True:
            self.ids.inch.text = ''
            if mm != '' and mm != '.' and '-' not in mm:
                self.ids.inch.text = '{:.2f}'.format(float(mm) / 25.4) + ' in "'


    def feet(self, feet):
        if self.ids.feet.focus == True:
            self.ids.cm.text = ''
            if feet != '' and feet != '.' and '-' not in feet:
                self.ids.cm.text = '{:.2f}'.format(float(feet) * 30.48) + ' cm'
    
    def cm(self, cm):
        if self.ids.cm.focus == True:
            self.ids.feet.text = ''
            if cm != '' and cm != '.' and '-' not in cm:
                self.ids.feet.text = '{:.2f}'.format(float(cm) / 30.48) + " ft '"


    def yard(self, yd):
        if self.ids.yard.focus == True:
            self.ids.metre.text = ''
            if yd != '' and yd != '.' and '-' not in yd:
                self.ids.metre.text = '{:.2f}'.format(float(yd) / 1.0936) + ' m'
    
    def metre(self, m):
        if self.ids.metre.focus == True:
            self.ids.yard.text = ''
            if m != '' and m != '.' and '-' not in m:
                self.ids.yard.text = '{:.2f}'.format(float(m) * 1.0936) + ' yd'


    def mile(self, mile):
        if self.ids.mile.focus == True:
            self.ids.km.text = ''
            if mile != '' and mile != '.' and '-' not in mile:
                self.ids.km.text = '{:.2f}'.format(float(mile) * 1.60934) + ' km'
    
    def km(self, km):
        if self.ids.km.focus == True:
            self.ids.mile.text = ''
            if km != '' and km != '.' and '-' not in km:
                self.ids.mile.text = '{:.2f}'.format(float(km) / 1.60934) + ' mile'

    # area
    def sqft(self, sqft):
        if self.ids.sqft.focus == True:
            self.ids.m21.text = ''
            if sqft != '' and sqft != '.' and '-' not in sqft:
                self.ids.m21.text = '{:.2f}'.format(float(sqft) / 10.764) + ' m²'

    def m21(self, m2):
        if self.ids.m21.focus == True:
            self.ids.sqft.text = ''
            if m2 != '' and m2 != '.' and '-' not in m2:
                self.ids.sqft.text = '{:.2f}'.format(float(m2) * 10.764) + ' sq ft'
    

    def sqyd(self, sqyd):
        if self.ids.sqyd.focus == True:
            self.ids.m22.text = ''
            if sqyd != '' and sqyd != '.' and '-' not in sqyd:
                self.ids.m22.text = '{:.2f}'.format(float(sqyd) / 1.196) + ' m²'

    def m22(self, m2):
        if self.ids.m22.focus == True:
            self.ids.sqyd.text = ''
            if m2 != '' and m2 != '.' and '-' not in m2:
                self.ids.sqyd.text = '{:.2f}'.format(float(m2) * 1.196) + ' sq yd'


    def acre(self, acre):
        if self.ids.acre.focus == True:
            self.ids.ha.text = ''
            if acre != '' and acre != '.' and '-' not in acre:
                self.ids.ha.text = '{:.2f}'.format(float(acre) / 2.471) + ' ha'

    def ha(self, ha):
        if self.ids.ha.focus == True:
            self.ids.acre.text = ''
            if ha != '' and ha != '.' and '-' not in ha:
                self.ids.acre.text = '{:.2f}'.format(float(ha) * 2.471) + ' acre'


    def sqmi(self, sqmi):
        if self.ids.sqmi.focus == True:
            self.ids.km2.text = ''
            if sqmi != '' and sqmi != '.' and '-' not in sqmi:
                self.ids.km2.text = '{:.2f}'.format(float(sqmi) * 2.59) + ' km²'

    def km2(self, km2):
        if self.ids.km2.focus == True:
            self.ids.sqmi.text = ''
            if km2 != '' and km2 != '.' and '-' not in km2:
                self.ids.sqmi.text = '{:.2f}'.format(float(km2) / 2.59) + ' sq mi'


    # widgets show/hide functions

    def show_temp(self):
        if flag.get() == True:
            if self.ids.layout_mass1.height != 0:
                flag.set(False)
                self.show_mass()
            elif self.ids.layout_volume1.height != 0:
                flag.set(False)
                self.show_volume()
            elif self.ids.layout_dist1.height != 0:
                flag.set(False)
                self.show_dist()
            elif self.ids.layout_area1.height != 0:
                flag.set(False)
                self.show_area()
        show(self.ids.fahrenheit, self.ids.celcius, self.ids.equal_temp, 
        self.ids.layout_temp, self.ids.temperature)
        self.ids.fahrenheit.text = ''
        self.ids.celcius.text = ''
    
    def show_mass(self):
        if flag.get() == True:
            if self.ids.layout_temp.height != 0:
                flag.set(False)
                self.show_temp()
            elif self.ids.layout_volume1.height != 0:
                flag.set(False)
                self.show_volume()
            elif self.ids.layout_dist1.height != 0:
                flag.set(False)
                self.show_dist()
            elif self.ids.layout_area1.height != 0:
                flag.set(False)
                self.show_area()
        show(self.ids.oz, self.ids.gram, self.ids.equal_mass1, 
        self.ids.layout_mass1, self.ids.mass)
        show(self.ids.ibs, self.ids.kgs, self.ids.equal_mass2, 
        self.ids.layout_mass2, self.ids.mass)
        self.ids.oz.text = ''
        self.ids.gram.text = ''
        self.ids.ibs.text = ''
        self.ids.kgs.text = ''
    
    def show_volume(self):
        if flag.get() == True:
            if self.ids.layout_temp.height != 0:
                flag.set(False)
                self.show_temp()
            elif self.ids.layout_mass1.height != 0:
                flag.set(False)
                self.show_mass()
            elif self.ids.layout_dist1.height != 0:
                flag.set(False)
                self.show_dist()
            elif self.ids.layout_area1.height != 0:
                flag.set(False)
                self.show_area()
        show(self.ids.floz, self.ids.ml, self.ids.equal_volume1, 
        self.ids.layout_volume1, self.ids.volume)
        show(self.ids.quart, self.ids.litre2, self.ids.equal_volume2, 
        self.ids.layout_volume2, self.ids.volume)
        show(self.ids.gallon, self.ids.litre3, self.ids.equal_volume3, 
        self.ids.layout_volume3, self.ids.volume)
        self.ids.floz.text = ''
        self.ids.ml.text = ''
        self.ids.quart.text = ''
        self.ids.litre2.text = ''
        self.ids.gallon.text = ''
        self.ids.litre3.text = ''
    
    def show_dist(self):
        if flag.get() == True:
            if self.ids.layout_temp.height != 0:
                flag.set(False)
                self.show_temp()
            elif self.ids.layout_mass1.height != 0:
                flag.set(False)
                self.show_mass()
            elif self.ids.layout_volume1.height != 0:
                flag.set(False)
                self.show_volume()
            elif self.ids.layout_area1.height != 0:
                flag.set(False)
                self.show_area()
        show(self.ids.inch, self.ids.mm, self.ids.equal_dist1, 
        self.ids.layout_dist1, self.ids.distance)
        show(self.ids.feet, self.ids.cm, self.ids.equal_dist2, 
        self.ids.layout_dist2, self.ids.distance)
        show(self.ids.yard, self.ids.metre, self.ids.equal_dist3, 
        self.ids.layout_dist3, self.ids.distance)
        show(self.ids.mile, self.ids.km, self.ids.equal_dist4, 
        self.ids.layout_dist4, self.ids.distance)
        self.ids.inch.text = ''
        self.ids.mm.text = ''
        self.ids.feet.text = ''
        self.ids.cm.text = ''
        self.ids.yard.text = ''
        self.ids.metre.text = ''
        self.ids.mile.text = ''
        self.ids.km.text = ''
    
    def show_area(self):
        if flag.get() == True:
            if self.ids.layout_temp.height != 0:
                flag.set(False)
                self.show_temp()
            elif self.ids.layout_mass1.height != 0:
                flag.set(False)
                self.show_mass()
            elif self.ids.layout_volume1.height != 0:
                flag.set(False)
                self.show_volume()
            elif self.ids.layout_dist1.height != 0:
                flag.set(False)
                self.show_dist()
        show(self.ids.sqft, self.ids.m21, self.ids.equal_area1, 
        self.ids.layout_area1, self.ids.area)
        show(self.ids.sqyd, self.ids.m22, self.ids.equal_area2, 
        self.ids.layout_area2, self.ids.area)
        show(self.ids.acre, self.ids.ha, self.ids.equal_area3, 
        self.ids.layout_area3, self.ids.area)
        show(self.ids.sqmi, self.ids.km2, self.ids.equal_area4, 
        self.ids.layout_area4, self.ids.area)
        self.ids.sqft.text = ''
        self.ids.m21.text = ''
        self.ids.sqyd.text = ''
        self.ids.m22.text = ''
        self.ids.acre.text = ''
        self.ids.ha.text = ''
        self.ids.sqmi.text = ''
        self.ids.km2.text = ''
    

    def imperial(self):
        if flag.get() == True:
            if self.ids.layout_temp.height != 0:
                flag.set(False)
                self.show_temp()
            if self.ids.layout_mass1.height != 0:
                flag.set(False)
                self.show_mass()
            elif self.ids.layout_volume1.height != 0:
                flag.set(False)
                self.show_volume()
            elif self.ids.layout_dist1.height != 0:
                flag.set(False)
                self.show_dist()
            elif self.ids.layout_area1.height != 0:
                flag.set(False)
                self.show_area()
        self.manager.current = "imperial_screen"


class ImperialScreen(Screen):
    # converson functions
    
    def select(self, instance):
        if instance.focus == True:
            Clock.schedule_once(lambda dt: instance.select_all())

    # mass
    def oz(self, oz):
        if self.ids.oz.focus == True:
            self.ids.ibs.text = ''
            if oz != '' and oz != '.' and '-' not in oz:
                self.ids.ibs.text = '{:.2f}'.format(float(oz) / 16)
    
    def ibs(self, ibs):
        if self.ids.ibs.focus == True:
            self.ids.oz.text = ''
            if ibs != '' and ibs != '.' and '-' not in ibs:
                self.ids.oz.text = '{:.2f}'.format(float(ibs) * 16)
    
    # volume
    def floz(self, floz):
        if self.ids.floz.focus == True:
            self.ids.quart.text = ''
            self.ids.gallon.text = ''
            if floz != '' and floz != '.' and '-' not in floz:
                self.ids.quart.text = '{:.2f}'.format(float(floz) / 40)
                self.ids.gallon.text = '{:.2f}'.format(float(floz) / 160)
    
    def quart(self, qt):
        if self.ids.quart.focus == True:
            self.ids.floz.text = ''
            self.ids.gallon.text = ''
            if qt != '' and qt != '.' and '-' not in qt:
                self.ids.floz.text = '{:.2f}'.format(float(qt) * 40)
                self.ids.gallon.text = '{:.2f}'.format(float(qt) / 4)
    
    def gallon(self, gal):
        if self.ids.gallon.focus == True:
            self.ids.floz.text = ''
            self.ids.quart.text = ''
            if gal != '' and gal != '.' and '-' not in gal:
                self.ids.floz.text = '{:.2f}'.format(float(gal) * 160)
                self.ids.quart.text = '{:.2f}'.format(float(gal) * 4)
    
    # distance
    def inch(self, inch):
        if self.ids.inch.focus == True:
            self.ids.feet.text = ''
            self.ids.yard.text = ''
            if inch != '' and inch != '.' and '-' not in inch:
                self.ids.feet.text = '{:.2f}'.format(float(inch) / 12)
                self.ids.yard.text = '{:.2f}'.format(float(inch) / 36)

    def feet(self, feet):
        if self.ids.feet.focus == True:
            self.ids.inch.text = ''
            self.ids.yard.text = ''
            if feet != '' and feet != '.' and '-' not in feet:
                self.ids.inch.text = '{:.2f}'.format(float(feet) * 12)
                self.ids.yard.text = '{:.2f}'.format(float(feet) / 3)

    def yard(self, yd):
        if self.ids.yard.focus == True:
            self.ids.inch.text = ''
            self.ids.feet.text = ''
            if yd != '' and yd != '.' and '-' not in yd:
                self.ids.inch.text = '{:.2f}'.format(float(yd) * 36)
                self.ids.feet.text = '{:.2f}'.format(float(yd) * 3)

    
    # area
    def sqft(self, sqft):
        if self.ids.sqft.focus == True:
            self.ids.sqyd.text = ''
            if sqft != '' and sqft != '.' and '-' not in sqft:
                self.ids.sqyd.text = '{:.2f}'.format(float(sqft) / 9)
    
    def sqyd(self, sqyd):
        if self.ids.sqyd.focus == True:
            self.ids.sqft.text = ''
            if sqyd != '' and sqyd != '.' and '-' not in sqyd:
                self.ids.sqft.text = '{:.2f}'.format(float(sqyd) * 9)
    

    def back(self):
        # self.manager.transition.direction = "right"
        self.manager.current = "main_screen"
        
        self.ids.ibs.text = ''
        self.ids.oz.text = ''
        self.ids.floz.text = ''
        self.ids.quart.text = ''
        self.ids.gallon.text = ''
        self.ids.feet.text = ''
        self.ids.yard.text = ''
        self.ids.inch.text = ''
        self.ids.sqyd.text = ''
        self.ids.sqft.text = ''


# class RootWidget(ScreenManager):
#     pass

sm = ScreenManager(transition=NoTransition())
sm.add_widget(MainScreen(name='main_screen'))
Clock.schedule_once(lambda dt: sm.add_widget(ImperialScreen(name='imperial_screen')), 1)


class MainApp(App):
    def build(self):
        # return RootWidget()
        return sm


if __name__ == "__main__":
    MainApp().run()


# trigger event by text change in TextInput:
# in .kv file among TextInput properties add:
# on_text: root.func(self.text)
# in python file in the rule class define a function:
# def func(self, text):
#     [do anything with] text

# def func(self, text):
#         self.ids.enlighten.text = text

# def func(self, text):
#         self.ids.enlighten.text = ""
#         num = int(text)
#         self.ids.enlighten.text = str(num*2)
