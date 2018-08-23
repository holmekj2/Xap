import time
import os
import readchar
import sys
import subprocess

i = 0
questions = [
'Pax, tell me about yourself.' , 
'Pax, why do you want to do robotics?',
'Pax, what robotics experience do you have?',
'Pax, What other skills do you have to make it on the robotics team?',
'Pax, how do you see robots helping the world?',
'Pax, other than me do you have robots at home?',
'Pax, thank you for letting me interview you. Good luck with robotics.'
]
f = open("robot2.ascii","r")
robot = f.read()
f.close()


def clear_screen():
  print(chr(27)+'[2j')
  print('\033c')
  print('\x1bc')

def print_robot():
  print robot

def intro_robot():
    speak("My name is Xap (that's Pax spelled backwards). I am a robot built using the Python programming language. I am going to interview Pax today about robotics.")

def slow_print(s):
    j = 0
    while j < len(s):
      #print s[j]
      sys.stdout.write(s[j])
      sys.stdout.flush()
      j += 1
      time.sleep(0.07)
    print

def speak(s):
  #speak = "say " + s
  #os.system(speak)
  clear_screen()
  print_robot()
  subprocess.Popen(['say', s])
  slow_print(s)

def intro():
  print_robot()
  intro_robot()


clear_screen()
intro()

while True:
  #time.sleep(0.1)
  readchar.readchar()
  #clear_screen()
  speak(questions[i])
  #slow_print(questions[i])
  i += 1 

