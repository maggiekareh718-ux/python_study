#1. numbers = (10, 20, 30, 40, 50)Add 60 to the end,Replace 30 with 35.
numbers = (10, 20, 30, 40, 50)
print(type(numbers))
numbers=list(numbers)
print(type(numbers))
numbers.append(60)
print(numbers)
numbers[2]=35
print(numbers)
numbers=tuple(numbers)
print(numbers)

# 2. values = (15, 5, 30, 25, 10) arrange the elements in ascending order.
values = (15, 5, 30, 25, 10)
values=list(values)
print(values)
values.sort()
print(values)
values=tuple(values)
print(values)

# 3. fruits = ("apple", "banana", "cherry", "banana", "mango", "banana")
# Count occurrences of "banana",Remove all occurrences of "banana".
fruits = ("apple", "banana", "cherry", "banana", "mango", "banana")
fruits=list(fruits)
print(fruits)
print(fruits.count('banana'))
fruits.pop(1)
fruits.pop(2)
fruits.pop(3)
print(fruits)
fruits=tuple(fruits)
print(fruits)

# 4. names = ("Alice", "Bob", "Charlie", "David") Reverse the order of elements using sort method.
names = ("Alice", "Bob", "Charlie", "David")
names=list(names)
print(names)
names.sort(reverse=True)
print(names)
names=tuple(names)
print(names)

# 5. colors = ("red", "blue", "green")add "yellow" at index 1,Extend with ["purple", "orange"]
colors = ("red", "blue", "green")
colors=list(colors)
colors.insert(1,"yellow")
print(colors)
lst=("purple","orange")
colors.extend(lst)
print(colors)
colors=tuple(colors)
print(colors)