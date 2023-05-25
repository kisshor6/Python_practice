class liberary:
    def __init__(self, listOfbooks):
        self.books = listOfbooks

    def displayavailablebooks(self):
        print("books present in library are:")
        for book in self.books:
            print("*" + book)

    def borrowbook(self, bookname):
        self.bookname = bookname
        if bookname in self.books:
            print(f"congratulation {bookname} havenot issued you can take it for 30 days") 
            self.books.remove(bookname)
            return True       
        else:
            print(f"the {bookname} is already issued from our liberary")
            return False

    def returnbook(self, bookname):
        self.books.append(bookname)
        print("thanks for returning this book hope you enjoyed this")
        
class student:
    def requestbook(self):
        self.book = input('enter the name of book that you want to borrow')
        return self.book

    def returnbook(self):
        self.book = input('enter the name of book that you want to return')
        return self.book 

if __name__ =="__main__":
    centralibrary = liberary(['algorithms', 'python','c++','java','php','sql'])
    student = student()
    # centralibrary.displayavailablebooks()
    while (True):
        
        welcomemsg = '''
        =====welcome to the central liberary====
        please choose an one option:
        1.listen all the books
        2.request the books
        3.return the books
        4.exit the liberary
        '''
        print(welcomemsg)
        a = int(input("enter a choice: "))
        if a == 1:
            centralibrary.displayavailablebooks()
        elif a == 2:
            centralibrary.borrowbook(student.requestbook())
        elif a == 3:
            centralibrary.returnbook(student.returnbook())            
        elif a == 4:
            print("thanks to come in this liberary")
            exit()
        else:
            print("invalid choice")

        