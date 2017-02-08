def decimal_to_binary_recursion(num):

    if num>1:
        decimal_to_binary_recursion(num//2)
    print(num%2)

def decimal_to_binary_stack(num):
    mylist=[]
    while(num>0):
        mylist.append(num%2)
        num=num//2
        zcount,ocount=counter(mylist)
    return (list(reversed(mylist)),zcount,ocount)

def counter(l):
    zcount=0
    ocount=0
    for item in l:
        if item==0:
            zcount+=1
        else:
            ocount+=1
    return zcount,ocount


#decimal_to_binary_recursion(34)
val,zcount,ocount=decimal_to_binary_stack(34)
st="".join([str(i) for i in val])
print(st)
print(zcount,ocount)
