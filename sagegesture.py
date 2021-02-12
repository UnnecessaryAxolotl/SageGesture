# import kivy module     
import kivy   
import sys, os

UNAME = "lorem"
# base Class of your App inherits from the App class.     
# app:always refers to the instance of your application    
from kivy.app import App  
caroSize = len(os.listdir('c:/users/' + UNAME + '/Pictures/caro/'))

# this restrict the kivy version i.e   
# below this kivy version you cannot   
# use the app or software   
kivy.require('1.9.0')

from kivy.uix.image import AsyncImage
from kivy.clock import Clock
from kivy.uix.carousel import Carousel 
  
Timing = int(input("Seconds per frame: "))
# Create the App class 
class CarouselApp(App): 
    def build(self): 
  
        # Add carousel 
        # And add the direction of swipe 
        carousel = Carousel(direction ='right') 
  
        # Adding 10 slides 
        for i in range(caroSize): 
            src = "c:/users/' + UNAME + '/Pictures/caro/%d.png" %i 
            # using Asynchronous image             
            image = AsyncImage(source = src, allow_stretch = True) 
            carousel.add_widget(image)
        Clock.schedule_interval(carousel.load_next, Timing)
        return carousel 
  
# Run the App 
CarouselApp().run() 
