import random # Importar o módulo Random.

print("Seja muito bem vindo ao Guess Number do Gustavo!")
choice_number = input("Digite o número teto do desafio: ") # Receber o número teto do usuário. O input serve para capturar dados fornecidos durante o programa.

if choice_number.isdigit(): # Verificar se o número fornecido é um número inteiro.
    choice_number = int(choice_number) # Converter o número fornecido para inteiro
else:
    print("Erro: o vaor informado não é um número inteiro. Por favor, tente novamente.") 
    quit() # Encerrar o programa.

random_number = random.randint(0, choice_number) # Gerar um número aleatório entre 0 e o número fornecido pelo usuário.

n_choices = 0

while True: # Loop infinito.
    answer_user = input("Tente adivinhar o número gerado: ") # Receber o palpite do usuário.

    if answer_user.isdigit(): # Verificar se o palpite do usuário é um número inteiro.
        answer_user = int(answer_user) # Converter o palpite do usuário para inteiro.
    else:
        print("Erro: o vaor informado não é um número inteiro. Por favor, tente novamente.")
        continue

    n_choices = n_choices + 1
    if answer_user == random_number:
        print("Acertou!")
        break
    elif answer_user > random_number:
        print("Errou! O número gerado é menor.")
    else:
        print("Errou! O número gerado é maior.")

print(f"Você acertou o número gerado em {n_choices} tentativa(s).") # Exibir o número de tentativas que o usuário levou para acertar o número gerado.