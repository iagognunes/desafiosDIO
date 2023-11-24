##Deposito: 
# deposito de valores positivos
# depositos devem ser armazenados em uma variavel e exibidos na operaçao de extrato

##Saque:
# permitir 3 saques diarios com limite de 500 por saque
# Se nao tiver saldo em conta, deve exibir uma mensagem
# todus os saques devem ser armazenados em uma variavel e exibidos no extrato.

## Extrato:
# lista todos os depositos e saques realizados na conta
# no fim deve ser exibido o saldo atual em "R$ 000,00"

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    match opcao:
        case 'd':
            valor_deposito = float(input("Quanto você irá depositar? "))

            if(valor_deposito > 0):
                saldo += valor_deposito
                extrato += f"Depósito realizado, valor da transação: R${valor_deposito:.2f}\n"
                print("Depósito realizado com sucesso.")
                print(f"Saldo atual: R${saldo:.2f}")
            else:
                print("Valor inválido!")
        case 's':
            valor_saque = float(input("Qual o valor do saque? "))

            excedeu_saldo = valor_saque > saldo
            excedeu_limite = valor_saque > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if(excedeu_saques):
                print("Limite de saques diários atingido.")
            elif(excedeu_limite):
                print("Valor limite para saque é de R$500")
            elif(excedeu_saldo):
                print("Saldo insuficiente.")
            else:
                saldo -= valor_saque
                extrato += f"Saque realizado, valor da transação: R${valor_saque:.2f}\n"
                numero_saques += 1
                print("Saque realizado com sucesso.")
                print(f"Saldo atual: R${saldo:.2f}")
        case 'e':
            print("\n========== EXTRATO ==========")
            print("\nNão foram realizadas movimentações." if not extrato else extrato)
            print("\n=============================")
            print(""if not extrato else f"Saldo atual da conta: R${saldo:.2f}")
        case 'q':
            print("Saindo do sistema...")
            break