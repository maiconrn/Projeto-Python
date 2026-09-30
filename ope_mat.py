# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

operação = input("Digite a operaçao que deseja realizar (+, -, *, /): ")

if operação == '+':
    print(num1 + num2)
elif operação == '-':
    print(abs(num1 - num2))
elif operação == '*':
    print(num1 * num2)
elif operação == '/':
     print (num1 / num2)
else:
    print("Operaçao invalida")

    