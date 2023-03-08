# codesbyguru

num = int(input("Enter Number : "))

p = 1

while(num):
    r = num % 10
    p = p * r
    num = num//10
    
print("Product =",p)
    
