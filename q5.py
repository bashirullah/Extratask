inp=input("please enter sentence:")


list=''
for i in inp:
    if i in "a e i o u A I O U" :
        list=list+i
print(list)

print(list[::-1])
