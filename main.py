import pyttsx3   
engine = pyttsx3.init() 
while True: 
    text = input('What do you want me to say?\n') 
    if text == 'q':
        bye = "Bye Bye Friend"
        engine.say(bye)
        engine.runAndWait()
        break
    engine.say(text)   
    engine.runAndWait()  
