class laibary:
    def __init__(self,books):
        self.books=books
    def boookslist(self):
        print("The available books are:")
        for i in self.books:
            print(i,end=" ")
    def buybooks(self,buybooks):
        if buybooks in self.books:
            print("thanks for buying")
            self.books.remove(buybooks)
    def retbooks(self,retbooks):
        print("you returned the book safely")
        self.books.append(retbooks)
books=["java","c","c++","python","c#"]
a=laibary(books)
msg="0:display books  1:buy books  2:return books"
while  True:
    print(msg)
    print("enter the choice")
    n=int(input())
    if(n==0):
        a.boookslist()
    elif(n==1):
        print("enter the book you want to buy")
        x=input()
        a.buybooks(x)
    elif(n==2):
        print("enter the book you return")
        x=input()
        a.retbooks(x)
    else:
        print("enter the  valid number") 
        print("thaank you")
        quit()           

                
            

