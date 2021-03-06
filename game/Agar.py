#Danielle
#Final project!
#8.1.19,30.1.19
#yay!
from turtle import Turtle 
import math
import turtle
import time
import random
import ball
from ball import Ball
import tkinter as tk
from tkinter import simpledialog
turtle.listen()
turtle.tracer(0,0)
turtle.hideturtle()
turtle.bgpic("sea.gif")
colors=["blue","red","green","yellow","black","white","orange","purple","hot pink","aquamarine","crimson"] #list of colors the turtle can be
Running=True
Sleep=0.0077
score=0
h_scor=0
screen_w=turtle.getcanvas().winfo_width()//2
screen_h=turtle.getcanvas().winfo_height()//2
turtle.penup()
turtle.goto(screen_w,screen_h)
turtle.pensize(5)
for i in range (4): #drawing a square
	turtle.right(90)
	turtle.pendown()
	turtle.forward(screen_w*2)
turtle.penup()
turtle.color(random.choice(colors))
turtle.goto(-100,450)
turtle.write("Welcome!",move=False,align="left",font=("Arial",24,"normal"))
turtle.goto(-250,420)
turtle.write("Your score is:" + str(score)+ " high score: "+str(h_scor),move=False,align="left",font=("Arial",24,"normal"))
num_balls=4
max_r=35
min_r=10
min_dx=-2
max_dx=2
min_dy=-5
max_dy=5
color1 = simpledialog.askstring("Input", "What is your favorite color?", parent=tk.Tk().withdraw())
def ran_ball():	
	x=random.randint(-screen_w+max_r,screen_w-max_r)#the other balls
	y=random.randint(-screen_h+max_r,screen_h-max_r)
	while x==0:
		x=random.randint(-screen_w+max_r,screen_w-max_r)
	while y==0:
		y=random.randint(-screen_w+max_r,screen_w-max_r)

	dy=random.randint(min_dy,max_dy)
	dx=random.randint(min_dx,max_dx)
	r=random.randint(min_r,max_r)
	color = (random.random(), random.random(), random.random())
	ball1= Ball(x,y,dx,dy,r,color)
	return ball1


M_ball= Ball(10,10,dx=5,dy=10,r=30,color=color1) #the ball we control
List_my_balls=[] #that's the list of the balls we control
List_my_balls.append(M_ball) 
Balls=[]
for x in range(num_balls):
	ball1=ran_ball()
	Balls.append(ball1)
def move_balls(list_balls): #move the balls
	for i in (list_balls):
		i.move(screen_w,screen_h)
def check_col(c1,c2): #
	x1=c1.xcor()
	x2=c2.xcor()
	y1=c1.ycor()
	y2=c2.ycor()
	d= math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
	if d+10<=c1.r+c2.r:
		return True
	return False
def check_all_balls():

	for c1 in (Balls):
		for c2 in (Balls):
			if check_col(c1,c2):
				if c1.r>c2.r and c1.r!=c2.r: #(!=) so it wont be the same ball
					c1.r+=5
					c1.shapesize(c1.r/10)
					c2.goto(random.randint(-screen_w,screen_w),(random.randint(-screen_h,screen_h)))
					if c2.r>40:
						c2.r=10
				elif c1.r!=c2.r:
					if c2.r>40:
						c2.r=10
					c2.r+=5
					c2.shapesize(c2.r/10)
					c1.goto(random.randint(-screen_w,screen_w),(random.randint(-screen_h,screen_h)))
					

def m_ball_col():
	for other in (Balls):
		for my_b in List_my_balls:
			if check_col(other,my_b):
				if other.r>my_b.r:
					global score,h_scor
					turtle.undo()
					turtle.write(" GAME OVER! your score is: " + str(score)+" high score "+str(h_scor),move=False,align="left",font=("Arial",24,"normal"))#if your ball hit a bigger one
					score=-1
					answer = simpledialog.askstring("Input", "Do you want to play again?", parent=tk.Tk().withdraw())
					if answer=="yes":
						turtle.undo()
						score+=1
						for i in range (len(List_my_balls)): #making all of my balls restart
							List_my_balls[i].r=10
							List_my_balls[i].shapesize(List_my_balls[i].r/10)
							List_my_balls[i].goto(400-(20*i),400-(20*i))
						for i in Balls:
							if i.xcor()>=350:
								i.goto(100,100)
						turtle.write("Your score is:" + str(score)+" high score "+str(h_scor),move=False,align="left",font=("Arial",24,"normal"))
						s= turtle.getscreen()
						s.onkey(space_bar,"space")
					else:
						quit()
					return False
				elif my_b.r>other.r: #if your ball hit a smaller one
					if my_b.r>100: #in order that your ball w'ont be 2 big
						my_b.r=20
					my_b.r+=10
					score+=1#because you ate a ball
					if h_scor<score:
						h_scor=score
					turtle.undo()
					my_b.r=30
					turtle.color(random.choice(colors))
					turtle.write("Your score is:" + str(score)+" high score "+str(h_scor),move=False,align="left",font=("Arial",24,"normal"))#update score
					my_b.shapesize(my_b.r/10)
					other.goto(100,100)
					return True
def movearound(event):
	for i in range (len(List_my_balls)):
		if i==0:
			List_my_balls[i].goto(event.x-475,405-event.y)
		elif i%2==0: #happend if isn't zero
			List_my_balls[i].goto(event.x-475+20*i,405-event.y+20*-i)
		elif i%3==0: #happend if isn't zero
			List_my_balls[i].goto(event.x-475+20*i,405-event.y+20*i)
		else:
			List_my_balls[i].goto(event.x-475+20*-i,405-event.y+20*-i)
turtle.getcanvas().bind("<Motion>", movearound)
def space_bar():
	global List_my_balls
	numb=len(List_my_balls)
	pr_rad=List_my_balls[0].r
	pr_x=List_my_balls[0].xcor()
	pr_y=List_my_balls[0].ycor()
	new_ball=Ball(pr_x-pr_rad+10,pr_y-pr_rad,5,5,pr_rad,"black")
	List_my_balls.append(new_ball)




s= turtle.getscreen()
s.onkey(space_bar,"space")
turtle.update()
turtle.listen()
while score>=0:
	move_balls(Balls)
	turtle.update()
	check_all_balls()
	m_ball_col()
	time.sleep(0.001)

turtle.mainloop()