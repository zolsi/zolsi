import math
def find_factors(n):
    for i in range(math.floor(n/2)):
        j=n+i*i
        if math.sqrt(j)-math.floor(math.sqrt(j))==0 :
            
            break 
    return int(math.sqrt(j)-i),int(math.sqrt(j)+i)         
