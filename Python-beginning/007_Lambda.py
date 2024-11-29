#lambda function
add = lambda x,y:x+y
print(add(35,24))

average = lambda x,y,z:(x+y+z)/3
print(average(50,60,70))
print(type(average))

print("\n")

#Using Lambda with map() for list
numbers={1,2,3,4,5}
doubled = list(map(lambda x:x*2, numbers))
squares = list(map(lambda x:x**2, numbers))
print(doubled)
print(squares)

#Using lambda inside a list comprehension to square each number
cubed = [(lambda x:x**3)(x) for x in numbers]
print(cubed)
even_numbers = [x for x in numbers if(lambda x:x%2==0)(x)]
print(even_numbers)

#Using lambda function for dictionary
book_price = {"Physics":600, "Chemistry":700, "Biology":500}
discounted_price = {k:(lambda price:price*0.09)(v) for k,v in book_price.items()}
print(discounted_price)

#if-else label
label = {x:(lambda x:'even' if x%2==0 else 'odd')(x)for x in numbers}
print(label)



