my_dict={
"name":"Maggie Kareh",
"age":18,
"city":"Nairobi"
}
print(my_dict)
print(type(my_dict))

#accessing values in a dictionary
print(my_dict["age"])
print(my_dict["city"])

#update  and add
#update age
my_dict["age"]=40
print(my_dict)
#adding a new property
my_dict["occupation"]="Software Developer"
print(my_dict)

my_dict["School"]="Anestar"
print(my_dict)

#Dictionary Methods
my_dict.pop('age')
print(my_dict)
# my_dict.popitem()->removes the last added property
print(my_dict)
