# codesbyguru

def sum_1_to_n(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum
    
n = int(input("Enter Number : "))

print(sum_1_to_n(n))

