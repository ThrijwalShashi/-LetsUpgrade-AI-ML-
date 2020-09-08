#Question 3:
#Write a Python program to check if the given string is a Palindrome or Anagram or None of them. Display
#the message accordingly to the user.
def isPalindrome(str):
 
     
    for i in range(0, int(len(str)/2)): 
        if str[i] != str[len(str)-i-1]:
            return False
    return True
 

s = "malayalam"
ans = isPalindrome(s)
 
if (ans):
    print("Yes")
else:
    print("No")