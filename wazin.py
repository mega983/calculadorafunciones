# Funciones con argumentos y retorno

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por 0."
    return a / b


# Programa principal
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

print("\nSeleccione una operación:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("Ingrese una opción (1-4): ")

if opcion == "1":
    resultado = sumar(num1, num2)
    print("Resultado:", resultado)

elif opcion == "2":
    resultado = restar(num1, num2)
    print("Resultado:", resultado)

elif opcion == "3":
    resultado = multiplicar(num1, num2)
    print("Resultado:", resultado)

elif opcion == "4":
    resultado = dividir(num1, num2)
    print("Resultado:", resultado)

else:
    print("Opción no válida.")