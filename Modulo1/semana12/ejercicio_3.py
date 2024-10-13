# Los usos mas comunes del uso de herencia multiple en python son los siguientes:
# 1) Sistemas que necesitan autenticar usuarios para poder realizar una accion
# 2) Juegos
# 3) Procesamiento de datos


# Sistema de pago que necesita autenticacion
class Logger():
    def log(self, message):
        # guardar el log en un servicio de tracks de log externo
        print(f'[LOG]: {message}')
        
class Auth():
    
    def authenticate(self, user):
        # hacer uso del servicio de autenticacion
        print(f'{user} authenticated successfully')
        return user
    
class Payment(Logger, Auth):
    
    def process_payment(self, user, amount):
        auth_user = self.authenticate(user)
        if auth_user:
            # Procesar pago mediante servicio de pagos
            self.log(f'Processing payment of {amount} for {auth_user}')
            return f'Payment proccesed for {auth_user} amount: {amount}'
           
payment = Payment()
print(payment.process_payment('Jose Benavides', 100))

# Sistema de procesamiento de datos
class FileReader():
    def read_file(self, filename):
        return f"Reading data from {filename}"

class Compressor():
    def compress(self, data):
        return f"Compressed data: {data}"

class Encryptor():
    def encrypt(self, data):
        return f"Encrypted data: {data}"

class ProcessData(FileReader, Compressor, Encryptor):
    pass

processor = ProcessData()
data = processor.read_file('data.txt')
compressed_data = processor.compress(data)
encrypted_data = processor.encrypt(compressed_data)
print(encrypted_data)