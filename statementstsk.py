
# # # Take three inputs from a user, separately. Print the largest of the numbers.
# # #     Hint: Determine what type of data is taken in as input.input=40
# a=int(input('Enter first number:'))
# b=int(input('Enter second number:'))
# c=int(input('Enter third number:'))
# if a>b and a>c:
#      print('Largest number is:',a)
# elif b>=a and b>=c:
#      print('Largest number is:',b)
# else:
#      print('Largest number is:',c)


# # Take four inputs from a user, separately. Print the largest of the numbers.
# w=input('Enter first number:')
# w=int(w)
# x=input('Enter second number:')
# x=int(x)
# y=input('Enter third number:')
# y=int(y)
# z=input('Enter fourth number:')
# z=int(z)

# if w>x and w>y and w>z:
#      print(w)
# elif x>w and x>y and x>z:
#      print(x)
# elif y>w and y>x and y>z:
#      print(y)
# else:
#      print(z)





# # # Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”,if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”

# temperature=int(input('Enter Temperature:'))
# if temperature >30:
#      print('The temperature is too high')
# elif temperature >=15 and temperature <30:
#      print('Normal Temperature')
# else:
#      print('Too cold')


# #Create a program that checks a user's balance :
# #"Insufficient funds"if <100
# #"Moderate balance"if 100-1000
# #"High balance"if >1000

# balance=input('Enter user balance:')
# balance=int(balance)
# if balance <100:
#     print('Insufficient funds')
# elif balance>100 and balance<=1000:
#     print('Moderate balance')
# else:
#     print('High balance')


# # # Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
# # # and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print "Conditions not met"
# x=int(input('Enter value for x:'))
# y=int(input('Enter value for y:'))
# if 10<=x <=20 and y>100:
#          print('Conditions met')
# else:
#      ('Conditions not met')


# #Write a program that checks:
# #"small"if number<10
# #"Medium"if 10-50
# #"Large"if above 50
#      num1=input('Enter first number:')
#      num1=int(num1)
    
# if num1<10:
#     print("small")
# elif num1>10 and num1<50:
#     print('Medium')
# else:
#     print('Large')


# # #  Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access   granted", otherwise print "Access denied"

# password=input('Enter password:')
# if password=="secret123":
#      print("Access granted")
# else:
#      print("Access denied")

#Write a program that asks the user for email and password checks if the email is equal to "admin@gmail.com"and password is equal to "admin123"if it is print"Access granted"otherwise print"Access denied"
email=input('Enter email:')
password=input('Enter password:')
correct_email="admin@gmail.com"
correct_password="admin123"

if email==correct_email and password==correct_password:
    print("Accesss granted")
else:
    print("Access Denied")