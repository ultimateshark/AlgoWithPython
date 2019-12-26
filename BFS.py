class BFS:
	def __init__(self):
		self.relations={}
	def Exe_bfs(self):
		begin=list(self.relations.keys())[0]
		adj=self.relations
		level={begin:0}
		parent={begin:None}
		i=1
		print(begin)
		frontier=[begin]
		while frontier!=None:
			nextx=[]
			for u in frontier:
				for v in adj[u]:
					if v not in level:
						level[v]=i
						parent[v]=u
						nextx.append(v)
						print(v)
			frontier=None if nextx == [] else nextx
			i+=1


b=BFS()
b.relations={1:[2,4],2:[3],4:[5],3:[6],5:[],6:[]}
b.Exe_bfs()
