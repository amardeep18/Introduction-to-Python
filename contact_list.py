class Contact:

	def __init__(self, first, last):
		self.first_name = first
		self.last_name = last
		self.full_info = first+" "+last
	
	def print_info(self):
		print(self.full_info)

	def send_message(self):
		pass

class EmailContact(Contact):
	
	def __init__(self, first, last, email):
		super().__init__(first,last)
		self.email = email
		self.full_info = email+": "+first+ " "+ last

class PhoneContact(Contact):
	def __init__(self, first,last,phone):
		super().__init__(first,last)
		self.phone = phone



sum_list = open('sumlist', 'r').read().splitlines()
sumlist = open('sumlist', 'w')
for number in sum_list:
        sumlist.write(str(number)+"\n")
sumlist.close()
:wq
