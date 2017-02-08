def factorial(num):
    if num <= 1:
        return 1
    else:
        return num*factorial(num-1)

val=factorial(4)
print(val)