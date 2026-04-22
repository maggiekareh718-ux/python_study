if 20>10:
    print('20 is greater')
else:
    print('20 is less')

# check if someone is eligible to vote
age=20
if age>=18:
    print('Eligible to vote')
else:
    print('Not eligible to vote')

#check if temeperature is greater than 30 print too hot otherwise normal temperature
temperature=40

if temperature>=30:
    print('too hot')
else:
    print('normal temperature')

#check if temeperature is greater than 30 print too hot,if temeperature is above 15 and less than 30  normal temperature otherwise too cold
temp=5

if temp>=30:
    print('too hot')
elif temp>=15 and temp<30:
    print('normal temperature')
else:
    print('too cold')

marks=40

if marks >=80:
    print('grade A')
elif marks >=70 and marks <80:
    print('grade B')
elif marks >=60 and marks <70:
    print('grade C')
elif marks >=50 and marks <60:
    print('grade D')
else:
    print('grade E')