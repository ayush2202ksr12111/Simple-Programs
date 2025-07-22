# we are writing a program to check whether a number is armstrong or not




def arm_num_cal(x):
  # we will define a sample number that will contain empty
    arm_num=0
    x_mod=x
    x_len = len(str(x_mod))
    for i in range(0, x_len):
      
      div = 10**(x_len-i-1)
      arm_num = arm_num + (int(x_mod/div)**3)
      x_mod=x_mod%div
      if(arm_num==x):
          return True
    return False
 
 
print(arm_num_cal(154))
