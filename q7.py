def find_pairs(x,sum):
    s = set(x)
    avg = sum/2
    if x.count(avg) ==2:
        print (avg, avg)
    s.remove(avg)      
    for i in s:
        diff = sum-i
        if diff in s: 
            print (i, diff)


x = [1,2,3,4,5,6,7,8,9,-1]
sum = 8        
find_pairs(x,sum)