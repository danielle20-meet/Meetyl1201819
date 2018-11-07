#five
#6.11.18
#Danielle Weiss

class Person():
   def __init__(self, name,age,food,color):#build the person
       self.name = name
       self.food = food
       self.age = age
       self.color=color


   def print_info(self):
       print("My name is " + self.name + ", I'm " + str(self.age) + " years old.")
       print("My favorite food is " + self.food + " and my favorite color is " + self.color)


a = Person("Britney",16, "Pizza","Black")
a.print_info()

b = Person("Jake", 15,"ice cream","Blue")
b.print_info()
#6
class Bear():
	def __init__(self, name):
		self.name=name
		print("A new bear created. Its name is:"+ self.name)
	
	def say_hi(self):
		print("Hi! I’m a bear. My name is "+ self.name)
my_bear = Bear("Danny")
my_bear.say_hi()
#7 a tale about a kid and a bloon
balloons = 5
name = "Ron"
color = "Yellow"
print("This is a tale about "+ str(balloons) + "balloons. The first kid is " + name + " who got a " + color + " balloon")

#8 
# what I want to be printed: Yummy!!! Eating a chocolate cake :)
class Cake():
	def __init__(self,flavor):
		self.flavor = flavor

	def eat(self):
		print("Yummy!!! Eating a", self.flavor, "cake :)")

cake = Cake("chocolate")
cake.eat()

#9 and last
# what I want: my cat to celebrate its 8th birthday (and all the 
# birthdays that come before that)
class Cat(object):
	def __init__(self,name):
		self.name = name
		self.age = 0 
	def birthday(self,age):
		self.age += age
		if self.age >= 100:
			print("Dong dong, the cat is dead!")
		else:
			print(self.name + "hasing its " +str(self.age)+" birthday!")

my_cat = Cat("Salem")
my_cat.birthday(8)
