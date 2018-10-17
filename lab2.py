#danielle weiss
#16.10.2018
#lab 2 lists
# from tkinter import simpledialog
import tkinter as tk
from tkinter import simpledialog
# application_window = tk.Tk()

def FirstLast(list1):
	x=len(list1)
	list2=[]
	list2.append(list1[0])
	list2.append(list1[x-1])
	return(list2)
#maincode
list1=["2",1,2,3,4,5,"hi"]
ret=FirstLast(list1)
print(ret)


#2
list1=[1,2,33,44,5,12,16,78]
for i in (list1):
  	if i<=5:
  		print(i)

#3
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=[]
for i in (a):
	if i in b:
		c.append(i)
print(c)


#4
def prime(n): #input:num output:if its a prime num
    print("jjj")
    for i in range(2,int(n/2)):
        if n%i==0 and n!=i:
            return(False)
        elif i==int(n/2):
            return (True)
answer = simpledialog.askstring("Input", "enter a number", parent=tk.Tk())
p=prime(int(answer))
if p:
	print("Its a prime number")
else:
	print("Its not a prime number")