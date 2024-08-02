
def first_second(my_list):
    max1, max2 = 0, 0
    
    for num in my_list:  
        if num > max1: 
            max2 = max1 
            max1 = num  
        elif num > max2:  
            max2 = num
            
    print(max1, max2)

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
first_second(myList) # 90 87