# MY HUGE MISTAKE IS NOT TO THINK ABOUT THE MOST PERFECT SOLUTION
# INSTEAD I JUST START WITH WHAT CONCEPT FLASHES IN MY MIND
# AFTER READING THE QUESTION

# def middle(lst):
#     newlist = []
    
#     for i in range(mylist):
#         if mylist[0] and len(mylist):
#             continue
#         else:
#             newlist.append(mylist[i])
            
#     print(newlist)
    
# mylist = [1,2,3,4]
# middle(mylist)


# AND THIS WAS THE SOLUTION GIVEN BY ELSHAD SIR.

# This thing won't work Yash if you don't think of the best 
# solution for the problem.
    
def middle(lst):
    return lst[1:-1]
    
mylist = [1,2,3,4]
print(middle(mylist))