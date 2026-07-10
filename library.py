
books = [
    ['IT', 'Stephen King']
]

borrowBooks = []

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







def borrowBook():


        print("tell me what fucking book yhou wanan F UCKING read fucking wanker")

        print("")

        try:

                userChoice = input("Enter Book: ")
        
                for book in books:

                    if userChoice in book:
                        
                        borrowBooks.append(book)

                        books.remove(book)

                        print(borrowBooks)

                        break
                        

        except ValueError:
            print("Book not in stock")







def returnBook():


        print("Enter Book you would like to return")

        print("")

        try:

                userChoice = input("Enter Book: ")
                print(borrowBooks)
        
                for book in borrowBooks:

                    if userChoice not in book:
                        
                        books.append(book)

                        borrowBooks.remove(book)

                        print(borrowBooks)

                        break
                        

        except ValueError:
            print("Book not in stock")









def viewBooks(): # Views each book and author (reciept)

    print("Books in stock:")   

    for book in books: #Iterates and loops through boos for book lists

        print("")

        print("Book Title: ",book[0])
        print("Author: ",book[1])

        print("")





while True: # Continues after user completes an option


    userOption = menu()


    if userOption == 1:
        addBook()

    elif userOption == 2:
        borrowBook()

    elif userOption == 3:
        returnBook()

    elif userOption == 4:
        viewBooks()


    elif userOption == 6:
        print("Goodbye")
        break