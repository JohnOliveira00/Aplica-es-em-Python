import random
n1 = str(input('O primeiro trabalho será: '))
n2 = str(input('O segundo trabalho será: '))
n3 = str(input('O terceiro trabalho será: '))
n4 = str(input('O quarto trabalho será: '))

lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(f"A ordem de apresentação será: {lista} ")