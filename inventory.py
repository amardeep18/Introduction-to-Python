from json import dumps, loads

class Product:
	
	def __init__(self, name, price):
		self.name = name
		self.price = price
	def to_dict(self):
		return {"name": self.name, "price": self.price}

def load_products():
	try:
		products_file = open("products.json", "r+")
	except IOError:
		return []
	product_json = products_file.read()
	product_data = loads(product_json)
	products = []
	for product in product_data:
		products.append(Product(product['name'], product['price']))
	products_file.close()
	return products

def list_products(products):
	for product in products:
		print("Product ({}): Price: ${}".format(product.name, product.price))

def add_product(name, price):
	new_product = Product(name,price)
	products.append(new_product)

def save_products(products):
	product_save_list = []
	for product in products:
		product_save_list.append(product.to_dict())
	product_file = open("products.json", "w+")
	product_file.write(dumps(product_save_list))
	product_file.close()

products = load_products()
while True:
	print("type 'add' to add a product")
	print("type 'list' to list your existing products")
	print("type 'quit' to quit the program")
	command = input("type a command: ")
	if command == "add":
		name = input("enter a product name: ")
		try:
			price = int(input("enter a product price"))
		except ValueError:
			print("invalid price! try again")
			continue
		add_product(name, price)
	if command == "list":
		list_products(products)
	if command == "quit":
		save_products(products)
		exit()
