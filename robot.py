import time
import os
import readchar
import sys
import subprocess

questions = [
'Pax, tell me about yourself.' , 
'Pax, why do you want to do robotics?',
'Pax, what robotics experience do you have?',
'Pax, What other skills do you have to make it on the robotics team?',
'Pax, how do you see robots helping the world?',
'Pax, other than me do you have robots at home?',
'Pax, thank you for letting me interview you. Good luck with robotics.'
]

#Read in the robot ascii file
f = open("robot2.ascii","r")
robot = f.read()
f.close()


def clear_screen():
  print(chr(27)+'[2j')
  print('\033c')
  print('\x1bc')

#print the robot ascii image
def print_robot():
  print robot

def intro():
    speak("My name is Xap (that's Pax spelled backwards). I am a robot built using the Python programming language. I am going to interview Pax today about robotics.")

#print a string as the robot is talking
def slow_print(s):
    j = 0
    while j < len(s):
      #print s[j]
      sys.stdout.write(s[j])
      sys.stdout.flush()
      j += 1
      time.sleep(0.07)
    print

#Use the macs 'say' command to speak
#Each time we speak, clear the previous screen, redraw robot, and 
def speak(s):
  clear_screen()
  print_robot()
  subprocess.Popen(['say', s])
  slow_print(s)

#Introduce the robot
intro()
#Loop over questions 
for q in questions:
  #Wait for a key to move on
  readchar.readchar()
  #Have the robot ask the question
  speak(q)

