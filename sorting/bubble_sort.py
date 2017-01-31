def get_list(input_list):
    return bubble_sorted_list(input_list)

def bubble_sorted_list(input_list):
    for i in range(len(input_list)-1,0,-1):
        for j in range(i):
            if input_list[j]>input_list[j+1]:
                input_list[j],input_list[j+1]=input_list[j+1],input_list[j]

    return input_list
