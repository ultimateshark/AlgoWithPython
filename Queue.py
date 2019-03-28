import LinkedList as ll

class Queue:
	def __init__(self):
		self.ls=ll.mlist()
	def Insert(self,value):
		if self.ls.head==None:
			self.ls.InsertFirst(val=value)
		else:
			self.ls.InsertEnd(val=value)
	def Delete(self):
		if self.ls.head==None:
			print("Queue UNDER FLOW")
		else:
			self.ls.DeleteBeg()
	def Display(self):
		self.ls.Display()

if __name__ == '__main__':
	newqueue=Queue()
	mode=int(input("Press 1 to Insert\nPress 2 to Delete\nPress 3 to Display\nPress 4 to quit"))
	while True:
		if mode==1:
			newqueue.Insert(value=input("Enter Value To Insert"))
		elif mode==2:
			newqueue.Delete()
		elif mode==3:
			newqueue.Display()
		elif mode==4:
			break
		mode=int(input("Enter Mode"))