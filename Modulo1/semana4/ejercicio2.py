#Cree un programa que le pida al usuario su nombre, apellido, y edad, 
# y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.
nombre = input("Ingrese su nombre\n")
apellido = input("Ingrese su apellido\n")
edad = int(input("Ingrese su edad\n"))

if edad >= 65:
    print(f"{nombre} {apellido} es un(a) adulto mayor")
elif edad <= 3:
    print(f"{nombre} {apellido} es un(a) bebé")
elif edad > 3 and edad <= 10:
    print(f"{nombre} {apellido} es un(a) niño(a)")
elif edad > 10 and edad <= 13:
    print(f"{nombre} {apellido} es un(a) preadolescente")
elif edad > 13 and edad <= 23:
    print(f"{nombre} {apellido} es un(a) adolescente")
elif edad > 23 and edad <= 35:
    print(f"{nombre} {apellido} es un(a) adulto joven")
elif edad > 35 and edad < 65:
    print(f"{nombre} {apellido} es un(a) adulto")