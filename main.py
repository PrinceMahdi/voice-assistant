import speech_recognition as sr
import wikipedia
import wolframalpha
import datetime
import pyttsx3
import pyjokes
import pywhatkit

r = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            print('P.I.C.O is at your service...')
            audio = r.listen(source)
            command = r.recognize_google(audio)
            command = command.lower()
    except:
        pass
    return command


def run_pico():
    command = take_command()

    print(f'COMMAND: "{command}"')

    if 'play' in command:
        song = command.replace('play', '')
        talk(f'Which {song} would you like me to play?')
        song_name = take_command()
        talk(f'Playing {song_name} now.')
        pywhatkit.playonyt(song_name)

    elif 'what time is it' in command:
        now = datetime.datetime.now().strftime('%I:%M %p')
        talk(f'It is {now}.')

    elif 'what is the date' in command:
        date = datetime.datetime.now().strftime('%A, %B %d, %Y')
        talk(f'The current date is {date}')

    elif 'tell me a joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)

    elif 'tell me about' in command:
        user = command.replace('tell me about', '')
        talk(f'How many sentences would you like? ')
        sentence_command = take_command()
        info = wikipedia.summary(user, int(sentence_command))
        print(info)
        talk(info)

    elif 'i have a question' in command:
        talk('what is your question')
        question = take_command()
        app_id = 'EQARP3-KH2AEKYLTX'
        client = wolframalpha.Client(app_id)
        res = client.query(question)
        answer = next(res.results).text
        talk(answer)


    else:
        talk(f'I didn\'t quite get it.')


run_pico()