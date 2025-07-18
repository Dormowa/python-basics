'''file_path = 'data.csv'
print(file_path)

file = open(file_path, 'r') # open in write mode
file = open(file_path, 'w') # open in write mod
file = open(file_path, 'a') # open in append mode
file = open(file_path, 'r+') # open in read/write mode'''

# write function will create a new file or overwrite an existing one
file = open("example.txt", "w")
file.write("Hello, World!\n")
file.write("This is line two!\n")
file.close()