squares = [x * x for x in range(10)]
print(squares)

from random import randint
rnd = [randint(0,100) for i in range(100)]
print(rnd)

even_squares = [x * x for x in range(10) if x % 2 == 0]
print(squares)

names = ["Cori", "Graham", "Ian", "Kathleen", "Cameron"]
long_names = [name for name in names if names if len(name) >= 5]
print(long_names)

