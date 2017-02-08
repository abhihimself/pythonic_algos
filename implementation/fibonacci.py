def fibbo_nacci(n):
    l=[]
    new=0
    f=0
    s=1
    l.append(f)
    l.append(s)
    while(n-2>0):
        new=f+s
        f=s
        s=new
        l.append(new)
        n=n-1
    return l

print(fibbo_nacci(7))