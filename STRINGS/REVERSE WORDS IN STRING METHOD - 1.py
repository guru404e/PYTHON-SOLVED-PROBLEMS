def rev_words(string):
    
    lst = string.split(" ")
    lst.reverse()
    
    s = ''
    
    for i in lst:
        s = s + i + " "
        
    return s
    
string = input("Enter String : ")

print(rev_words(string))
