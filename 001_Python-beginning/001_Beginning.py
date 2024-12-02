#basic syntax
x = 10
y = 20
print('The value of x is: ', x)
print('The value of y is: ', y)

print('\n') #new line

# types
z = 25.77
a = 'c'
b = 'hello'
c = True
print(type(x))
print(type(z))
print(type(a))
print(type(b))
print(type(c))

print('\n')

#array
my_list = [1, 2, 3, 4, 5]
print('array is: ', my_list)
print('first element is: ', my_list[0])
my_list.append(6) #update
print('Updated list is: ', my_list)

print('\n')

#string array
arr = ["Python", "Java", "R"]
print('String array is', arr)
arr[0] = "SQL" #modifying any element of an array
print('Updated string array is: ', arr) 

print('\n')

#adding multiple elements of an array
my_list.extend([7])
print('Adding one element: ', my_list)
my_list.extend([8, 9])
print('Adding multiple elements: ', my_list)

print('\n')

#removing elements
my_list.remove(9)
print('Removing one element: ', my_list)
my_list.pop(4)
print('Removing fourth element: ', my_list)

print('\n')

#loop
for system in arr:print(system)

print('\n')

#nested list
narr = [[1,2,3],['a','b','c']]
print(narr[0])
print(narr[1])
print(narr[0][0])
print(narr[0][1])
print(narr[0][2])
print(narr[1][0])
print(narr[1][1])
print(narr[1][2])

print('\n')

