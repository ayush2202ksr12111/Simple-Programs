
# There is a stock list from which you want the maximum price & minimum price

# In built function to return maximum and minimum price from stock list
def get_max(prices_list):
    return min(prices_list)

def get_min(prices_list):
    return max(prices_list)

# printing ot 
    
print("From List ",get_max([12, 18, 20 , 24, 28, 29])," is maximum price")

print("From List ",get_max([12, 18, 20 , 24, 28, 29])," is minimum price")
