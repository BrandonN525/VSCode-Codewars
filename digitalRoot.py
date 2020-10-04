def digital_root(n):
    sum = 0
    if n == 0:
        return 0
    
    if n % 9 == 0:
        sum = 9
        
    else:
        sum = n % 9
        
    return sum