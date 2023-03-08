string = input("Enter String  : ")

lst = []

lst.extend(string)

lst2 = lst.copy()

lst.reverse()

if lst2 == lst:
    print("Palindrome")
else:
    print("Not Palindrome")
