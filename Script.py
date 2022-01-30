
#Voice Assistant By Sarthak Bhake

#All the modules used in the Project.
import pyttsx3
import speech_recognition as sr
import pyjokes
import datetime
import webbrowser as wb
import os
import smtplib

#initializing the voice of the Assistant
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
print(voices[1].id)
engine.setProperty("voice",voices[0].id)

#Function controlling the speaking
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#Function Created to greet and wish the user.
def wishMe():
    print("Hello! , Welcome!")
    speak("Hello! , Welcome!")
    hour = int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        print("Good Afternoon!")
        speak("Good Afternoon!")
    elif hour>=18 and hour<24:
        print("Good Evening!")
        speak("Good Evening!")
    print("Lorenzo at your service! how can I help you?")
    speak("Lorenzo at your service! how can I help you?")


#Function which accepts the command from the user 
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Please say that again...")   
        speak("Please say that again...")
        return "None"
    return query

#Function which sends email to the desired Email from a single sender
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('bhakesarthak1@gmail.com', "So13@02bha")
    server.sendmail('bhakesarthak1@gmail.com', to, content)
    server.close()

         
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        #created if the user wishes to know the current time. 
        if "time" in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S")    
            speak(f"Sir, the current time is {strTime}")

        #created if the user wishes to know the current date.
        elif "date" in query:
            year = int(datetime.datetime.now().year)
            month = int(datetime.datetime.now().month)
            date = int(datetime.datetime.now().day)
            speak("Sir,the Date is")
            speak(date)
            speak(month)
            speak(year)

        #to accept email from user and pass it to the send email function previously defined
        elif "email" in query:
            try:
                speak("Enter your Email ID")
                to =input("Enter email id:-") 
                print("What should I say?")
                speak("What should I say?")
                content = takeCommand()   
                sendEmail(to, content)
                print("Email has been sent!")
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("I'm sorry. I am not unable to send this email.")
                print("I'm sorry. I am not unable to send this email.")

        #to wish the user a very happy birthday
        elif "birthday today" in query:
            print("Wow! Wish you a very Happy Birthday Sir , may god bless you!")
            speak("Wow! Wish you a very Happy Birthday Sir , may god bless you!")
        
        #to tell a joke to the user when requested
        elif "joke" in query:
            speak(pyjokes.get_joke())
            

        #to open youtube
        elif "youtube" in query:
            url="https://www.youtube.com"
            wb.open(url)

        #to open instagram
        elif "instagram" in query:
            url2="https://www.instagram.com/"
            wb.open(url2)

        #to open news       
        elif "news" in query:
            url3="https://www.wionews.com/"
            wb.open(url3)
        
        elif "play music" in query:
            path=r"C:\Users\Sarthak\Desktop\file_example_MP3_5MG.mp3"
            os.startfile(os.path.join(path))

        #to show the location of the place user says
        elif "where is" in query:
            data = query.split(" ")
            location = data[2]
            speak("Hold on, I will show you where " + location + " is.")
            os.system('cmd /k "start chrome https://www.google.nl/maps/place/"'+ location)

        #to open a notepad file   
        elif "notepad" in query:
            filePath = r"C:\Users\Sarthak\Desktop\MyCountry.txt"
            os.startfile(filePath)  

        #to go offline
        elif "offline" in query:
            print("Shutting down the system")
            speak("Shutting down the system")
            quit()


        






