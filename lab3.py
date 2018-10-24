#danielle weiss
#24.10.18
#turtles shapes
import turtle
colors=["red","yellow","green","blue","purple"]
num=0
for i in range (5): #draw a star
	turtle.color(colors[i])
	turtle.forward(100)
	turtle.left(216)
	num+=1

turtle.mainloop()