from turtle import *
import turtle
import random
import math
turtle.tracer(0)

class Ball(Turtle):
	def __init__(self, radius, color, speed,dx,dy):
		Turtle.__init__(self)
		self.penup()
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)
		self.dx=dx/20
		self.dy=dy/20
	def move(self):
		self.goto(self.xcor()+self.dx,self.ycor()+self.dy)
	def check_b(self):
		if self.xcor()-self.radius<=-300 or self.xcor()+self.radius>=300:
			self.dx=-self.dx
		elif self.ycor()-self.radius<=-300 or self.ycor()+self.radius>=300:
			self.dy=-self.dy

b1 = Ball(20, "blue", 5,1,5)
b2 = Ball(15, "light blue", 5,5,1)
b2.goto(200,200)
list1=["red","yellow","green","blue","orange","black","purple","light blue","turquoise"]
turtle.penup()
turtle.pensize(5)
turtle.goto(300,300)
turtle.speed(0)
for i in range (4):
	turtle.pendown()
	turtle.right(90)
	turtle.forward(600)
turtle.penup()
turtle.goto(0,0)
turtle.shape("circle")
turtle.shapesize(3)
turtle.color("black")
def check_col(c1,c2):
	x1=c1.xcor()
	x2=c2.xcor()
	y1=c1.ycor()
	y2=c2.ycor()
	d= math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
	if d<=c1.radius+c2.radius:
		c1.dx,c2.dx=random.randint(0,5)/20,random.randint(5,10)/20
		c1.dy,c2.dy=random.randint(5,10)/20,random.randint(0,5)/20
		if c1.radius>c2.radius:
			c2.color(random.choice(list1))
			c2.goto(random.randint(-300,300),random.randint(-300,300))
			c2.radius=random.randint(10,30)
			c2.shapesize(c2.radius/10)
		elif c2.radius>c1.radius:
			c1.color(random.choice(list1))
			c1.goto(random.randint(-300,300),random.randint(-300,300))
			c1.radius=random.randint(10,30)
			c1.shapesize(c2.radius/10)
def getxy(event):
	turtle.goto(event.x-475,405-event.y)

turtle.getcanvas().bind("<Motion>",getxy)
turtle.listen()

while True:
	b1.move()
	b2.move()
	check_col(b1,b2)
	b1.check_b()
	b2.check_b()
	turtle.update()
	







turtle.mainloop()