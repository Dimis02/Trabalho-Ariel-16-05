import re

while True:
    print("Selecione a operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("X - Sair")

    opcao = input("Escolha a operação: ")

    if opcao == 'X':
        print("Encerrando a calculadora...")
        break

    if not re.match("[1-4]", opcao):
        print("Opção inválida. Por favor, escolha novamente.")
        continue

    valores = []
    while True:
        valor = input("Digite um valor (ou 'P' para parar): ")
        if valor.upper() == 'P':
            break
        valores.append(float(valor))

    if (valores) < 2:
        print("Erro: É necessário inserir pelo menos dois valores.")
        continue

    if opcao == '1':
        resultado = 0
        for valor in valores:
            resultado += valor
        print("Resultado da adição:", resultado)
    elif opcao == '2':
        resultado = valores[0]
        for valor in valores[1:]:
            resultado -= valor
        print("Resultado da subtração:", resultado)
    elif opcao == '3':
        resultado = 1
        for valor in valores:
            resultado *= valor
        print("Resultado da multiplicação:", resultado)
    elif opcao == '4':
        resultado = valores[0]
        for valor in valores[1:]:
            if valor != 0:
                resultado /= valor
            else:
                print("Erro: Divisão por zero!")
                break
        else:
            print("Resultado da divisão:", resultado)