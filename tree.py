#Danielle Weiss
#24.10.18
#we draw a tree with recurision
import turtle
turtle.speed(1)
def tree(n):
	if n>10:
		turtle.forward(n)
		turtle.right(20)
		tree(n-10)
		turtle.forward(-n)
		turtle.left(40)
		tree(n-10)
		turtle.right(20)



		
	else: 
		return (n)
tree(100)
turtle.mainloop()
		#turtle.forward(n)
		#turtle.right(20)
		#tree(n-10)	
		#turtle.forward(-2*n)
		#turtle.left(40)
		#tree(n-10)
		#turtle.right(20)