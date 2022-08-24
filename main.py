
class Library():
    def __init__(self,list,name):
        self.name=name
        self.booklist=list
        self.landdict={}
    
    def displayBook(self):
        print(f"We Have following book in our library :{self.name}")
        for book in self.booklist:
            print(book)
    
    def lendBook(self,user,book):
        if book not in self.landdict.keys():
            self.landdict.update({book:user})
            print("You can take Book Now")
        else:
            print(f"Book Has been already issued to {self.landdict[book]}")
    def addBook(self,book):
        a=input("Enter a book name")
        if book in self.booklist:
            print("Book already in the list")
        else:
            self.booklist.append(a)
            print("Book has been Updated")
            
    def returnBook(self,book):
        if book in self.landdict.keys():
            self.booklist.remove(book)
            print()
        else:
            print("No book is for return")
        
if __name__=="__main__":
    shivam=Library(['Python','C','C++','Data Structure'],'Hnbgu')
    while True:
        print(f"Welcome to {shivam.name} Libray Please Enter your Choice")
        print('1' ,"for Display book")
        print('2' ,"for lend a book")
        print('3' ,"for add a book")
        print('4' ,"for return book")
        user_Choice=int(input())
        if user_Choice==1: 
            shivam.displayBook()
        elif user_Choice==2:
            print("Please Enter a book that you want")
            book=input()
            user=input("Enter your Name")
            shivam.lendBook(user,book)
        elif user_Choice==3:
            book=print("Enter a book name you want to add")
            shivam.addBook(book)
        elif user_Choice==4:
            book=print("Enter a book name you want to add")
            shivam.returnBook(book)
        else:
            print('Please Try again later')
        
        print("Press q to quit and c to continue")
        user_Choice2=""
        while(user_Choice2 !="q" and user_Choice2 !="c"):
            user_Choice2=input()
            if user_Choice2=="q":
                exit()
            if user_Choice2=="c":
                pass

            
        # if user_Choice==3:
        #     shivam.addBook()
        # if user_Choice==4:
        #     shivam.returnBook()
        
        

