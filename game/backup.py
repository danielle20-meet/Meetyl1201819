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
colors=["blue","red","green","yellow","black","white","orange","purple","hot pink","aquamarine","crimson"]
Running=True
Sleep=0.0077
score=0
h_scor=0
screen_w=turtle.getcanvas().winfo_width()//2
screen_h=turtle.getcanvas().winfo_height()//2
turtle.penup()
turtle.goto(screen_w,screen_h)
turtle.pensize(5)
for i in range (4):
	turtle.right(90)
	turtle.pendown()
	turtle.forward(screen_w*2)
turtle.penup()
turtle.color(random.choice(colors))
turtle.goto(-100,450)
turtle.write("Welcome!",move=False,align="left",font=("Arial",24,"normal"))
turtle.goto(-250,420)
turtle.write("Your score is:" + str(score)+ " high score: "+str(h_scor),move=False,align="left",font=("Arial",24,"normal"))
num_balls=5
max_r=35
min_r=10
min_dx=-2
max_dx=2
min_dy=-5
max_dy=5
color1 = simpledialog.askstring("Input", "What is your favorite color?", parent=tk.Tk())
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
		if check_col(other,M_ball):
			if other.r>M_ball.r:
				global score,h_scor
				turtle.undo()
				turtle.write(" GAME OVER! your score is: " + str(score)+" high score "+str(h_scor),move=False,align="left",font=("Arial",24,"normal"))#if your ball hit a bigger one
				score=-1
				answer = simpledialog.askstring("Input", "Do you want to play again?", parent=tk.Tk())
				if answer=="yes":
					turtle.undo()
					M_ball.goto(400,400)
					score+=1
					M_ball.r=20
					M_ball.shapesize(M_ball.r/10)
					for i in Balls:
						if i.xcor()>=350:
							i.goto(100,100)
					turtle.write("Your score is:" + str(score)+" high score "+str(h_scor),move=False,align="left",font=("Arial",24,"normal"))
				return False
			elif M_ball.r>other.r: #if your ball hit a smaller one
				if M_ball.r>100: #in order that your ball w'ont be 2 big
					M_ball.r=20
				M_ball.r+=2
				score+=1
				if h_scor<score:
					h_scor=score
				turtle.undo()
				turtle.color(random.choice(colors))
				turtle.write("Your score is:" + str(score)+" high score "+str(h_scor),move=False,align="left",font=("Arial",24,"normal"))
				M_ball.shapesize(M_ball.r/10)
				other.goto(100,100)
				return True
def movearound(event):
	M_ball.goto(event.x-475,405-event.y)
turtle.getcanvas().bind("<Motion>", movearound)

turtle.update()
while score>=0:
	move_balls(Balls)
	turtle.update()
	check_all_balls()
	m_ball_col()
	time.sleep(0.001)
turtle.mainloop()