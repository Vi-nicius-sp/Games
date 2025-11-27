import random

num_secreto = random.randint(1, 100)
max_tentativas = 10
atual_tentativa = 0
palpite = 0

print('===== Jogo de Adivinhação =====')
print('Adivinhe qual o Número secreto de 1 a 100 !!')
print('Você tem um total de 10 tentativas.')
while atual_tentativa < max_tentativas:
    palpite = int(input("Digite o seu palpite: "))
    if palpite == num_secreto:
        print(f'Parábens, você acertou o número era.. ',num_secreto)
        atual_tentativa +=1
        print('Número de Tentativas: ', atual_tentativa)
        print('')
        break
    elif palpite < num_secreto:
        print(f'O número secreto é maior que ',palpite)
        atual_tentativa +=1
        print('Número de Tentativas: ', atual_tentativa)
        print('')
    elif palpite > num_secreto:
        print(f'O número secreto é menor que ',palpite)
        atual_tentativa +=1
        print('Número de Tentativas: ', atual_tentativa)
        print('')
    else:
        print("Número incorreto, digite somente números de 1 a 100")
        print('')

if atual_tentativa == 10:
    print('Você esgotou suas tentativas, o número é ', num_secreto,'. Obrigado por jogar')
else:
    print('Obrigado por jogar.')
