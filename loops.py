
def print_list(mylist):
	for element in mylist:
		if element == 4:
			continue
		print(element)

def sum_list(mylist):
	list_sum = 0
	for number in mylist:
		list_sum = list_sum + number
	return list_sum

def list_contains(mylist, element):
	for el in mylist:
		if el == element:
			print("Yes!")
			break


print_list([2,4,6,8])
