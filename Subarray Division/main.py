def birthday(s, d, m):
    result = 0
    if len(s) < m: 
        return result
    for i in range(len(s)-(m-1)): 
        lim = i+m
        print(lim)
        if sum(s[i:lim]) == d: 
            result += 1 
        if lim == len(s): 
            break
    return result

print(birthday([2,5,1,3,4,4,3,5,1,1,2,1,4,1,3,3,4,2,1], 18, 7))