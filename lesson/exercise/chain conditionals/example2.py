# Test out filenames of different lengths. Which filenames fall into the else case?
filename = input("What would you like to name the photo? ")

if len(filename) < 3 or len(filename) > 20:
    # Clear out the filename if it's invalid.
    filename = ""
    print("Filename must be between 3 and 20 characters.")
else:
    # Photos are stored as JPEGs, so we add the file extension.
    filename = filename + ".jpeg"
    print("The file has been renamed to " + filename)