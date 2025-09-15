#list comprehensions
square_list=[x**2 for x in range(1,10)]
print("List comprehensions(square):",square_list)

#Dictionary comprehensions
square_dict={x:x**2 for x in range(1,10)}
print("Dictionary comprehensions(square):",square_dict)

#set comprehensions 
square_set={x**2 for x in range(1,10)}
print("set comprehensions(square):",square_set)

#Generator comprehensions
square_gen=(x**2 for x in range(1,10))
print("Generator comprehensions(square):",square_gen)
print(list(square_gen))