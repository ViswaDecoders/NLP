import speech_recognition as sr
import pyttsx3

r=sr.Recognizer()

while(1):
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            print("Start speaking ...\n")
            audio = r.listen(source)

            MyText = r.recognize_google(audio)
            MyText = MyText.lower()

            print("Did you say "+MyText+"\n")

    except sr.RequestError as e:
        print('Could not request results; {0}\n'.format(e))

    except sr.UnknownValueError:
        print("Did't get you, pardon ...\n")

    if(MyText == "quit"):
        break
