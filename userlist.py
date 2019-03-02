




user_list = []


while True:
	user_input = input()
	if user_input == 'exit':
		break
	elif user_input == 'list':
		print(user_list)
	elif user_input == 'pop':
		print(user_list.pop())
	else:
		user_list.append(user_input)
