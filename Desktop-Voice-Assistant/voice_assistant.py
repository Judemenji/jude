import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import smtplib
import pywhatkit
import pyjokes
import PyPDF2
import time
import sys

print("Your Assistant is starting......")

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 190)

Master="Your Name"  # when you start using the assistant enter your name here

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wish_user():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!" + Master)
        
    elif hour>=12 and hour<16:
        speak("Good Afternoon!" + Master)
        
    else:
        speak("Good Evening" + Master)
        
    speak("I am your Desktop-Assistant! How may I help you?")
    
def user_command():
    # takes microphone command and converts to string
    
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening....")
        r.pause_threshold=1
        audio=r.listen(source)
        
    try:
        print("Recognising.....")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
        
    except Exception as e:
        print("I am sorry I don't understand, Say that again please...")
        return "None"
    return query

def mailSent(to, content):
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email', 'your app password')  # when you start working with the assistant, save this on your device
    #check important.txt for creating an app password
    server.sendmail('Your email',to,content)
    
    server.close()
    
def reader():
    file= open('enter the pdf name','rb')   #for example: open('abc.pdf','rb')
    pdfReader=pyPDF2.Pdffilereader(file)
    pages=pdfReader.numPages
    speak(f"There are {pages} pages in this book")
    speak("which page you want me to read")
    pg=int(input("Enter the page number: "))
    page=pdfReader.getPage(pg)
    text=page.extractText()
    speak(text)

if __name__=='__main__':

    wish_user()
    while True:
        query= user_command().lower()

        if 'wikipedia' in query:
            speak('Give me sometime I am looking into Wikipedia')
            query= query.replace("wikipedia","")
            results= wikipedia.summary(query, sentences=5)
            speak("This is what I found!")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'search google' in query:
            search=user_command.lower()
            webbrowser.open(f"{search}")

        elif 'play music' in query:
            webbrowser.open("spotify.com")
            # you can use API as well, with the help of spotipy module

        elif 'time' in query:
            time= datetime.datetime.now().strftime("%H:%M")
            speak(f"Its {time} now")

        elif 'date' in query:
            date=datetime.datetime.today().strftime("%DD-%MM")
            speak(f"Today's is {date}")

        elif 'send email' in query:
            try:
                speak("please tell me the content of the email")
                content=user_command()
                speak(content)
                to=input()
                speak(to)
                mailSent(to, content)
                speak(f"successfully sent the email to {to}")
            except exception as e:
                print(e)
                speak("sorry! i was unable to send the mail")
                
        elif 'send whatsapp message' in query:    #you should be logged in into whatsapp web for this
            speak("To whom should I send the message?")
            number=int(input())
            speak("Tell me the message please")
            message=user_command()
            kit.sndwhatmsg(number,message)
            
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            
        elif 'make me laugh' in query:
            joke=pyjokes.get_joke()
            speak(joke)
            
        elif 'read for me' in query:       #this basically acts as an audiobook
            reader()
        
        elif 'no thanks' in query:
            speak("thanks for using me! Have a good day")
            sys.exit()
            
        time.sleep(5)
        speak("do you have any other work?") 