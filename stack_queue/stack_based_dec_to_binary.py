import stack_implementation

def dec_to_bin(dec_num):
    stack=stack_implementation.Stack()

    while(dec_num>0):
        remainder=dec_num%2
        stack.push(remainder)
        dec_num=dec_num//2

    bin_num=""

    while not stack.isEmpty():
        bin_num=bin_num+str(stack.pop())

    return bin_num


print(dec_to_bin(42))



