import math
angulo = float(input("Digite o ângulo que você deseja: "))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print(f'O seno do ângulo {angulo:.2f} é de: {seno:.2f} ')
print(f"O coseno do ângulo {angulo:.2f} é de: {cos:.2f} ")
print(f"A tangente do ângulo {angulo:.2f} é de: {tan:.2f} ")

