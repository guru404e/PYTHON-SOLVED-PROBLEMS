# codesbyguru

def sum_1_to_n(n):
    sum = 0
    
    while(n>=0):
        sum = sum + n
        n -= 1
    
    return sum

n = int(input("Enter Number : "))

print(sum_1_to_n(n))

