import LinkedList as ll
class Stack:
	def __init__(self):
		self.ls = ll.mlist()
	def Push(self,value):
		if self.ls.head==None:
			self.ls.InsertFirst(val=value)
		else:
			self.ls.InsertBegining(val=value)
	def Pop(self):
		if self.ls.head==None:
			print("Stack Empty")
		else:
			self.ls.DeleteBeg()
	def Display(self):
		self.ls.Display()

if __name__ == '__main__':
	newstack=Stack()
	mode=int(input("Press 1 to Push\nPress 2 to Pop\nPress 3 to Display\nPress 4 to quit"))
	while True:
		if mode==1:
			newstack.Push(value=input("Enter Value To Push"))
		elif mode==2:
			newstack.Pop()
		elif mode==3:
			newstack.Display()
		elif mode==4:
			break
		mode=int(input("Enter Mode"))