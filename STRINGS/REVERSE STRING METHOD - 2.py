def rev_string(string):
    
    lst = []
    
    lst.extend(string)
    lst.reverse()
    
    s = ''
    
    for i in lst:
        s = s + i
        
    return s

string = input("Enter String : ")

print(rev_string(string))
