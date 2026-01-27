from numpy.ma.core import arange

largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede0 em metros: "))
area = largura * altura
quantidade_de_tinta = area / 2
print(f"A partir dos dados é possível concluir que a área é: {area:.2f} metros quadrados. ")
print(f"Portanto, a quantidade de tinta para pintar a parede é: {quantidade_de_tinta:.2f} litros de tinta.")

