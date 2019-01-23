#Collisions
#28.11.18
#Danielle Weiss
import turtle
from turtle import *
import random
class Ball(Turtle):
	"""docstring for Ball"""
	def __init__(self, rad,color,speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(rad/10)
		self.rad=rad
		self.color=color
		self.speed(speed)
c1=Ball(10,"blue",10)
c2=Ball(7,"red",10)
def check_col(b1,b2):
	r1=b1.rad
	r2=b2.rad
	x1=b1.xcor()
	x2=b2.xcor()
	y1=b1.ycor()
	y2=y2.xcor()
	if(math.sqrt(math.pow((x1-x2),2)+math.pow((y1-y2),2))>r1+r2):
		print("there is not a Collision")

turtle.mainloop()


