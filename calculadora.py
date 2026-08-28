
nome = input("informe seu nome: ")   #conheci o comando "def" porem nao usei: Você está avisando ao Python: 'Olha, vou definir um bloco de código chamado

while True:  #comando  para um laço que repete o código
    try:
        num1 = float(input(f"\nOlá {nome} digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        print(f"\nResultados para {nome}:")  #comando \n: é um caractere de escape que representa uma quebra de linha. cria um espacamento
        print(f"{num1} + {num2} = {num1 + num2}")
        print(f"{num1} - {num2} = {num1 - num2}")
        print(f"{num1} * {num2} = {num1 * num2}")
        print(f"{num1} ** {num2} = {num1 ** num2}")

        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Divisão: Não é possível dividir por zero.")

    except ValueError:
        print("Erro: Por favor, insira apenas números válidos.")

    continuar = input("\nDeseja continuar? (s/n): ").lower() #.lower: ele transforma todas as palavras em minusculas para o programa enteder
    if continuar == 'n':
        print(f"Encerrando a calculadora, ate a proxima {nome}")
        break   #encarramento do laco
