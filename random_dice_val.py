# Now we are going to print random number which will be from 1 to 6 just like a dice

# we are going to import random library module
from random import random

# we are going to define a random number
def rand_num_dice():
   
    for i in range(0,2):
        dice_val = (int)(random()*10)
        if(dice_val<6 ):
            return dice_val+1
            
    return 0
       

print(f"Hey Computer can you give me a random number between 1 to 100 - {rand_num_dice()}")
