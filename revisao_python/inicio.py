from ex3 import Aluno

a= Aluno (200,50)

print(f"Faltas-hs permitidas: {a.calcular_faltas()}")


print (f'Aluno com {a.faltas} faltas e esta: {a.aprovado_reprovado()}')