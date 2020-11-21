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
            operacao = input("Qual operação deseja realizar?: ")
            vInt = True

        except ValueError:
            try:
                float(quantDig)
                print("Valor inválido. Insira um novo valor.")

            except ValueError:
                print("Valor inválido. Insira um novo valor.")

#salva valores digitados no array
while l < quantDig:
    valorN = input("Insira o " + str(l + 1) + "° valor: ")

    try: 
        int(valorN)
        valorN = int(valorN)
        valores.append(valorN)
        l+=1

    except ValueError:
        try:
            float(valorN)
            valorN = float(valorN)
            valores.append(valorN)
            l+=1

        except ValueError:
            print("Valor inválido. Insira um novo valor.")

#printa valores em tela
#print("O comprimento do array é " + str(len(valores)))
print(valores)