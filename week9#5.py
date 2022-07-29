def isSorted(lists):
    count = 0
    for i in range(1, len(lists)):
        if lists[i-1]<lists[i] :
            count += 1;
    if count == len(lists)-1:
        return True
    else:
        return False

print(isSorted([1, 2, 3, 5, 6, 3]))    
