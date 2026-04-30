fruits=["mango","apple","banana"]
for i in fruits:
    print(i)
#for i in tries:
#pin=input('enter pin:')

#display even numbers between 10 and 100
numbers=list(range(10,101))
even_numbers=[]
for i in numbers:
    if i%2==0:
        even_numbers.append(i)

print(even_numbers)

#display numbers divisible by 3 and 7 from numbers 1 to 100
numbers=list(range(1,101))
both_numbers=[]
for i in numbers:
    if i%3==0 and i%7==0:
        both_numbers.append(i)

print(both_numbers)

tries=3
attempts=list(range(1,4))

for i in attempts:
    pin=input('Enter pin:')
    correct_pin='1234'
    if pin==correct_pin:
        print('Proceed')
        break
    else:
        remaining_tries=tries-i
        if remaining_tries>0:
            print(f'incorrect pin try again{remaining_tries}tries remaining')
        else:
            print('Account blocked')
        