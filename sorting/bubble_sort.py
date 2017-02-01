def get_list(input_list):
    return bubble_sorted_list(input_list)

def bubble_sorted_list(input_list):
    # for any n numbers there will be n-1 pairs
    #Thats why we will run the loop n-1 to 0
    for i in range(len(input_list)-1,0,-1):
        for j in range(i):
            if input_list[j]>input_list[j+1]:
                input_list[j],input_list[j+1]=input_list[j+1],input_list[j]

    return input_list
