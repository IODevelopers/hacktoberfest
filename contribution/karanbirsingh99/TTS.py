import PySimpleGUI as sg
from gtts import gTTS
from pygame import mixer
import time   
import os


layout = [[sg.Text('Please enter any words you would like to say')],      
          [sg.Input()],      
          [sg.RButton('Read'), sg.Exit()]]      

window = sg.Window('Text to Speech').Layout(layout)      
values = str
while True:      
    event, values = window.Read()      
    if event is None or event == 'Exit':      
        break      
    print(event, values)     
    duration = len(values[0])*0.1
    tts = gTTS(text=values[0], lang='en',slow=False)
    tts.save("text.mp3")
    mixer.init()
    mixer.music.load('D:/Git/Hacktoberfest-1/text.mp3')
    mixer.music.play()
    time.sleep(duration)