
books = []

def menu():
    print("Welcome to the Library")

    print("")

    print("1: Add Book")
    print("2: Borrow Book")
    print("3: Return Book")
    print("4: View Books")
    print("5: Search Book")
    print("6: Exit")

    print("")


    try:
        userChoice = int(input("Enter Options 1-6: "))
        return userChoice

    except ValueError:
        print("Enter numbers 1-5")


def addBook(): 

    while True:

        try:

            bookTitle = input("Book Title: ")


            bookAuthor = input("Author: ")

            book = [bookTitle, bookAuthor]  # New list to make seperate lists possible inside expenses list

            books.append(book) # New list added to the original list

            print("Book Added!")
                
            break

            
        except ValueError:

            print("Invalid Input")


def viewBooks(): # Views each expense (reciept)

    print("Books in stock:")   

    for book in books: #Iterates and loops through expenses for expense lists

        print("")

        print("Book Title: ",book[0])
        print("Author: ",book[1])

        print("")


while True: # Continues after user completes an option


    userOption = menu()


    if userOption == 1:

        addBook()

    elif userOption == 4:
        viewBooks()


    elif userOption == 6:
        print("Goodbye")
        break