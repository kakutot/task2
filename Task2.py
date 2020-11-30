def outlier(arr):
    if (len(arr) < 3): raise Exception("Array size should be more than 2")

    evens = [x for x in arr if x % 2 == 0]
    odds = [x for x in arr if x % 2 != 0]
    return odds[0] if len(odds) < len(evens) else evens[0]
    
#Testing
print(outlier([1, 4, 4, 4])) 
print(outlier([1, 4, 5, 3])) 