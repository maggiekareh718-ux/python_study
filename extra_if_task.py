
# Write a program that checks login credentials:
# "Access granted" if email = "admin@gmail.com" and password = "Admin@123"
# "Wrong password" if email is correct but password is wrong
# "Email not found" otherwise

email=input('Enter email:')
password=input('Enter password:')
correct_email="admin@gmail.com"
correct_password="Admin@123"

if email==correct_email and password==correct_password:
    print('Access granted')
elif email==correct_email and password!=correct_password:
    print('Wrong password')
else:
    print('Email not found')

# Create a program that validates an email:
# "Invalid email" if it does not contain "@" or "."
# "Gmail account" if it ends with "@gmail.com"
# "Other email provider" otherwise

email=input('Enter email:')
if '@'not in email or'.' not in email:
    print('Invalid email')
elif email.endswith ("@gmail.com"):
    print('Gmail account')
else:
    print('Other email provider')
#or
if email.find('@')==-1 or email.find('.')==-1:
    print('Invalid email')
elif email.endswith('@gmail.com'):
    print('Gmail account')
else:
        print('Other email provider')

#  **   Write a program that checks password strength:
# "Weak" if length < 6
# "Moderate" if length 6–10 and contains at least one digit
# "Strong" if length > 10 and contains both digits and uppercase letters
password=input('Enter password:')


if len(password) <6:
    print('Weak')
elif len(password) >=6 and len(password) <=10 and password.isalnum():
    print('Moderate')
elif len(password)>6 and password.isalnum and password.isupper:
    print('Strong')

#     Write a program that checks a password:
# "Invalid" if it does not start with a capital letter
# "Invalid" if it does not end with a number
# "Valid password" otherwise

password=input('Enter password')

if password[0].isupper() and password[-1].isdigit():
    print('valid password')
else:
    print('Invalid')

    # Write a program that takes a number and checks:

# "Fizz" if divisible by 3
# "Buzz" if divisible by 5
# "FizzBuzz" if divisible by both
# Otherwise print the number
number=input('Enter a number:')
number=int(number)
if number%3==0:
    print('Fizz')
elif number%5==0:
    print('Buzz')
elif number%3==0 and number%5==0:
    print('FizzBuzz')
else:
    print('number')


# Create a program that takes a score and prints a grade:
# A (≥ 80)
# B (70–79)
# C (60–69)
# D (50–59)
# F (< 50)
score=input('Enter score: ')
if score >=80:
    print('grade A')
elif score >=70 and score<=79:
    print('grade B')
elif score >=60 and score <=69:
    print('grade C')
elif score >=50 and score <=59:
    print('grade D')
else:
    print('grade F')

#     Create a program that takes two numbers and prints:
# "Equal" if same
# "First is greater"
# "Second is greater"
num1=input('Enter first number:')
num1=int(num1)
num2=input('Enter second number:')
num2=int(num2)
if num1==num2 and num2==num1:
    print('Equal')
elif num1>num2:
    print('First is greater')
else:
    print('Second is greater')


# 8.
# Write a program that takes a day number (1–7) and prints:
# Weekday (1–5)
# Weekend (6–7)
# Invalid input otherwise
day=input('Enter a day number')
day=int(day)
if day>=1 and day<=5:
    print('Weekday')
elif day>=6 and day<=7:
    print('Weekend')
else:
    print('Invalid input')
# 9.
# Create a program that takes a temperature and prints:
# "Freezing" if ≤ 0
# "Cold" if 1–15
# "Warm" if 16–30
# "Hot" if > 30
temperature=input('Enter temperature')
temperature=int(temperature)
if temperature<=0:
    print('Freezing')
elif temperature >=1 and temperature <=15:
    print('Cold')
elif temperature >=16 and temperature <=30:
    print('Warm')
else:
    print('Hot')
# 10.
# Create a program that takes a year and prints:
# "Leap year" if divisible by 4
# "Century year" if divisible by 100
# "Common year" otherwise

year=int(input('Enter year:'))
if year%4==0 and (year%400==0 or year%100!=0):
    print('leap year')
elif year%100==0:
    print('Century year')
else:
    print('Common year')