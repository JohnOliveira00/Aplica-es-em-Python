import random
n1 = str(input('Digite a nota do primeito do aluno: '))
n2 = str(input('Digite a nota do segundo aluno: '))
n3 = str(input('Digite a nota do terceiro aluno: '))
n4 = str(input('Digite a nota do quarto aluno: '))

Lista = [n1, n2, n3, n4]
sorteado = random.choice(Lista)
print(f"O aluno escolhido foi: {sorteado}")

