# Somar e mostrar a soma e a media de 3 notas
# verificar se o aluno foi promovido ou retido

class Nota :
    def __init__(self,nota1,nota2,nota3):
        self.nota1=nota1
        self.nota2=nota2
        self.nota3=nota3
        self.media_nota=(self.nota1+self.nota2+self.nota3)/3
        self.soma_nota=(self.nota1+self.nota2+self.nota3)
    def media (self):
        return self.media_nota
    def aprovado(self):
        if self.media_nota>=70:
            return 'promovido'
        else:
            return 'retido'
    def soma (self):
        return self.soma_nota
        


n1=float(input ('Digite a nota1: '))
n2=float(input ('Digite a nota2: '))
n3=float(input ('Digite a nota3: '))


nota= Nota(n1,n2,n3)
print(f'Soma das notas: {nota.soma()}')
print(f'Media: {nota.media() : .2f}')
print(f'Aluno esta: {nota.aprovado()}')