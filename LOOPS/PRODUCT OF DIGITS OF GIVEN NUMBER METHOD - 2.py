# codesbyguru

def product_of_digits(num):

    p = 1
    
    while(num):
        r = num % 10
        p = p * r
        num = num//10
        
    return p
    
num = int(input("Enter Number : "))
print("Product =",product_of_digits(num))
    
    
