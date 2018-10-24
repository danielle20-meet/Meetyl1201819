#Danielle Weiss
#24.10.18
#we draw a tree with recurision
import turtle
def tree(n):
	if n>10:
		turtle.forward(n)
		turtle.right(25)
		tree(n-10)	
		turtle.forward(-n)
		turtle.left(75)
		tree(n-10)


		
	else: 
		return (n)
tree(100)
turtle.mainloop()