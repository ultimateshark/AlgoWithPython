class Node:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next

class list:
    def __init__(self):
        self.head=None
    def Insert(self):
        while True:
            val=input("Enter the Value to be insert")
            if self.head==None:
                newNode=Node(val=val,next=None)
                self.head=newNode
            else:
                temp=self.head
                while  temp.next!=None:
                    temp=temp.next
                newNode=Node(val=val,next=None)
                temp.next=newNode
            if input("Do you want to insert more!!!")!="y":
                break
    def Display(self):
        if self.head==None:
            print("Empty")
        else:
            temp=self.head
            while temp!=None:
                print(temp.val)
                temp=temp.next

if __name__=="__main__":
    newList=list()
    newList.Insert()
    newList.Display()
