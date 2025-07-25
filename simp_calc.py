# we will try to make a simple program that will do nothing but calculate here

def calc_sim():
    # we will use two simple input variable here
    val_1 = int(input("Enter your first value"))
    val_2 = int(input("Enter your second value"))
    # now we will choose what type of operation will be performed here
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    calc_opt = int(input("Choose one of the following for operation"))
    # this is simple program that will choose what operation we have performed here
    if(calc_opt==1):
        return f"Additon of two number is {val_1+val_2}"
    elif(calc_opt==2):
        return f"Subtraction of two number is {val_1-val_2}"
    elif(calc_opt==3):
        return f"Multiplication of two number is {val_1*val_2}"
    elif(calc_opt==4):
        return f"Division of two number is {int(val_1/val_2)}"
    else:
        return f"Wrong option"
print(calc_sim())
