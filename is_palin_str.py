# We are going to check that whether this palindrome of another function that is available or not
# In first function we are just going to reverse the string and check whether it will give the reverse value or not
def rev_str(str):
    # we are going to create a variable that will determine its length
    str_len = len(str)
    # we are going to determine an empty reverse string to check whether it is good or not
    rev_str=""
    # we are going to determine the for loop for it to check with range 0 till the length of the string 
    for i in range(0, str_len):
        # we are just taking the last character from the string and using concatenation feature to add it to the string
        rev_str+=str[str_len-i-1]
    # now we are going to reverse the string
    return rev_str

# now we are going to create another function that whether it is Palindrome we already have reverse string function and we need to check whether this function gives the true or not in comparision
def isPal(str):
    if(rev_str(str)==str):
        return True
    return False

print(isPal("deed"))
