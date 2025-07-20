# we are going to define a list of program to check whether it is prime or not
def is_prime(lst):
    # we initialize a for loop from 0 to len(lst)
    for i in lst:
        #check that if it is divisible by 2, 3, 5 and gives remainder 0 then it is not prime but we
        if (i%2==0) | ((i%3==0)) | (i%5==0):
            print()
        else:
            print(i)
is_prime([3,7,9,11,2,6,4])     
