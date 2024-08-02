mylist = [10,20,30,40,50,60,70,80,90]

target = 20
# in operator
# if target in mylist:
#     print(f"{target}is in the list")
# else:
#     print(f"{target} is not in the list")

#Linear Search

def linear_search(p_list, p_value):
    for i, value in enumerate(p_list):
        if value == p_value:
            return 1
    return -1

print(linear_search(mylist, target))


total = 0
count = 0

while(True):
    inp = input("Enter a Number: ")
    if inp == 'done': break

    value = float(inp)
    total = total + value
    count = count + 1
    average = total / count

print("Average: ", average)

