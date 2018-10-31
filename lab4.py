class Animal(object):
	"""docstring for Animal"""
	def __init__(self,sound,name,age,fav_c):
		self.sound=sound
		self.name=name
		self.age=age
		self.fav_c=fav_c
	def eat(self,food):
		print("Yummy! "+self.name+" is eating "+food)
	def desc(self):
		print(self.name+"is "+str(self.age)+" years old and love the color "+self.fav_c)
	def make_s(self,times):
		print("my sound is "+times*self.sound)
	#print the sound



dolphine=Animal("rr","Danielle",16,"blue")
dolphine.eat("ice cream")
dolphine.desc()
dolphine.make_s(3)#problem 2 extra


		