# GROUP 1
# Q1
# A bank wants to improve its ATM service. Create a program that stores a customer’s name and account balance, then allows them to request a withdrawal. If the amount requested is greater than the available balance, the transaction should fail. If successful, deduct the amount together with a transaction fee of KES 30 and display the new balance.
customer_name=input('Enter your name:')
account_balance=10000
amount_requested=input('Enter the amount to withdraw:')
amount_requested=int(amount_requested)


trans=30
if amount_requested>account_balance:
    print(f'Hello {customer_name}Transaction failed insufficient funds to withdraw {amount_requested}your balance is{account_balance}')
else:
    account_balance=account_balance-(amount_requested+trans)
    print(f'hello {customer_name} {amount_requested} withdrawned successfully New_balance {account_balance}')
# Q2
# A trainer entered marks for five subjects and needs help analyzing student performance. Create a program that stores the marks in a list, calculates the average, awards grade A for averages of 70 and above, grade B for averages of 50 to 69, and grade C for anything below 50. If any subject score is below 40, display a message showing the student must retake that subject.
marks=[20,60,40,80,100]
average=sum(marks)/len(marks)
print(average)

if average>=70:
    grade='A'
elif average>=50 and average <70:
    grade='B'
elif average>=40 and average <50:
    grade='C'
elif average>=30 and average <40:
    grade='D'
# Q3
# A supermarket manager needs help checking stock levels. Create a program that stores product names and quantities in a dictionary, identifies items that are completely out of stock, and also shows products with quantities below five units that need urgent restocking.
# Q4
# A company wants to secure employee accounts. Create a login system that stores a username and password, allows only three attempts, locks the account after three failed attempts, and welcomes the user when the correct credentials are entered.





























