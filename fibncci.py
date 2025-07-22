# program to print the fibonacci number

# we are going to define a function that will print the fibonacci number

# we have created a variable of fibonacci number
fib_num=0
# another variable of a
a=1
# created a function with limit
def fib_fun(limit):
    
    print(0)
    print(1)
    # the function we have defined globally we are going to use that function local
    global fib_num,a
    # In this function there will be an  limit till that limit we are going to print that function
    for i in range(1,limit ):
        # now we are going to update the variables and created another variable update_num for swapping the variable for fibonacci number
        update_num= fib_num +a
        
        fib_num,a=a,update_num
        
# we are going to print the number
#
        print(update_num)


fib_fun(10)
        

