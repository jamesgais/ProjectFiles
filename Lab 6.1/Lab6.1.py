

def print_file(file_spec):
    #This function prints the contents of our data file to the screen.

    #Print the Header Line and add a space.

    file_reader = open(file_spec, 'r')
    a,b = file_reader.readline().rstrip('\n').split(" ")
    print(f"{a:12}{b:12}\n")


    #continue reading and printing the remainder of the file.

    for line in file_reader:
        a,b = line.strip('\n').split(" ")
        print(f"{a:12}{b:12}")

    file_reader.close()


def add_person(file_spec):
    #prompts the user for their first, middle, and last name. Concatenates them, then appends them to the end of thie file.
    pass

def remove_person(person_to_remove,file_spec):
    #removes the person from the file. Write everyone back to the file except this person.
    pass

def main():
    file_name = "data.txt"
    print_file(file_name) 

    #Part #1 Add a new person

    #Your code goes here

    #Show that the peron was added
    print_file(file_name)

    #Part #2 Remove a person by last name.

    #Your code goes here

    #show the person was removed
    print_file(file_name)

main()
