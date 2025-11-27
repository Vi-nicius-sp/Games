# Jogo de Pedra, papel e Tesoura
import random 

print('---- Jogokenpo ----')
player = input('Escolha: Pedra, Papel ou Tesoura: ').upper()
op = ['Tesoura','Pedra','Papel']
computador = random.choice(op)

if player == 'TESOURA' and computador == 'Papel' or player == 'PAPEL' and computador == 'Pedra' or player == 'PEDRA' and computador == 'Tesoura':
    print('Jogador = ',player ," X ", computador,' = Computador')
    print("Você Venceu!!!")
elif  player == 'PAPEL' and computador == 'Papel' or player == 'PEDRA' and computador == 'Pedra' or player == 'TESOURA' and computador == 'Tesoura':
    print('Jogador = ',player ," X ", computador,' = Computador')
    print("Vocês Empataram...")
else:
    print('Jogador = ',player ," X ", computador,' = Computador')
    print("Você Perdeu...")

