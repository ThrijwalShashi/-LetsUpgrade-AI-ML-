#Question 4:
#Write a Python's user-defined function that removes all the additional characters from the string and
#convert it finally to lower case using built-in lower(). eg: If the string is "Dr. Darshan Ingle @AIML Trainer",
#then the output be "drdarshaningleaimltrainer".
Str = "Dr. Darshan Ingle @AIML Trainer"
newStr = " "
for i in Str:
    if i.isalnum():
        newStr+= i
    else:
        continue

print(newStr.lower())
