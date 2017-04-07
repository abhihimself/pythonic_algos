def sum_rec(l):
    if len(l)==1:
        return l[0]
    else:
        return l[0]+sum_rec(l[1:])

a=[1,2,3]
print(sum_rec(a))