import random as rd

# looping infinito - repetição - laço
while True:
    numero_aleatorio=rd.randint(1,25)
    print(f'Numero sortedado: {numero_aleatorio}')
    resposta= input('Deseja sortear outro numero? (s/n)').strip(' ').lower()
    # strip -> manipula string tirando caracteres especiais
    # lower - > converte tudo para minusculo
    if resposta!='s':
        print('Encerrando o sorteio!')
        break