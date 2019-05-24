class BinarySearchTree:
	def __init__(self,key=None):
		self.key=key
		self.left=None
		self.right=None
		self.parent=None
		self.height=0

	def Insert(self,key):
		if self.key==None:
			self.key=key
			return
		if key>self.key:
			if self.right==None:
				newnode=BinarySearchTree(key)
				newnode.parent=self
				self.right=newnode
			else:
				self.right.Insert(key)
		elif key<self.key:
			if self.left==None:
				newnode=BinarySearchTree(key)
				newnode.parent=self
				self.left=newnode
			else:
				self.left.Insert(key)

	def __str__(self):
		return self.key

	def Inorder(self):
		if self.key==None:
			return
		if self.left!=None:
			self.left.Inorder()
		print(self.key)
		if self.right!=None:
			self.right.Inorder()

	def Preorder(self):
		if self.key==None:
			return
		print(self.key)
		if self.left!=None:
			self.left.Inorder()
		if self.right!=None:
			self.right.Inorder()

	def Postorder(self):
		if self.key==None:
			return
		if self.left!=None:
			self.left.Inorder()
		if self.right!=None:
			self.right.Inorder()
		print(self.key)

	def Calheight(self):
		l,r=0,0
		if self.left==None and self.right==None:
			return 0
		if self.left!=None:
			l=self.left.Calheight()
		if self.right!=None:
			r=self.right.Calheight()
		h=self.height=max([l,r])+1
		return h

	def Search(self,key):
		if self.key==key:
			#print("Found at height : ",self.height)
			return self
		if self.left!=None:
			sc=self.left.Search(key)
			if sc!=None:
				return sc
		if self.right!=None:
			sc=self.right.Search(key)
			if sc!=None:
				return sc
		return None
	
	def Findreplace(self):
		temp=self
		while True:
			if temp.right==None:
				return temp
			temp=temp.right

	def Delete(self,loc):
		if loc==None:
			print("Not Present")
			return
		if loc.left==None and loc.right==None:
			if loc.parent.left==loc:
				loc.parent.left=None
			elif loc.parent.right==loc:
				loc.parent.right=None
			loc=None
			return
		elif loc.left==None:
			if loc.parent.left==loc:
				loc.parent.left=loc.right
			elif loc.parent.right==loc:
				loc.parent.right=loc.right
			loc=None
			return
		elif loc.right==None:
			if loc.parent.left==loc:
				loc.parent.left=loc.left
			elif loc.parent.right==loc:
				loc.parent.right=loc.left
			loc=None
			return
		else:
			replace=loc.left.Findreplace()
			loc.key=replace.key
			self.Delete(replace)

if __name__ == '__main__':
	tr=BinarySearchTree()
	tr.Insert(32)
	tr.Insert(2)
	tr.Insert(16)
	tr.Insert(33)
	tr.Insert(75)
	print("To Insert Press 1\nFor Inorder Press 2\nFor Preorder Press 3\nFor Postorder Press 4\nFor Search Press 5\nTo Delete Press 6\nTo Quit Press 9\n")
	while True:
		mode=int(input("Enter Mode\n"))
		if mode==1:
			tr.Insert(int(input("Enter Key")))
			tr.Calheight()
		elif mode==2:
			tr.Inorder()
		elif mode==3:
			tr.Preorder()
		elif mode==4:
			tr.Postorder()
		elif mode==5:
			pr=tr.Search(int(input("Enter Key")))
			if pr==None:
				print("Not Found!!!")
			else:
				print("Found at height: ",pr.height)
				if pr.parent!=None:
					print("Parent is : ",pr.parent.key)
		elif mode==6:
			loc=tr.Search(int(input("Enter Key")))
			tr.Delete(loc)
		else:
			exit()
