#variáveis
valores = []
vInt = False
quantDig = 0
operacoes = ["Soma", "Subtração", "Multiplicação", "Divisão"]
operacao = 0
valorFinal = 0
l = 0

#filtro de entrada
while (vInt == False):
    quantDig = input("Quantos valores possui a operação?: ")

    if quantDig == "0" or quantDig == "1":
        print("Valor inválido. Insira um novo valor.")

    else:
        try: 
            int(quantDig)
            quantDig = int(quantDig)
            vInt = True

        except ValueError:
            try:
                float(quantDig)
                print("Valor inválido. Insira um novo valor.")

            except ValueError:
                print("Valor inválido. Insira um novo valor.")

#salva valores digitados no array
while l < quantDig:
    valorn = int(input("Insira o " + str(l + 1) + "° valor: "))
    valores.append(valorn)
    l+=1

#printa valores em tela
print(valores)