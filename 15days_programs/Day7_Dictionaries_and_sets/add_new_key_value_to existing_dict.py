from multiprocessing.connection import address_type

person = {
    "name":"venkyle",
    "age":22,
}

person["address"] = "hyderabad" #using assignment
print(person)

person.update({"address":"pune"}) #if value exist it will update the value
print(person)