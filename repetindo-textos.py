#Vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado
info1 = str(input("Digite a frase: "))
vezes = int(input("Digite o número de vezes que deseja repetir a frase: "))

for i in range(vezes):
    print(info1)