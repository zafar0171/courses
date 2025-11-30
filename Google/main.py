# find the duplicates number in the list or array 

# var set = mutableSetOf()
# var duplicates = mutableSetOf()
# for(i in arr.indices)
# if(!set.add(arr[i]))
# duplicates.add(arr[i])



arr = [1, 2, 3, 1, 2, 4, 5, 6, 5, 5,4,4,4,4]


dup = set()
a = []

for i in arr:
    if i not in a:
        a.append(i)
    else:
    	dup.add(i)
    
print(dup)
    


#