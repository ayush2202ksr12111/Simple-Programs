# this is a program to convert binary to decimal using recursion
# we are converting binary number to decimal number using recursion method such that the output will come fast
# we have defined a variable with total 
tot=0
# this is a recursioin function which will convert the binary to decimal
def fact_rec(num):
    global tot
    if(num<=1):
        return 1
    tot+=1
    num=int(num/2)
    return (10**tot*(num%2))+fact_rec(num)

print(fact_rec(25))
    
