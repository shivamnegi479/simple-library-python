import datetime
class Library():
    def __init__(self,books,user):
        self.booklist=books
        self.user=user
        landbook={}
    def display(self):
        return self.booklist
    def addbook(self):
        a=input("Enter a book")
        self.booklist.append(a)
        print(f"{a} added in Library by {self.user}")  
        f=open('books.txt','w')
        f.write(f"{datetime.datetime.now()} {a} added by {self.user} \n")
        f.close()
stu1=Library(['c','c++',"java",".net"],'shivam')


stu1.addbook()
print(stu1.display())