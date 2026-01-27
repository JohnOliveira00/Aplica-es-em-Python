peso = float(input("Digite seu peso em KG: "))
altura = float(input("Digite sua altura em metros: "))

IMC = peso / (altura * altura)

formato_IMC = f"{IMC:.2f}"

print("Seu IMC é:", formato_IMC)
if IMC <= 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= IMC < 25:
    print("Seu peso está normal.")
elif 25 <= IMC < 30:
    print("Você está sobrepeso.")
elif 30 <= IMC < 35:
    print("Você está com obesidade grau I.")
elif 35 <= IMC < 40:
    print("Você está com obesidade grau II.")
else:
    print("Você está com obesidade grau III.")

        
    


