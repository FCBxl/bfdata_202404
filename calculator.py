class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self):
        self.result += 1


calc = Calculator()
print(calc.result)
calc.add()
print(calc.result)