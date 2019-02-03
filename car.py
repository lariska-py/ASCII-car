from time import sleep
from os import system

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
	x = system('cls')
	return x
speed = 1
distance = 100 # kilometros rodados
for i in range(distance):
  car(i, speed)
  distance -= 1
