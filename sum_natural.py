# We are going to write a program which will be the sum of natural number

# we are going to create a function that will be the list of natural numbers
def sum_list_num(list_num):
    sum_var=0
    for i in list_num:
        if(i>=0):
            sum_var+=i
    
    return sum_var
    

print(sum_list_num([12,-13,1,-5,22,25,14,78,-54,-32,-990,12]))
