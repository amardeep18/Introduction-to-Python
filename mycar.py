


class Car:
	def __init__(self,color, model):
		self.color = color
		self.model = model
		self.engine = "off"

	def start_engine(self):
		if self.engine == "off":
			print("Starting Engine!")
			self.engine = "on"
		else:
			print("The engine is running already!")

	def stop_engine(self):
		if self.engine == "on":
			print("Stopping Engine")
			self.engine = "off"
		else:
			print("The engine is already off")

	
	def drive(self):
		if self.engine == "on":
			print("Driving the Car!")
		else:
			print("The engine needs to be started first")

	
	def display_car(self):
		print(self.color)
		print(self.model)
		print("The engine is" +self.engine)
