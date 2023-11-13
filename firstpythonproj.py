import time
import pyttsx3
import calendar
from datetime import datetime
import datetime as dat
import wikipedia
import webbrowser
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import sys

def Time():    #dispaly time 

   
    engine = pyttsx3.init()
    engine.setProperty('rate',100)
    Time=time.strftime('%H:%M:%S')
    print(Time)
    Time=int(time.strftime('%H'))+int(time.strftime('%M'))/60+int(time.strftime('%S'))/3600
    if(0 <= Time < 12):
      engine.say("goodmorning")
      engine.runAndWait()

    elif(12 <= Time < 18):    
      engine.say("goodafternoon")
      engine.runAndWait()
    else:
      engine.say("goodevening")
      engine.runAndWait()
       
       
def leap_year(year):
    import calendar
    
    if(calendar.isleap(year)): print(year,":leap year")
    else: print(year,": non leap year")
    
    
def current_dte():
    
      import calendar
      current_date = dat.date.today()  
      current_month_name = current_date.strftime("%B")    # B for month
      print(calendar.day_name[datetime.today().weekday()],",",datetime.today().day,current_month_name)
      
      
def calendar():         # printing calendar and current date and weekday and leap year
    
     import calendar
     top = pyttsx3.init()
     top.setProperty('rate',100)
     month = int(input("enter month"))
     year = int(input("enter year "))
     engine = calendar.month(year,month)
     print(engine)
     leap_year(year)
     top.say("would you want to see current date if yes write Y")
     top.runAndWait()
     x = input("would you want to see current date if yes write Y")
     x1 = x.capitalize()
     if(x1 == "Y"):
       current_dte()         

        
def searching_speaker():    # seraching something give result with audio

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate',100)
    engine.say("Which voice type do you prefer, a male voice (M) or a female voice (F)?")
    engine.runAndWait()
    v=input("Which voice type do you prefer, a male voice (M) or a female voice (F)?")
    v1= v.capitalize()
    if(v1 == "M"):
     engine.setProperty('voice',voices[0].id)
    else:
     engine.setProperty('voice',voices[1].id)

    engine.setProperty('volume',1000)
    engine.setProperty('rate',110)
    In = input("searching wikipedia/google")
    result = wikipedia.summary(In,sentences = 2)
    print(result)
    engine.say(result)
    engine.runAndWait()

def speech():       # speech about what you type here
    
    engine = pyttsx3.init()  # create an object 
    engine.setProperty('rate',100)
    voices = engine.getProperty('voices')
    engine.say("Which voice type do you prefer, a male voice (M) or a female voice (F)?")
    engine.runAndWait() 
    v=input("Which voice type do you prefer, a male voice (M) or a female voice (F)?")
    v1= v.capitalize()
    if(v1 == "M"):
     engine.setProperty('voice',voices[0].id)
    else:
     engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',110)
    engine.setProperty('volume',1)
    speech = input("write speech what you like :")
    engine.say(speech)
    engine.runAndWait()
    
    
def opensite():
    
    isopen=input("which site : would you like to open")
    webbrowser.open(isopen)
    
    
def phonelocation():
   
    no = input("phone number with country code i.e +12......")
    phone_number = phonenumbers.parse(no)
    print("current country location")
    print(geocoder.description_for_valid_number(phone_number,"en"))
    print(carrier.name_for_number(phone_number,"en"))
    

engine = pyttsx3.init()
engine.setProperty('rate',100)
voices = engine.getProperty('voices') 
engine.setProperty('voice',voices[0].id)
print("\t\t\twelcome to my fantastic project")
print("\t\t\t*******************************\n") 
engine.say("welcome to my fantastic project")   
engine.runAndWait()

  
def choice():
   
   in1 = int(input("1.time 2.calendar 3.searching speaker 4.speech 5.opensite 6. exit 7.phonelocation"))
   return in1

def announce():

   engine = pyttsx3.init()
   engine.setProperty('rate',120)
   voices = engine.getProperty('voices') 
   engine.setProperty('voice',voices[0].id)
   engine.say("choose any one of them among options")   
   engine.runAndWait()

while(True):
    announce()
    match choice():
            
            case 1: 
                    Time()
                    
            case 2: 
                   calendar()
                    
            case 3: 
                    searching_speaker()
                    
            case 4: 
                    speech()
                    
            case 5: 
                    opensite()
            case 6:
                    engine = pyttsx3.init()
                    engine.setProperty('rate',100)
                    engine.say("Thank you for giving your's precious time to view the outstanding project.")
                    engine.runAndWait()
                 
                    sys.exit()
                    
            case 7:
                    phonelocation()
         
            case _:
                    engine = pyttsx3.init()
                    engine.setProperty('rate',100)
                    engine.say("ohh , Invalid option , try again")
                    engine.runAndWait()
                 
        
            
    

     
                 
        
            
    

     
