
def remove_duplicates(lst):
    unique_list = []
    seen = set()
    for i in lst:
        if i not in seen:
            unique_list.append(i)
            seen.add(i)

    return unique_list

my_list = [1,1,2,2,3,4,5,5]
print(remove_duplicates(my_list))