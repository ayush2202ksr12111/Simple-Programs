# Program to display multiplication of a table

#Enter list of number and then move it using for loop

def mult(num, rang):
    # we have created a for that will help printing the number
    for i in range(1, rang+1):
        # this will print the function
        print(f"The multiplication of {i} * {num} = {i * num}")

mult(3,10)

        
