# Author JRI 11/2/21

x = input("Please enter a palindrome ")
if x[::-1] == x:
    print(x + ' is a palindrome')
else:
    print(x + ' is not a palindrome')