#using intersection
set1 = {1, 2,3, 4}
set2 = {3, 5, 6}
common = set1.intersection(set2) ##print only unique common ele
print("Common elements exist:",common)

common1 = set1 & set2 #print only unique common ele
print("Common elements exist:",common1)

common2 = set1 | set2 #remove duplicate ele
print("Common elements exist:",common2)

common3 = set1 ^ set2  #removes common elements
print("Common elements exist:",common3)

common4 = set1.isdisjoint(set2)  #returns true if no common ele found
print("Common elements exist:",common4)
