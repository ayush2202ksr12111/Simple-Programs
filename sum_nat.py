# this is a sum of all natural numbers
# we are adding all the natural number using recursion method such that the output will come fast
# this is the reccursion method for adding number
def sum_nat_rec(num_rng):
    if(num_rng==1):
        return 1
    return num_rng+sum_nat_rec(num_rng-1)

print(sum_nat_rec(6))
    
