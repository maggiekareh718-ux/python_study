# append->used to add items at the end of the list

my_list=["Mike","Jane","Alex",1000,200,2000,True,False]
my_list.append('Donkey')
print(my_list)

# insert->adds an item at a specified index

my_list.insert(1,"Mary")
print(my_list)

# pop->removes ana item at  a specified index

my_list.pop(3)
print(my_list)

# task
lst=[10,20,30,['Jane','Mary',[1000,2000,3000]],40,50,60]

# using methods
# add 70 at the end of the list
lst.append(70)
print(lst)
#add 1500 btww 1000 and 2000
lst[3][2].insert(1,1500)
print(lst)
#delete 2000
lst[3][2].pop(2)
print(lst)

# sort->used to arrange list items asc by default
lst1=[1,50,10,20,5,2]
lst1.sort(reverse=True)
print(lst1)
lst2=["Mike","Jane","Alex"]
lst2.sort()
print(lst2)

#remove
lst2.remove('Alex')
print(lst2)

#extend
lst2=["Mike","Jane","Alex"]
lst1=[1,50,10,20,5,2]

#concating->not a method
lst3=lst2+lst1

lst2.extend(lst1)
print(lst2)

#count
print(lst2.count("Mike"))

#copy
lst4=lst1.copy()
print(lst4)

#clear
my_list.clear
print(my_list)

#in memebrship->checks whether
lst2=["Mike","Jane","Alex"]
print('alex'in lst2)