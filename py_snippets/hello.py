
class Calculator:

    # atributos -------------------------------------------

    def __init__(self, text):
        self.stackAdress = text

    # metodos ---------------------------------------------

    def set_stack_adress(self, text):
        self.stackAdress = text

    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b
    
    def div(self, a, b):
        return a / b

    # -----------------------------------------------------

calc = Calculator("0x4080")
print(calc.stackAdress)

calc.set_stack_adress("0x4090")
print(calc.stackAdress)
