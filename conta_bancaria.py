menu = """

      ############### MENU ###############

      [1] Depositar
      [2] Sacar
      [3] Extrato
      [0] Finalizar

      ####################################

      

                  Obrigado por uar nosso sistema!!!
=> """


saldo = 0
limite = 500
extrato_deposito = []
extrato_saque = []
numero_saques = 0
LIMITE_SAQUES = 3
deposito = 0
saque = 0


while True:

    opcao = input(menu)

    if opcao == "1":
            
            deposito = int(input("Qual o valor do depósito?  Valor:  "))

            if deposito > 0:
                        print(f"Depósito realizado no valor de R${deposito:,.2f}.")
                        input()
                        saldo += deposito
                        extrato_deposito.append(deposito)
                        deposito = 0

            else:
                  print("Valor inválido. Voltando para o menu principal.")
                  input()

                  

    elif opcao == "2":
            
            saque = int(input("Qual o valor do saque?  Valor:  "))

            if numero_saques == LIMITE_SAQUES:
                        print("Número de Saques Diário Chegaram ao Limite! Disponível: 3 Saques Por Dia.")
                        input()

            elif saque > 500:
                        print("Limite Máximo Diário São de 500 Reais!")
                        input()

            elif saque > 0 and saldo >= saque and saque <= 500 and numero_saques < 3:
                        print(f"Saque realizado no valor de R${saque:,.2f}.")
                        input()
                        saldo -= saque
                        numero_saques += 1
                        extrato_saque.append(saque)
                        saque = 0

            else:
                  print("Valor inválido. Voltando para o menu principal.")
                  input()



    elif opcao == "3":
            print("Estamos Gerando o Seu Extrato Bancário")
            input("Tecle Para Continuar")
            


            print (
                  f"""

            ############### EXTRATO ###############

            Depósitos Realizados

            {extrato_deposito}

            Saques Realizados

            {extrato_saque}

            Número de Saques = {numero_saques}
            TOTAL = R${saldo:,.2f}

            ####################################
            => """
            )
            input()



        
    elif opcao == "0":
            break
                  

    else:
            print("Opção inválida. Por favor escolha uma opção válida.")
            input()