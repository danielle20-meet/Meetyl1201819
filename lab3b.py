#Danielle Weiss
#24.10.18
#a huge curcle
import turtle
turtle.speed(0)
def shape(): #draw the basic shape
	turtle.pendown()
	turtle.forward(120)
	turtle.right(45)
	turtle.forward(75)
	turtle.right(90)
	turtle.forward(50)
	turtle.penup()
	turtle.goto(0,0)
for i in range (720):
	turtle.right(0.5)
	shape()

turtle.mainloop()