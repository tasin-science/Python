####set
a_set = {1,2,3,4,5}
print("a_set:", a_set)

####another method to write set (list system)
#warning: b_set is a list, so some set method may not works for list. 
b_set = ([1,2,3,4,5])
print("b_set:", b_set)




####adding elements to the set
a_set.add(6)
print("Adding 6, a_set is:", a_set)

####remove elements to the set
a_set.remove(6)
print("Removing 6, set is:", a_set)
a_set.discard(5) #discard works as remove. Discard can't work for list
print("Removing 5, set is:", a_set)

print("\n")


####set operation
print("Set operation")
x_set = {3, 7, 10, 15, 20}
y_set = {5, 7, 10, 25, 30}
print("x_set: ", x_set)
print("y_set: ", y_set)
#union
print("x_set union y_set: ", x_set | y_set)
#intersection
print("x_set intersection y_set: ", x_set & y_set)
#difference
print("x_set - y_set:", x_set - y_set)
print("y_set - x_set:", y_set - x_set)
#symmetric difference
print("x_set ^ y_set:", x_set ^ y_set) #[here x_set ^ y_set means (x_set - y_set) union (y_set - x_set)]



print("\n")



#looping through a set
print("Elements of x_set:")
for element in x_set:
    print(element)
print("\n")
print("Elements of y_set:")
for elem2 in y_set:
    print(elem2)
print("\n")
print("Elements of a_set:")
for elem3 in a_set:
    print(elem3)
print("\n")
print("Elements of b_set:")
for elem4 in b_set:
    print(elem4)
print("\n")


#checking any element in my set
if 2 in b_set:
    print("good")
else:
    print("bad")

if 6 in b_set:
    print("good")
else:
    print("bad")
