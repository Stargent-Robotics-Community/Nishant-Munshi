#Simple chatbot that answers general questions
import random
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 10.0)
rate = engine.getProperty('rate')
engine.setProperty('rate', 120)

greetings = ['hey there', 'hello', 'hi', 'hai', 'hey']
question = ['how are you', 'how are you doing']
responses = ['Okay', "I'm fine"]
var1 = ['who made you', 'who created you']
var2 = ['I_was_created_by_Nishant_right_in_his_computer.', 'Nishant', 'Some_guy_whom_i_never_got_to_know.']
var3 = ['who are you', 'what is you name']
cmd1 = ['tell a joke', 'tell me a joke', 'say something funny', 'tell something funny']
jokes = ['Can a kangaroo jump higher than a house? Of course, a house doesn’t jump at all.', 'My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.', 'Doctor: Im sorry but you suffer from a terminal illness and have only 10 to live.Patient: What do you mean, 10? 10 what? Months? Weeks?!"Doctor: Nine.']
cmd2 = ['exit', 'close', 'goodbye', 'nothing']
cmd3 = ['what is your color', 'what is your colour', 'your color', 'your color?']
colrep = ['Right now its rainbow', 'Right now its transparent', 'Right now its non chromatic']
cmd4 = ['what is you favourite colour', 'what is your favourite color']
cmd4 = ['thank you']
repfr4 = ['youre welcome', 'glad i could help you']
while True:
  
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        print("Tell me something:")
        audio = r.listen(source)
        try:
            au= r.recognize_google(audio)
            print("You said:- " + au)
        except sr.UnknownValueError:
            print("Could not understand audio")
            engine.say('I didnt get that.')
            engine.runAndWait()
            
    if au in greetings:
        random_greeting = random.choice(greetings)
        print(random_greeting)
        engine.say(random_greeting)
        engine.runAndWait()
    elif au in question:
        
        engine.say('I am fine')
        engine.runAndWait()
        print('I am fine')
    elif au in var1:
        engine.say('I was made by Nishant')
        engine.runAndWait()
        reply = random.choice(var2)
        print(reply)
    elif au in cmd4:
        print(random.choice(repfr4))
        engine.say(random.choice(repfr4))
        engine.runAndWait()
    elif au in cmd3:
        print(random.choice(colrep))
        engine.say(random.choice(colrep))
        engine.runAndWait()
        print('It keeps changing every micro second')
        engine.say('It keeps changing every micro second')
        engine.runAndWait()
    elif au in cmd4:
        print(random.choice(colrep))
        engine.say(random.choice(colrep))
        engine.runAndWait()
        print('It keeps changing every micro second')
        engine.say('It keeps changing every micro second')
        engine.runAndWait()
    elif au in var3:
        engine.say('I am a bot, my name is Kelly')
        engine.runAndWait()

    elif au in cmd2:
        print('see you later')
        engine.say('see you later')
        engine.runAndWait()
        exit()   
    elif au in cmd1:
        jokrep = random.choice(jokes)
        engine.say(jokrep)
        engine.runAndWait()
    