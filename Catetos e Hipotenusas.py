CO = float(input("Digite o valor do cateto oposto: "))
CA = float(input("Digite o valor do cateto adjacente: "))
hipo = (CO ** 2 + CA ** 2) ** (1/2)
print(f"A hipotenusa {hipo:.2f}")