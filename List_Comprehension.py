# Syntax:
# new_list = [new_item for item in list]

prev_list = [1,2,3,4,5]
new_list = []

for i in prev_list:
    a = i * 2
    new_list.append(a)

print(new_list)

new_List1 = [i * 2 for i in new_list]
print(new_List1)


language = 'Python'
newlist2 = [letter for letter in language]
print(newlist2)


list1 = [10, 20, -90, -56, 54, -99, -1, 0, 21]
newlist3 = [number for number in list1 if number > 0 ]
print(newlist3)

list2 = [10, 20, -90, -56, 54, -99, -1, 0, 21]
newlist4 = [number*number for number in list1 if number < 0 ]
print(newlist4)

sentence = 'My Name is Yash'

def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels

consonants = [i for i in sentence if is_consonant(i)]
print(consonants)


def get_number(number):
    # if number > 0:
    #     return number
    # else:
    #     return 'Negative Number'
    
    return number if number > 0 else 'Negative Number'

mylist = [-1, 15, -95, 66, -87, 1, -78]
mylist2 = [get_number(number) for number in mylist]
print(mylist)
print(mylist2)

# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60
# print(a)

a=[1,2,3,4,5]
print(a[3:0:-1])


fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]
 
fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'
 
sum = 0
for ls in (fruit_list1, fruit_list2, fruit_list3):
    if ls[0] == 'Guava':
        sum += 1
    if ls[1] == 'Kiwi':
        sum += 20
 
print(sum)

data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
def fun(m):
    v = m[0][0]
 
    for row in m:
        for element in row:
            if v < element: v = element
 
    return v
print(fun(data[0]))

# arr = [1, 2, 3, 4, 5, 6]
# for i in range(1, 6):
#     arr[i - 1] = arr[i]
# for i in range(0, 6): 
#     print(arr[i], end = " ")



arr = [[1, 2, 3, 4],
       [4, 5, 6, 7],
       [8, 9, 10, 11],
       [12, 13, 14, 15]]
for i in range(0, 4):
    print(arr[i].pop())


def f(value, values):
    v = 1
    values[0] = 44
t = 3
v = [1, 2, 3]
f(t, v)
print(t, v[0])