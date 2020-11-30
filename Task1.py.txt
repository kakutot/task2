RANK_DEL = 10

def digits(natural): 
    res = []
    while (natural > 0):
        left = natural % RANK_DEL 
        natural = natural // RANK_DEL 
        res.append(left)
    return res[::-1]

def digitsCount(natural):
    return len(digits(natural))

def digitRoot(natural): 
    natural = sum(digits(natural))
    if digitsCount(natural) == 1:
        return natural
    
    return digitRoot(natural)

#Testing    
print (digitRoot(16))    
print (digitRoot(942))
print (digitRoot(132189))    
print (digitRoot(493193))