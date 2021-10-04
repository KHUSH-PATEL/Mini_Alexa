#AIM: THE AIM IS TO CREATE A ALEXA CODE, WHICH CAN HEAR YOU AND TALK YOU BACK. IT CAN DO VARIOUS FUNCTIONALITY LIKE PLAY MUSIC, TELLS JOKES, DATE-TIME AND MANY MORE.


import speech_recognition as sc    #Used to recognize speech
import pyttsx3                     #python text to speech(it will reply us back)
import pywhatkit                   #contains a youtube function which plays music
import datetime                    #date and time value
import wikipedia                   #contains wikipedia
import pyjokes                     #tells unlimited jokes


listener = sc.Recognizer()
engine = pyttsx3.init()          #engine required to talk for alexa
voices = engine.getProperty('voices')        #different voice MALE/FEMALE
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sc.Microphone() as source:
            print('listening...')
            talk('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)     #listen your voice with the help of google api
            command = command.lower()
            
    except:
        pass
    return command
    

talk('Hey !!! I am your alexa. What can i do for you???...')


while True:
    command=take_command()
    if 'alexa' in command:
        command=command.replace('alexa', '')
        print(command)
        talk(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing' + song)
            pywhatkit.playonyt('song')   #play song on youtube

        if ' date' in command:
            from datetime import date
            today = date.today()
            date = today.strftime("%B %d, %Y")    #format of date
            print('Current date is ' + date)
            talk('Current date is ' + date)

        if 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')    #format of time
            print('Current time is ' + time)
            talk('Current time is ' + time)

        elif 'who is' in command:
            person = command.replace('who is' ,'')
            info=wikipedia.summary(person,1)     #summary
            print(info)
            talk(info)

        elif 'what is' in command:
            thing = command.replace('what is' ,'')    
            info=wikipedia.summary(thing,1)    #summary
            print(info)
            talk(info)

        elif 'where is' in command:
            place = command.replace('what is' ,'')
            info=wikipedia.summary(place,2)    #summary
            print(info)
            talk(info)

        elif 'feeling' in command:
            print(command)
            talk('I am great. hope you are feeling well with my company')

        elif 'joke' in command:
            jokes=pyjokes.get_joke()   #joke
            print(jokes)
            talk(jokes)                

        elif 'stop' in command:
            talk('Shutting down...')
            break

    else:
        print('Please say the command again...')
        talk('Please say the command again...')
