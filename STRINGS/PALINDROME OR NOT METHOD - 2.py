def ispalindrome(string):
    
    lst = []

    lst.extend(string)
    
    lst2 = lst.copy()
    
    lst.reverse()
    
    if lst2 == lst:
        return True
    else:
        return False

string = input("Enter String  : ")

print(ispalindrome(string))
