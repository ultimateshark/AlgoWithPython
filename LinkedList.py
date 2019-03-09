class Node:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next

class mlist:
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
        newmlist=mlist()
        while True:
            mode=input("Enter Mode")
            if mode=='Stop':
                print("Bye Bye")
                break
            elif mode=='Display':
                newmlist.Display()
            elif mode=='InsertEnd':
                if newmlist.head==None:
                    newmlist.InsertFirst(val=input("Enter value to insert.\n"))
                    continue
                newmlist.InsertEnd(val=input("Enter value to insert.\n"))
            elif mode=='InsertBegining':
                if newmlist.head==None:
                    newmlist.InsertFirst(val=input("Enter value to insert.\n"))
                    continue
                newmlist.InsertBegining(val=input("Enter value to insert.\n"))
            elif mode=='InsertMiddle':
                if newmlist.head==None:
                    newmlist.InsertFirst(val=input("Enter value to insert.\n"))
                    continue
                newmlist.InsertMiddle(val=input("Enter value to insert.\n"),pos=input("Enter Position.\n"))
            elif mode=='DeleteEnd':
                if newmlist.head==None:
                    newmlist.InsertFirst(val=input("Enter value to insert.\n"))
                    continue
                newmlist.DeleteEnd()
            elif mode=='DeleteBeg':
                if newmlist.head==None:
                    newmlist.InsertFirst(val=input("Enter value to insert.\n"))
                    continue
                newmlist.DeleteBeg()
            elif mode=='DeleteATPos':
                if newmlist.head==None:
                    newmlist.InsertFirst(val=input("Enter value to insert.\n"))
                    continue
                newmlist.DeleteATPos(pos=input("Enter Position"))
            else:
                print("Wrong Mode")
    except Exception as e:
        print(str(e))
        pass
