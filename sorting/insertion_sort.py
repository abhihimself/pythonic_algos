def insertion_sort(alist):
    for index in range(1,len(alist)):
        current_value=alist[index]
        pos=index
        while pos>0 and current_value<alist[pos-1]:
            alist[pos]=alist[pos-1]
            pos=pos-1

        alist[pos]=current_value
    return alist

l=[i*i%2 for i in range(4,0,-1)]
print(l)
insertion_sort(l)
print(l)