

books = []




borrowBooks = []




def loadBooks():
        
    with open("book.txt", "r") as file:

        for line in file:

            line = line.strip()      # Removes the newline (\n)

            book = line.split(",")   # Splits "IT,Stephen King"

            books.append(book)


def loadBorrowBooks():
     
    with open("borrow.txt", "r") as file:

        for line in file:

            line = line.strip()      # Removes the newline (\n)

            book = line.split(",")   # Splits "IT,Stephen King"

            borrowBooks.append(book)



def saveBooks():

    with open("book.txt", "w") as file:

        for book in books:

            file.write(book[0] + "," + book[1] + "\n")


def saveBorrowBooks():

    with open("borrow.txt", "w") as file:

        for book in borrowBooks:

            file.write(book[0] + "," + book[1] + "\n")




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

        if userChoice < 1 or userChoice > 6:
            print("Choose numbers 1-6")

        else:

            return userChoice

    except ValueError:
        print("Enter numbers 1-6")





def addBook(): 

    while True:

        try:

            bookTitle = input("Book Title: ")

            bookAuthor = input("Author: ")

            book = [bookTitle, bookAuthor]  # New list to make seperate lists possible inside expenses list

            books.append(book) # New list added to the original list

            print("Book Added!")

            saveBooks()
            saveBorrowBooks()
                
            break

            
        except ValueError:

            print("Invalid Input")







def borrowBook():
        
        if not books:
            print("Books not in stock")

        else:

            print("Enter Book you want to borrow:")

            print("")

            print("Books in stock:")   

            for book in books: #Iterates and loops through boos for book lists

                    print("")
    
                    print("Book Title: ",book[0])
                    print("Author: ",book[1])

                    print("")

            try:

                    userChoice = input("Enter Book: ")

                    
            
                    for book in books:

                        if userChoice in book:
                            
                            borrowBooks.append(book)

                            books.remove(book)

                            print("Enjoy your book!")
                            print("")

                            saveBooks()
                            saveBorrowBooks()

                            break

                    else:
                        print("Book not in stock")
                            

            except ValueError:

                print("")

                print("Book not in stock")

                print("")







def returnBook():
        

        if not borrowBooks:
            print("No books to return")

        else:    
            print("Enter Book you would like to return")

            print("")

            print("Book(s): ")


            for book in borrowBooks: #Iterates and loops through boos for book lists

                    print("")

                    print("Book Title: ",book[0])
                    print("Author: ",book[1])

                    print("")


            try:
        
                
                userChoice = input("Enter Book: ")

            
                for book in borrowBooks:

                    if userChoice in book:
                        
                        books.append(book)

                        borrowBooks.remove(book)

                        print("Book Returned!")

                        print("")

                        saveBooks()
                        saveBorrowBooks()

                        break



                else:
                    print("")

                    print("Invalid Book")

                    print("")
                        

            except ValueError:
                print("Book invalid")








def viewBooks(): # Views each book and author (reciept)

    print("")
    print("Books in stock:")   
    print("")

    for book in books: #Iterates and loops through boos for book lists

        print("")

        print("Book Title: ",book[0])
        print("Author: ",book[1])

        print("")




def searchBook():
    
    print("")



    try:

            userChoice = input("Search Book: ")
            
            print("")

        
            for book in books:

                if userChoice in book:
                            
                    print("")

                    print("Search Results")

                    print("Book Title: ",book[0])
                    print("Author: ",book[1])

                    print("")

                    break

            else:

                print("")

                print("Book not in stock")

                print("")
                    


    except ValueError:
        print("Invalid Book")






loadBooks()
loadBorrowBooks()




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

    elif userOption == 5:
        searchBook()


    elif userOption == 6:
        print("Goodbye")
        break