parent={}
def DFS_visit(adj,s):
	for v in adj[s]:
		if v not in parent:
			
