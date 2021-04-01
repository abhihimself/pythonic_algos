def mergeSort(alist):
    if len(alist) > 1:
        pivot = len(alist)//2
        left_half = alist[:pivot]
        right_half = alist[pivot:]
        mergeSort(left_half)
        mergeSort(right_half)
        left_list_index = 0
        right_list_index = 0
        main_list_index = 0

        while left_list_index < len(left_half) and right_list_index < len(right_half):
            if left_half[left_list_index] <= right_half[right_list_index]:
                alist[main_list_index] = left_half[left_list_index]
                left_list_index += 1
            else:
                alist[main_list_index] = right_half[right_list_index]
                right_list_index += 1
            main_list_index += 1

        while left_list_index < len(left_half):
            alist[main_list_index] = left_half[left_list_index]
            left_list_index += 1
            main_list_index += 1

        while right_list_index < len(right_half):
            alist[main_list_index] = right_half[right_list_index]
            right_list_index += 1
            main_list_index += 1




alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)
