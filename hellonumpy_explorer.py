import numpy as np

a = np.array([1,7,12])
print(a * 5)
b = np.array([[1.5, 2, 5], [3,17,42]])
print(b*2)

c = np.zeros((2,3))
print(c)

numbers = np.arange(1, 12, 2)
print(numbers) 

#reshape a table
numbers = numbers.reshape((3,2))
print(numbers)

print(np.linspace(0,10,4))