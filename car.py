class Car:
	
	def __init__(self):
		self.engine = False

	def start_engine(self):
		print("Starting the engine!")
		self.engine = True

	def stop_engine(self):
		print("Turning off the car!")
		self.engine = False

	def drive(self):
		if self.engine:
			print("Driving the Car!")
		else:
			print("You need to start the engine first!")


class BlueCar:
	color = 'Blue'


class Honda(Car, BlueCar):
	model = 'Honda'

	def start_engine(self):
		super().start_engine()
		print("Honda! Start Engine!")


class HondaCivic(Honda):
	model = 'Honda Civic'

