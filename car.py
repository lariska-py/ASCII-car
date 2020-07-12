from time import sleep
from os import system
from sys import argv

def car(b, s):
	line1 = "       .--------."
	line2 = " ____/_____|___ \\___"
	line3 = " O    _   - |   _   ,*"
	line4 = " '--(_)-------(_)--'"
	x = distance
	print(b*' ' + line1)
	print(b*' ' + line2)
	print(b*' ' + line3)
	print(b*'.' + line4 + '.'*x)
	sleep(s)
	clear()

def clear():
	return system('clear')

try:
  speed = int(argv[1])
  distance =  int(argv[2]) # kilometros rodados
except:
  speed = 3
  distance =  10 # kilometros rodados

for i in range(distance):
  car(i, 1/speed)
  distance -= 1
