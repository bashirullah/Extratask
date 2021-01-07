# Python Program to Put Even and Odd Numbers in Separate List

# Python Program to Put Even and Odd Numbers in Separate List

NumList = []
Even = [2,4,6]
Odd = [1,3,5]

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

for j in range(Number):
    if(NumList[j] % 2 == 0):
        Even.append(NumList[j])
    else:
        Odd.append(NumList[j])

print("Element in Even List is : ", Even)
print("Element in Odd List is : ", Odd)

Even_list_Sum=sum(Even)
print("Even List sum: ",Even_list_Sum)

Odd_list_sum=sum(Odd)
print("Odd list sum is: ")

Even_List_Max=max(Even)
print("Even list Maxis: ",Even_List_Max)

Odd_List_Max=max(Odd)
print("Odd list Maxis: ",Odd_List_Max)
