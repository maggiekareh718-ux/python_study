# 

# Q4
# A social media platform verifies popular users. Build a program that grants verification once followers exceed 10,000.

followers=input('Enter number of followers:')
followers=int(followers)

if followers >10000:
    res='Verified'
else:
    res='Not verified'

print(res)
    
