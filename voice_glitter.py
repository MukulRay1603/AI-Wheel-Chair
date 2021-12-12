pip installspeechrecognition
pip install pyaudio
pip install pyttsx3
pip install pywhatkit
pip install pyserial


//Then download the pythoncode from hereor copy from below. Head for coding2 step.

import speech_recognition as sr   # voice recognition library
import random                     # to choose random words from list
import pyttsx3                    # offline Text to Speech
import datetime                   # to get date and time
import webbrowser                 # to open and perform web tasks
import serial                     # for serial communication
import pywhatkit                  # for more web automation
from gpiozero import Motor


# Declare robot name (Wake-Up word)
robot_name = 'Glitter'
# random words list
Motion_words = ['Forward', 'Backward', 'Left', 'Right']
Activate_words = ['Go', 'Move', 'Take', 'Turn', 'Slow', 'Fast']
Stop_Words = ['Stop']
# initilize things
engine = pyttsx3.init()                    # init text to speech engine
#voices = engine.getProperty('voices')      #check for voices
#engine.setProperty('voice', voices[1].id)  # female voice
listener = sr.Recognizer()                 # initialize speech recognition API
# connect with NiNi motor driver board over serial communication
try:
   port = serial.Serial("COM15", 9600)
   print("Glitter Chair, connected.")
except:
   print("Unable to connect to Glitter Chair")
def listen():
	""" listen to what user says"""
	try:
		with sr.Microphone() as source:                         # get input from mic
			print("Talk>>")
			voice = listener.listen(source)                     # listen from microphone
			command = listener.recognize_google(voice).lower()  # use google API
			# all words lowercase- so that we can process easily
			#command = command.lower()         
			print(command)
			# look for wake up word in the beginning
			if (command.split(' ')[0] == robot_name):
				# if wake up word found....
				print("[wake-up word found]")
				process(command)                 # call process funtion to take action
	except:
		pass
def process(words):
	""" process what user says and take actions """
	print(words) # check if it received any command
        present_state = 0
	# break words in
	word_list = words.split(' ')[1:]   # split by space and ignore the wake-up word
        


        if word_list[0] == 'stop':
                present_state = 0
                while (present_state):
                motor1.stop()
                motor2.stop()
                goto vc;
	if word_list[0] == 'forward'
                present_state = 1
                while (present_state):
		motor1.forward()
                motor2.forward()
                motor3.forward()
                motor4.forward()
                goto vc;
		return
       if word_list[0] == 'backward'
                present_state = 2
                while (present_state):
		motor1.backward()
                motor2.backward()
                motor3.backward()
                motor4.backward()
                goto vc;
		return
       if word_list[0] == 'left'
                

		motor1.forward()
                motor2.backward()
                motor3.forward()
                motor4.backward()
                goto vc;
		return
       if word_list[0] == 'forward'
  

		motor1.backward()
                motor2.forward()
                motor3.backward()
                motor4.forward()
                goto vc;
		return

# run the app

vc:
while True:
   listen()  # runs listen one time