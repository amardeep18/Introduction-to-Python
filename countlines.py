


print("Enter a file name: ")

file_name = input()

myfile = open(file_name, "r+")


print("The file is ", len(myfile.read().splitlines()), "lines long")


