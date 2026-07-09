
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


while True: # Continues after user completes an option


    userOption = menu()


    if userOption == 1:

        addBook()