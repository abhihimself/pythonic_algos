'''
This program shows how to perform binary search with and without recursion
Binary search works on a sorted list that is a precondition
Efficiency=O(logn)
The number of comparisons necessary to get to this point is i where n2i=1n2i=1. Solving for i gives us i=logni=log⁡n.
The maximum number of comparisons
is logarithmic with respect to the number of items in the list. Therefore, the binary search is O(logn)O(log⁡n).
'''

def binary_search(element, alist):
    if not alist:
        return False
    mid_index = (len(alist)-1)//2
    current_item_from_list = alist[mid_index]
    if element==current_item_from_list:
        return True
    elif element>current_item_from_list:
        return binary_search(element, alist[mid_index+1:])
    elif element<current_item_from_list:
        return binary_search(element, alist[:mid_index])

def binary_search_witout_rec(l,target):
    first=0
    last=len(l)-1
    while(first<=last):
        mid =(first+last)//2
        if target>l[mid]:
            first=mid+1
        elif target<l[mid]:
            last=mid-1
        else:
            print(mid)
            return True
    else:
        print("not found")
        return False




l=[1,2,3,4,5]
#result=binary_search_recursive(l,10)
result=binary_search_witout_rec(l,3)
print(result)