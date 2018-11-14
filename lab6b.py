import turtle 
from turtle import Turtle 
class Rectangle(Turtle):
	"""docstring for Rectangle"""
	def __init__(self, width,height):
		Turtle.__init__(self)
		turtle.register_shape("Rectangle", ( (0,0),(width,0),(width,height), (0,height,) ))
		self.shape("Rectangle")
		self.color("light blue")
r1=Rectangle(50,100)
turtle.mainloop()