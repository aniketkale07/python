my_list = [4, 5, 6, 44, 33, 23]

# find max
def find_max(my_list):
    max_val = my_list[0]  
    for x in my_list:
        if x > max_val:
            max_val = x  
    return max_val 


max_value = find_max(my_list) 
print("The Max is: ", max_value)  
