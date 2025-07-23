# write a program to diplay powers of 2 we will try to use recusrsion here to check whether it is possible or not

def power_disp(num):
    for i in range(0, num):
        print(2**(i+1))

print(power_disp_rec(5))
