# Question 1
# Write a Python program to find the first 20 non-even prime natural numbers.
for i in range(20):
    if i%2 != 0:
        print(i)
    else:
        continue