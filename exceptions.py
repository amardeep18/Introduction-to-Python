
myarray = {}

for item in [0,1,2,3,4,5]:
	try:
		print(myarray[item])
	except IndexError:
		print("The element is not in the list")


print("The program continues to run!")
