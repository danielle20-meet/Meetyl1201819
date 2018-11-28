from turtle import *
import turtle
import random
import math

class Ball(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)
		


b1 = Ball(20, "blue", 5)
b2 = Ball(15, "red", 5)

def check_col(c1,c2):
	x1=c1.xcor()
	x2=c2.xcor()
	y1=c1.ycor()
	y2=c2.ycor()
	d= math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
	if d>c1.radius+c2.radius:
		print("Yay!")
	else:
		c1.color="pink"
check_col(b1,b2)

turtle.mainloop()
