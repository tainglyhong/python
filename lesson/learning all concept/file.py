'''
"r" => read mode (default)
"w" => write mode (creates a new file or overwrites an existing file)
"a" => append mode (adds to the end of the file)
"b" => binary mode (used for non-text files)  "rb", "wb", "ab"
'''

file_object = open("example.txt", "w")  # Open the file in write mode
# file_object = open(file="example.txt", mode="r")  # Open the file in read mode

file_object.write("Hello, this file is created using Python.\n")  # Write a line to the file
file_object.write("This is the second line.\n")  # Write another line to the file


mul_line = ["line one\n", "line two\n", "line three\n"]  # List of lines to write

file_object.writelines(mul_line)  # Write multiple lines to the file


append_file = open("example.txt", "a")  # Open the file in append mode
append_file.write("This line is appended to the file.\n")  # Append a line
append_file.write("This is a second line appended to the file.\n")  # Append a line



file_object = open("example.txt", "r")  # Open the file in read mode
print(file_object.read())  # Read the entire content of the file and print it
append_file = open("example.txt", "r")  # Open the file in read mode
print(append_file.read())  # Read the entire content of the file and print it

file_object.close()  # Close the file
append_file.close()  # Close the file


with open('test.jpg', 'rb') as image_file:
    image_data = image_file.read()  # Read the binary data of the image
    print(f'{image_data}')

with open('test_copy.jpg', 'wb') as copy_file:
    copy_file.write(image_data)  # Write the binary data to a new file