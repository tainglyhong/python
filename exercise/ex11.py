"""
    Exercise 11 : Advanced String Sorting
    Write a program that get the input in words from user then sort them with what 
    user want to do by select the option in the menu.
    Note : Inputs from user are stored as list.
    1. 
    
"""
def get_words():
    print(f'Enter your strings one at a time. Press Enter on an empty line to finish.')

    words = []

    while True:
        word = input("Enter word (or press enter to finish) : ").strip()
        if word == "":
            break
        words.append(word)
    
    return words

def choose_sort_option():
    print("\nChoose a sorting option: ")
    print("1. Alphabetical order (case-sensitive)")
    print("2. Alphabetical order (ignoring case)")
    print("3. Reverse alphabetical order")
    print("4. By length (shortest to longest)")

    while True:
        try:
            option = int(input(f'Enter option number (1-4): '))
            if option in[1,2,3,4]:
                return option
            else:
                print("Invalid option. Please choosse a number between 1 to 4.")
                
        except ValueError:
            print("Invalid value. Please Enter the valid number.")
            
def sort_words(words, option):
    if option == 1:
        # alphabetical order (case-sensitive)
        words.sort()
    elif option == 2:
        # alphabetical order (ignoring case)
        # words = ['apple','Apple', 'Banana']
        # words = ['apple','apple', 'banana']
        words.sort(key=str.lower)
    elif option == 3:
        # Reverse 
        words.sort(reverse=True)
    elif option == 4:
        # length
        words.sort(key=len)
        
    return words

def main():
    words = get_words()
    
    if not words:
        print("No words were entered. Exiting...")
        return

    option = choose_sort_option()
    
    sorted_word = sort_words(words=words, option=option)
    
    print("Sorted list: ")
    for word in sorted_word:
        print(word)
        
if __name__ == "__main__":
    main()