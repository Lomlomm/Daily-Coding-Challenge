def divisibleSumPairs(k, ar):
    right = len(ar)-1 #al final 
    left = 0 # al principio 
    result = 0
    while True: 
        if (ar[right]+ar[left])%k == 0: 
            result += 1 
        right -= 1     
        if left == len(ar)-2: 
            break
        if right == left: 
            left += 1
            right = len(ar)-1
            
    return result 

print(divisibleSumPairs(2,[8,10]))