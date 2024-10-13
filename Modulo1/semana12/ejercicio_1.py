# 1. Cree una clase de `BankAccount` que:
#     1. Tenga un atributo de `balance`.
#     2. Tenga un método para ingresar dinero.
#     3. Tengo un método para retirar dinero.
    
#     Cree otra clase que herede de esta llamada `SavingsAccount` que:
    
#     1. Tenga un atributo de `min_balance` que se pueda asignar al crearla.
#     2. Arroje un error si se intenta retirar dinero y el `balance` está debajo del `min_balance`.
class BankAccount():
    balance = 0
    
    def deposit(self):
        pass
    
    
    def withdraw(self):
        pass
        
        
class SavingsAccount(BankAccount):
    
    def __init__(self, min_balance):
        self.min_balance = min_balance
    
    
    def deposit(self, amount):
        self.balance += amount
        
        
    def withdraw(self, amount):
        if (self.balance - amount) < self.min_balance:
            raise ValueError(f'No se pudo retirar {amount} por fondos insuficientes')
        else:
            self.balance -= amount
        
        
    def get_balance(self):
        print(self.balance)
        
            


movement = SavingsAccount(100)
movement.deposit(150)
movement.deposit(350)
movement.get_balance() # deposito 500
movement.withdraw(50) # retiro 50 ahora es 450
movement.withdraw(350) # aqui aun se permite retirar porque quedan 100 que es = al balance minimo
movement.withdraw(50) # aqui da error porque sobrepasa el balance minimo
movement.get_balance()