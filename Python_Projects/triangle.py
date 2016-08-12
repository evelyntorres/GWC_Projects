from turtle import *
begin_fill()
def triangle(color):
	pendown()
	pencolor(color)
	speed(1)
	for i in range(3):
		forward(50)
		right(60)
	penup()
	forward(70)
drawtriangle("yellow")
drawtriangle("pink")
drawtriangle("green")