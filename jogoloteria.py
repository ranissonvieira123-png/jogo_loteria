import random

numero_secreto = random.randint(1, 60)

tentativas = 0
chances = 10


print('----- Bem vindo ao jogo de Adivinhação -----')

while tentativas < chances:
    chute = int(input('Chute um numero de 1 a 60: '))
    tentativas += 1
    if chute < numero_secreto:
        print(f'O numero foi menor que o sorteado, tentativas = {tentativas}')
    elif chute > numero_secreto:
        print(f'O numero foi maior que o sorteado, tentativas = {tentativas}')
    else:
        print(f'Parabens!! voce acertou!! o numero sorteado foi examente o {chute}')
        break
if tentativas == chances and chute != numero_secreto:
    print(f'A suas tentativas acabaram ! o numero secreto era {numero_secreto}')
print(f'A sua quantitade de tentativa foi {tentativas}')
