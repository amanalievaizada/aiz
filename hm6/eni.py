from turtle import *


sc = Screen()
sc.setup(700,700)
speed(30)
setpos(300,50)
color('green')
bgcolor('black')
i = 200
while i >0:
    left(i)
    forward(i+3)
    i-=1
