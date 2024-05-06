numbers = [42, 12345, 42, 987, 546]
numbers.append(50)
numbers.append(657)
numbers.insert(4, 784)
numbers.remove(42)
while 42 in numbers:
    numbers.remove(42)
numbers.pop(4)
numbers[0] = 99

print(numbers.pop(2))


