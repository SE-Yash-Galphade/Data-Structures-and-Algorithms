

a = int(input("How many Day's Temperature? "))
total = 0 
temp = []

for i in range(a):
    newDay = float(input("Day " + str(i+1) + "'s high temperature: "))
    temp.append(newDay)
    total += temp[i]

avg = round(total/a, 2)
print("\nAverage Temperature = " + str(avg))
   
above = 0
for i in temp:
    if i > avg:
        above += 1

print(str(above) + " day(s) are above Average.")

