"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)

list_of_lists = []

def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:

        parts = [line.strip('\n') for line in line.split(',')]
        parts[2] = int(parts[2])
        list_of_lists.append(parts)
    print(list_of_lists[:2])

    a = list_of_lists[:2]
    b = a[0]
    #print(b)
    c = a[1]
    #print(c)

    print (b[0], "is taught by", b[1], "and has", b[2], "students")
    print (c[0], "is taught by", c[1], "and has", c[2], "students")

    #print(line)  # See what a line looks like
        #print(repr(line))  # See what a line really looks like
        #line = line.strip()  # Remove the \n
       # line = line.strip('\n')
       # parts = line.split(',')  # Separate the data into its parts
      #  print(parts)  # See what the parts look like (notice the integer is a string)


        #parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        #print(parts)  # See if that worked

                # in alternative, if you need to use the file content as numbers
                # inner_list = [int(elt.strip()) for elt in line.split(',')]

        #print("----------")
    input_file.close()


#[['CP1401', 'Ada Lovelace', 192],['CP1404', 'Alan Turing', 98]]


main()


