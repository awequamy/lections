def isPalindrome(word):
    return word == word[::-1]
    """
    the given function checks if the word entered is a pelindrome or not
    """
    
word = input('enter any word')
result = isPalindrome(word)
 
if result:
    print("Yes")
else:
    print("No")