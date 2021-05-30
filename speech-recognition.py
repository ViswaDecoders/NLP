import pandas as pd
import os
from werkzeug.utils import secure_filename

import speech_recognition as sr

DIRNAME = 'F:\\sem - 4\\Distributed real time system - CSE2021\\j component'
#print(DIRNAME)

def get_file_paths(dirname):
    file_paths = []
    for root, directories, files in os.walk(dirname):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths

def process_file(file):
    r = sr.Recognizer()
    a = ''
    with sr.AudioFile(file) as source:
        audio = r.record(source)
        try:
            a = r.recognize_google(audio)
        except sr.UnknownValueError:
            a = "Speech Recognition cound not understand audio"
        except sr.RequestError as e:
            a = "Cound not request results from Speech Recognition service; {0}".format(e)
    return a

greetings = []
filenamee = []
greeting_word = []
files = get_file_paths(DIRNAME)
for file in files:
    filepath, ext = os.path.splitext(file)

    if ext == '.wav':
        file_name = os.path.basename(file)
        filenamee.append(file_name)
        a = process_file(file)

        greetings.append(a)
        if "good morning" in a:
            greeting_word.append('Wow... greeting is there..')
        else:
            greeting_word.append('Sorry.. No greetings...')

#print(greeting_word)
#print(greetings)
#print(filenamee)
print("\n")
dff = pd.DataFrame({'Audio':filenamee, 'text':greetings, 'Result':greeting_word})
dff.index = dff.index+1
print(dff.head(5))

print("\n")
