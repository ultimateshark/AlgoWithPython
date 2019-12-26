parent={}


def DFS_visit(adj,s):
	global parent
	for v in adj[s]:
		if v not in parent:
			parent[v]=s
			print(v)
			DFS_visit(adj,v)

def DFS(adj):
	global parent
	v=list(adj.keys())
	parent={}
	for s in v:
		if s not in parent:
			parent[s]=None
			print(s)
			DFS_visit(adj,s)

V={1:[4,2],2:[3,5],4:[],5:[6],3:[7],6:[],7:[]}
DFS(V)
