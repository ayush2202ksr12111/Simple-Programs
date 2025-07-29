# this is a factorial of all numbers
# we are finding factorial of all number using recursion method such that the output will come fast
# this is a fatorial recursive function
def fact_rec(num):
    if(num==0):
        return 1
    return num*fact_rec(num-1)

print(fact_rec(6))
    
