#OOP=Object Oriented Programming
#31.10.18
#Danielle Weiss
#Hi Meet
class Person(object):
	"""docstring for Person"""
	def __init__(self, name,age,city):
		self.name=name
		self.age=age
		self.city=city
	def eat(self,breakfast):
		print("I'm eating "+ breakfast+" for breakfast")#eating
	def climb(self,person):
		print("I'm climbing with "+person)
Danielle=Person("Danielle",15.75,"jerusalem")#new object named Danielle
Danielle.climb("a")