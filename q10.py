# input the list
A=(1,2,3,4,5,6,7,8,9,10)

# create two empty lists to store EVEN and ODD elements
B=[]
c=[]

for j in A:
    if j%2==0:
        B.append(j)
    else:
        c.append(j)
        
print('List of even number: ',B)
print('List of odd number: ',c)