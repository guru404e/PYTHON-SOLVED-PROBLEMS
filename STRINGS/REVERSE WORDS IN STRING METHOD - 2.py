def rev_words(string):
    
    lst = string.split(" ")
    lst.reverse()
    
    lst2 = []
    
    for i in lst:
        lst2.append(i)
        
    s = ''
    
    for i in lst2:
        s = s + i + ' '
        
    return s
    
string = input("Enter String : ")

print(rev_words(string))
