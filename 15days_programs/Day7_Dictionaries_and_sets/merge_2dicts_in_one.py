fruits = {"apple":"red","mango":"yellow"}
vegetable = {"brinjal":"purple","tomoto":"red"}
#items = fruits.update(vegetable) ths wont work
fruits.update(vegetable)
print(fruits)

#update() → modifies original dict, returns None
#{**d1, **d2} or d1 | d2 → creates new dict

merged = fruits | vegetable #using operator method
print(merged)

a = {**fruits, **vegetable} #unpacking
print(a)
