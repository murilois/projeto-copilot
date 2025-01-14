#Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.
info1 = int(input("Digite o primeiro número: "))
info2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operação que deseja realizar (+, -, *, /): ")
if operacao == "+":
    resultado = info1 + info2
elif operacao == "-":
    resultado = abs(info1 - info2)
elif operacao == "*":
    resultado = info1 * info2
elif operacao == "/":
    resultado = info1 / info2
else:
    print("Operação inválida")
    resultado = None
print("O resultado da operação é: ", resultado)