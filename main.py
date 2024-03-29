import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib

dict = {"a" : "osama@demonscombat.com" , "b" : "mobeenhasan.hashmi@gmail.com" , "send email to f": "faherhasan@gmail.com", "send email to": "shahzaibquershi@gmail.com" , "send to": "sshashmi23@gmail.com"} #key is important
# mail = dict["mail"]

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com' , 587)
    server.ehlo()
    server.starttls()
    server.login('syedmobeen08@gmail.com' , 'sdr7hr08@A')
    server.sendmail('syedmobeen08@gmail.com', to, content)
    server.close()

def speak(audio):
    engine.say(audio) 
    engine.runAndWait() 

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Mobeen Assistant, how may I can assist you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

if __name__=="__main__" :
    wishme()
    # while 1:
    if 1:
        
        query = takeCommand().lower()

        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif'send email' in query:
            try:
                speak("To whom")
                askingemail = takeCommand()
                mail = dict[askingemail]
                to =  mail
                speak("Please tell content of email or what should I say")
                content = takeCommand()
                sendemail(to, content)
                speak("Email has been sent successfully")
            except Exception as e:
                print(e)
                speak("Sorry can not send the email")
        

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'time please' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Respected person, the time is {strTime}")
            print(strTime) 
        elif 'who i am' in query:
            speak("Mobeen")