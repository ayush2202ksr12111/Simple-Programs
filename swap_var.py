#swapping two variables in python
# creating a simple function to swap two variable
def swap_var(a, b):
    a,b = b,a
    return a,b

# creating variables to swap two varible in python
a, b = swap_var(5,6 )

# printing it
print(f"Swapped variable of a is {a} and b is {b}")
