class Library:
    def __init__ (self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books Present In This Library Are:")
        for book in self.books:
            print(" *"  + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it within 30 Days.")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book has already been issued to someone else. Please wait until the book is returned.")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks For Returning this Book! Hope you enjoyed reading it. Have a Good Day!")



class Student:
    def requestBook(self):
        self.book = input("Enter The Name Of The Book You Want to Borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter The Name Of The Book You Want to Return: ")
        return self.book

if __name__ == "__main__":
    centraLibrary = Library(["Algorithms", "Data Structures", "Django", "C++", "HTML CSS JS", "Python Notes", "Algorithms & Analysis" ])
    student = Student()
    # centraLibrary.displayAvailableBooks()

    while (True):
        welcomeMsg = '''======Welcome To Central Library======
        Please Choose an Option:
        1. Listing all the Books.
        2. Request a Book.
        3. Return a Book.
        4. Exit the Library
        '''
        print(welcomeMsg)

        a = int(input("Enter a Choice: "))
        if a == 1:
            centraLibrary.displayAvailableBooks()
        elif a == 2:
            centraLibrary.borrowBook(student.requestBook())
        elif a == 2:
            centraLibrary.returnBook(student.returnBook())
        elif a == 2:
            print("Thanks For Using Central Library. Have a Good Day!")
            exit()
        else:
            print("Invalid Choice!")
