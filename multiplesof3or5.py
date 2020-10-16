def solution(number):
    i = number - 1
    totalNum = 0
    for i in range (0, number):
        if i % 5 == 0:
            totalNum += i
            continue
            
        if i % 3 == 0:
            totalNum += i
            continue
            
        i -= 1
        
    return totalNum