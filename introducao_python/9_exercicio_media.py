# Receba 4 notas de um aluno e exiba se ele foi aprovado (nota maior ou igual que 6)
# Se ele ficou de recuperação (nota maior ou igual a 4) ou
# Se ele foi reprovado (nota menor do que 4)

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))
nota4 = float(input("Quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 6:
    print(f"APROVADO COM A NOTA {media}")
elif media >= 4:
    print(f"RECUPERACAO COM A NOTA {media}")
else:
    print(f"REPROVADO COM A NOTA {media}")