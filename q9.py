 
 
inp_str = '12abcbacbaba344ab'


out = {x : inp_str.count(x) for x in set ( inp_str )} 

# printing result 

print ("Occurrence of all characters in GeeksforGeeks is :\n " + str(out)) 
