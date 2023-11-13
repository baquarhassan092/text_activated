def Time():    #dispaly time 

    import time
    Time=time.strftime('%H:%M:%S')
    print(Time)
    Time=int(time.strftime('%H'))+int(time.strftime('%M'))/60+int(time.strftime('%S'))/3600
    if(0 <= Time < 12):
      print("goodmorning")

    elif(12 <= Time < 18):    
      print("goodafternoon")
    else:
       print("goodevening")
       
       
def leap_year(year):
    
    import calendar
    if(calendar.isleap(year)): print(year,":leap year")
    else: print(year,": non leap year")
    
    
def current_dte():
    
      import calendar
      from datetime import datetime
      import datetime as dat
      current_date = dat.date.today()  
      current_month_name = current_date.strftime("%B")    # B for month
     # year1 =int(datetime.today().year)
      print(calendar.day_name[datetime.today().weekday()],",",datetime.today().day,current_month_name)
      
      
def calendar():         # printing calendar and current date and weekday and leap year

     import calendar
     from datetime import datetime
     import datetime as dat
     month = int(input("enter month"))
     year = int(input("enter year "))
     engine = calendar.month(year,month)
     print(engine)
     leap_year(year)
     x = input("would you want to see current date if yes write Y")
     x1 = x.capitalize()
     if(x1 == "Y"):
       current_dte()         

        
def searching_speaker():    # seraching something give result with audio

    import pyttsx3
    import wikipedia
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('volume',1000)
    engine.setProperty('rate',110)
    In = input("searching wikipedia/google")
    result = wikipedia.summary(In,sentences = 3)
    print(result)
    engine.say(result)
    engine.runAndWait()

def speech():       # speech about what you tpye here
    
    import pyttsx3
    engine = pyttsx3.init()  # create an object to acess module
    engine.setProperty('rate',90)
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('volume',1)
    speech = input("write speech what you like :")
    engine.say(speech)
    engine.runAndWait()
    
    
def opensite():
    
    import webbrowser
    isopen=input("which site : would you like to open")
    webbrowser.open(isopen)
    
    
def phonelocation():
    
    import phonenumbers
    from phonenumbers import geocoder
    from phonenumbers import carrier
    no = input("phone number with country code i.e +12......")
    phone_number = phonenumbers.parse(no)
    print("current country location")
    print(geocoder.description_for_valid_number(phone_number,"en"))
    print(carrier.name_for_number(phone_number,"en"))
    
    
print("\t\t\twelcome to my unqiue project")
print("\t\t\t****************************\n")   
def choice():
    
   in1 = int(input("1.time 2.calendar 3.searching speaker 4.speech 5.opensite 6. exit 7.phonelocation"))
   return in1
import sys
while(True):

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
                    sys.exit()
                    
            case 7:
                    phonelocation()
         
            case _:
                     print("Invalid option")
                 
        
            
    

     