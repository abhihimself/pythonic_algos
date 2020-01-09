def quick_sort(alist):
    first = 0
    last = len(alist)-1
    quick_sort_helper(alist, first, last)
    print(alist)

def quick_sort_helper(alist, first, last):
    if first<last:
        boundry = partitioner(alist, first, last)
        quick_sort_helper(alist, first, boundry-1)
        quick_sort_helper(alist, boundry+1, last)

def partitioner(alist, first, last):
    pivot = alist[first]
    left_mark = first+1
    right_mark = last
    while left_mark<right_mark:
        while left_mark<=right_mark and alist[left_mark]<pivot:
            left_mark+=1
        while left_mark<=right_mark and alist[right_mark]>pivot:
            right_mark-=1
        if left_mark<=right_mark:
            temp = alist[left_mark]
            alist[left_mark] = alist[right_mark]
            alist[right_mark] = temp
    alist[first] = alist[right_mark]
    alist[right_mark] = pivot
    return right_mark


l = [100, 50, 8908, 4638, 4646, 383]

print(quick_sort(l))