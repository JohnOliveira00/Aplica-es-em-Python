preco = float(input(f"Digite o preço do produto: "))
desconto = preco * 5 / 100
resultado = preco - desconto
print(f"Seu novo preço com desconto é: {resultado:.2f} R$")
