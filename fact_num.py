# find the facetorial of a number

# my favourite thing we will do it through recusrsion

# we have defined a function that will run through it 
def fact_num(num):
    # we will initialize a variable with num as 0
    if num==0:
        # we are going to end the loop here
        return 1
    # here we will start the recursion
    return num*fact_num(num-1)

print(fact_num(4))


