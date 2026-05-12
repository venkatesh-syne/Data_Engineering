#Access an element from tuple.
numbers = (10,20,"venkat",40,10.2,20)
print(numbers[2])

#Find length of tuple.
print(len(numbers))

#Count occurrences of an element.
print(numbers.count(20))

#Convert tuple to list.
new_list = list(numbers)
print(new_list)

#Tuple unpacking example.
person = ("venkat",25,"Hyderabad")

name, age, city = person
print(name)
print(age)
print(city)

#Check whether an item exists in tuple.
cars = ("benz","audi","bmw")

if "audi" in cars:
    print("Item exists")
else:
    print("Item not found")

#Find index of an element in tuple.
print(numbers.index(40))