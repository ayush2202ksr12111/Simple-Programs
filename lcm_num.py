# we have created a function that will print an LCM limit of it
def lcm_fun(num,lmt):
    # we have created an empty list here
    lst=[]

# we will create a for loop with its limit 
    for x in range(0,lmt):
    # Code block to execute at least once
# if num is divisible by 2 and giving 0 remainder then it is lcm of 2 same with 3 and 5 and we will append it in list so it will give the list
        if(num%2==0):
            #
          lst.append(2) 
          num=num/2
        elif(num%3==0):
          lst.append(3)
          num=num/3
        elif(num%5==0):
          lst.append(5)
          num=num/5
    
    return lst
    
print(lcm_fun(15,4))
