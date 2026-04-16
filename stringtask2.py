# Convert a float to an integer with an inbuilt function in Python
# temp = 56.8926 to 57
temp = 56.8926
temp=round(temp,0)
print(temp)
temp=int(temp)
print(type(temp))

# Convert the float below to give the results as follows
# temp = 56.8926 to 56.89 
temp = 56.8926 
temp=round(temp,2)
print(temp)
# Convert the float below to give the results as follows
# temp = 56.8926 to 56.893
temp = 56.8926 
temp=round(temp,3)
print(temp)
# Convert the float below to give the results as follows
# temp=56.8926 to 8.926 
temp=56.8926
temp=round(temp,-5,-4)
print(temp)
