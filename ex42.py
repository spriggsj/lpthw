## Animal is -a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass
	
## is a
class Dog(Animal):
	def __init__(self, name):
		## has a
		self.name = name
		
## is a
class Cat(Animal):
	def __init__(self, name):
		## has a
		self.name = name
		

## is a		
class Person(object):
	def __init__(self, name):
		## has a
		self.name = name
		
## is a
class Employee(Person):
	def __init__(self, name, salary):
		## has a
		super(Employee, self).__init__(name)
		## has a
		self.salary = salary
		
## is a
class Fish(object):
	pass
	
## is a
class Salmon(Fish):
	pass
	
## is a
class Halibut(Fish):
	pass
	
## has a
rover = Dog("Rover")

## has a
satan = Cat("Satan")

## has a
mary = Person("Mary")

## has a
mary.pet = satan

## has a
frank = Employee("Frank", 120000)

## is a a
frank.pet = rover

## is a
flipper = Fish()

## is a
crouse = Salmon()

## is a
harry = Halibut()

