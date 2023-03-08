# codesbyguru

def sum_of_digits(num):
    
    s = 0
    
    for i in range(len(str(num))):
        r = num % 10
        s = s + r
        num = num//10
    
    return s
    
num = int(input("Enter Number : "))
print("Sum =",sum_of_digits(num))
    
