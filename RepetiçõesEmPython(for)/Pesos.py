
maior = 0  # Inicialize a variável 'maior' com um valor mínimo.
menor = float('inf')   # Inicialize a variável 'menor' com um valor máximo.

for _ in range(5):
    i = int(input("Digite o peso: "))
    if i > maior:
        maior = i
    if i < menor:
        menor = i

print("O maior peso digitado é:", maior)
print("O menor peso digitado é:", menor)





