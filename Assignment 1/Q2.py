#Palindrome
def ispalindrome(s):
    if len(s) < 2: return True
    if s[0] != s[-1]: return False
    return ispalindrome(s[1:-1])

s = 'dog'
print(ispalindrome(s))

