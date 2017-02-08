def sum_of_digits(number):
    sum = 0
    while(number>0):
        sum = sum+number%10
        number=number//10

    return sum

sum=sum_of_digits(456466)
print(sum)
