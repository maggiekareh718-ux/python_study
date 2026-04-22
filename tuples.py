days_of_the_week=("sun","mon","tue","wed","thu","fri","sat")

print(type(days_of_the_week))
print(days_of_the_week[1])
print(days_of_the_week[2:4])
# display sat
print(days_of_the_week[6])
# display thursday to saturday
print(days_of_the_week[4:7])

# convert tuples to list using the list function .list()
days_of_the_week=list(days_of_the_week)
print(type(days_of_the_week))
days_of_the_week[2]='Tuesday'
print(days_of_the_week)

#convert back to tuple using the tuple function .tuple()
days_of_the_week=tuple(days_of_the_week)
print(days_of_the_week)

#sun to Sunday
days_of_the_week=list(days_of_the_week)
print(days_of_the_week)
days_of_the_week[0]='Sunday'
print(days_of_the_week)
days_of_the_week=tuple(days_of_the_week)
print(days_of_the_week)

#add january to the tuple
days_of_the_week=list(days_of_the_week)
print(days_of_the_week)
days_of_the_week.append('jan')
print(days_of_the_week)
days_of_the_week=tuple(days_of_the_week)
print(days_of_the_week)

#tuple methods
#.index()
print(days_of_the_week.index('fri'))
#.count()
print(days_of_the_week.count('sun'))