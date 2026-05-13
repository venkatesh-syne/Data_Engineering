person = {"name": "Venkatesh", "age": 25, "address": "AP","job":"IT"}
del person["age"]  #if age is not give error
print(person)

person.pop("address") #it  returns a value
print(person)

person.popitem() #remove last inserted pair
print(person)

#using functions
def remove_key(dictionary, key):
    if key in dictionary:
        del dictionary[key]
person1 = {"name": "Venkatesh", "age": 25, "address": "AP","job":"IT"}
remove_key(person1, "job")
print(person1)
