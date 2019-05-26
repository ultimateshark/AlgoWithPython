def print_subseq(inp,out):
    if(len(inp)==0):
        print(out)
        return
    print_subseq(inp[1:],out)
    print_subseq(inp[1:],out+inp[0])

def get_subseq(inp,out):
    subs={out}
    if(len(inp)==0):
        return subs
    subs=subs.union(get_subseq(inp[1:],out))
    subs=subs.union(get_subseq(inp[1:],out+inp[0]))
    return subs

if __name__=="__main__":
    inp=input("Enter String")
    print_subseq(inp,"")
    sub=get_subseq(inp,"")
    print(sub)