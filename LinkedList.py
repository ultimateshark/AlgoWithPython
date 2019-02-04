class Node:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next

class list:
    def __init__(self):
        self.head=None
    def InsertFirst(self,val):
        newNode=Node(val=val,next=None)
        self.head=newNode
    def InsertEnd(self,val):
        temp=self.head
        while  temp.next!=None:
            temp=temp.next
        newNode=Node(val=val,next=None)
        temp.next=newNode
    def InsertBegining(self,val):
        newNode=Node(val=val,next=self.head)
        self.head=newNode
    def InsertMiddle(self,val,pos):
        newNode=Node(val=val,next=None)
        temp=self.head
        for i in range(1,pos):
            if i<pos-1 and temp==None:
                print("Invalid Position")
                return
            temp=temp.next
        newNode.next=temp.next
        temp.next=newNode
    def DeleteEnd(self):
        temp=self.head
        while temp.next.next!=None:
            temp=temp.next
        temp.next=None
    def DeleteBeg(self):
        self.head=self.head.next
    def DeleteATPos(self,pos):
        temp=self.head
        for i in range(0,pos):
            if i<(pos-1) and temp==None:
                print("Invalid Position")
                return
            temp=temp.next
        if temp.next==None:
            print("Invalid Position")
            return
        temp.next=temp.next.next
    def Display(self):
        if self.head==None:
            print("Empty")
        else:
            temp=self.head
            while temp!=None:
                print(temp.val)
                temp=temp.next

if __name__=="__main__":
    try:
        print("Mode:\nInsertEnd\nInsertBegining\nInsertMiddle\nDeleteEnd\nDeleteBeg\nDeleteATPos\nDisplay\nStop\n")
        newList=list()
        while True:
            mode=input("Enter Mode")
            if mode=='Stop':
                print("Bye Bye")
                break
            elif mode=='Display':
                newList.Display()
            elif mode=='InsertEnd':
                if newList.head==None:
                    newList.InsertFirst(val=input("Enter value to insert.\n"))
                    continue
                newList.InsertEnd(val=input("Enter value to insert.\n"))
            elif mode=='InsertBegining':
                if newList.head==None:
                    newList.InsertFirst(val=input("Enter value to insert.\n"))
                    continue
                newList.InsertBegining(val=input("Enter value to insert.\n"))
            elif mode=='InsertMiddle':
                if newList.head==None:
                    newList.InsertFirst(val=input("Enter value to insert.\n"))
                    continue
                newList.InsertMiddle(val=input("Enter value to insert.\n"),pos=input("Enter Position.\n"))
            elif mode=='DeleteEnd':
                if newList.head==None:
                    newList.InsertFirst(val=input("Enter value to insert.\n"))
                    continue
                newList.DeleteEnd()
            elif mode=='DeleteBeg':
                if newList.head==None:
                    newList.InsertFirst(val=input("Enter value to insert.\n"))
                    continue
                newList.DeleteBeg()
            elif mode=='DeleteATPos':
                if newList.head==None:
                    newList.InsertFirst(val=input("Enter value to insert.\n"))
                    continue
                newList.DeleteATPos(pos=input("Enter Position"))
            else:
                print("Wrong Mode")
    except Exception as e:
        print(str(e))
        pass
