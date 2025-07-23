# program to see if it is divisible by another number or not whether the sum is divisible by the given number or not 

# In a function there will be range and a number whether it is divisible by sum or not

# We had created a sum recursion function where we are going to print the sum of all of it in loop
def sum_rec(range):
    if(range==0):
        return 1
    return range+sum_rec(range-1)

# now we are going to create another function where we are going to use another function that will help us print the divisor is sum of all the number function or not
def comp_divis(range, divs):
    if((sum_rec(range)-1)%divs==0):
        return True
    return False
    

print(comp_divis(5,5))
