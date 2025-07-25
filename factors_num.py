# program to find a factors of a number

# we will write a function for it

def factors_num(num):
    # now we are going to create a list that will store the number which is being divided
    
    lst=[]
    # we will append the other number 1 also here
    lst.append(1)
    # first we are going to try to run it in a loop
    for i in range(2, int(num/2)):
        #we are going to whether the number  is divisible by the other and the remainder which we get itself is a number so both number are it we have used 2 if condition here through both we will add the number
            if(num%i==0):
                if int(i) not in lst: lst.append(int(i))
                if int(num/i) not in lst: lst.append(int(num/i))
     # we will append the number variable number manually  and we will try to return the list also         
    lst.append(num)
    return lst

print(factors_num(15))
