def ispalindrome(string):
    
    if string == string[::-1]:
        return True
    else:
        return False

string = input("Enter String  : ")

print(ispalindrome(string))
