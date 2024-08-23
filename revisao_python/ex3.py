# programação orientada a objetos - POO

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
            return 'reprovado'
        else:
            return 'aprovado'
