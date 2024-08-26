# programação orientada a objetos - POO


'''
Programação orientada objeto
- flask e django


Programaçao estruturada com OO
-Flet

Programação funcional
- lambda
'''

class Aluno():
    def __init__(self,ch,faltas) :
        self.ch=ch
        self.faltas=faltas
        
         
    def calcular_faltas (self):
        percent_ch=self.ch * (25/100)
        return percent_ch

    def aprovado_reprovado (self):
        percent_ch=self.ch * (25/100)
        if self.faltas>percent_ch:
            return 'retido'
        else:
            return 'promovido'

