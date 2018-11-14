#hi meet
#Danielle weiss
#14.11.18
#Inheritance
#1
import turtle 
from turtle import Turtle
turtle.colormode(255)
from lab6b import Rectangle
import random

class Square(Rectange):
	"""gets a size"""
	def __init__(self, size):
		Rectangle.__init__(self,size,size)
		self.color("blue")
	def random_color(self):
		a=random.randint(1,255)
		b=random.randint(1,255)
		c=random.randint(1,255)
		self.color(a,b,c)
s1=Square(10)
s1.random_color()
turtle.mainloop()


