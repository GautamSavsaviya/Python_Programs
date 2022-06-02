# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# HarryLibrary = Library(listofbooks, library_name)


# dictionary (books-nameofperson)

# create a main function and run an infinite while loop asking
# users for their input


class Library:

    def __init__(self, listofbooks, nameoflibrary):
        self._listOfBooks = listofbooks.copy()
        self._nameOfLibrary = nameoflibrary
        self._lendRecord = {}

    def display_book(self):
        if self._listOfBooks is None:
            print("\nCurrently library has no books...!")
        else:
            print("\n Our Library have following books: ")
            for book in self._listOfBooks:
                print(f"\t{book}")

    def lend_book(self, nameofbook, nameofperson):
        if nameofbook in self._lendRecord:
            print(f"\n'{nameofbook}' is given to someone else, So we can't able to give you...!")
        else:
            self._lendRecord.update({nameofbook: nameofperson})
            print(f"\n {nameofbook} is given to you...!")
            print("\n You must be return the book on the time, Otherwise you will have to pay some charges.")

    def return_book(self, nameofbook):
        if nameofbook in self._lendRecord:
            self._lendRecord.pop(nameofbook)
            print(f"\n {nameofbook} book in returned...!")

    def add_book(self, books):
        self._listOfBooks.extend(books)
        print("\n Your given book is added into the library....!")


if __name__ == '__main__':
    print("Please Enter your library name: ", end="")
    nameOfLibrary = input()
    print("\n Please enter your book list: ", end="")
    listOfBooks = [book for book in input().split(",")]

    myLibrary = Library(listOfBooks, nameOfLibrary)

    while True:
        print("\n Following are some options from which you select one of them and enter the no. of this option: ")
        print(
            "\n 1) Add books into library \n 2) Display all books list of library \n 3) Lend the book \n 4) Return the book")

        try:
            userChoice = int(input("Please enter your choice here: "))

            match userChoice:
                case 1:
                    addBooksList = [book for book in input("\n Please enter list of books: ").split(",")]
                    myLibrary.add_book(addBooksList)

                case 2:
                    myLibrary.display_book()

                case 3:
                    nameOfPerson = input("\n Please Enter person name that want to borrow the book: ")
                    nameOfBook = input("Please enter book name that you want to borrow: ")
                    myLibrary.lend_book(nameOfBook, nameOfPerson)

                case 4:
                    nameOfBook = input("Please enter book name that you want to return: ")
                    myLibrary.return_book(nameOfBook)

                case _:
                    print("\n Invalid choice..!, Please enter again...!")
                    continue

        except Exception as e:
            print("Error: ", e)
