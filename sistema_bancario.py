def exibir_menu():  
  print(f"""
    ========== MENU ==========
 
      [0] Sair
      [1] Depósito
      [2] Saque
      [3] Extrato
    
    ==========================
""")


saldo = 0.00
quantidade_saques = 0
LIMITE_DIARIO_SAQUE = 3
LIMITE_SAQUE = 500.00
extrato_conta = ""


while True: 
  exibir_menu()
  menu_escolha = int(input("    Digite a operação que você deseja: "))
  print()

  ## OPERAÇÃO INVÁLIDA/SAIR
  if menu_escolha < 0 or menu_escolha > 3:
    print("    Operação inválida, digite uma operação válida: ")
    continue
  elif menu_escolha == 0:
    print("    Saindo . . .")
    break

  ## DEPÓSITO
  elif menu_escolha == 1:
    valor_deposito = float(input("    Valor que deseja depositar: "))
    saldo += valor_deposito
    print(f"    Seu saldo agora é: R${saldo:.2f}")
    print()
    extrato_conta += f"Depósito de R$ {valor_deposito:.2f} efetuado  \n".center(33)
    print()

## SAQUE
  elif menu_escolha == 2:
        
    if quantidade_saques >= LIMITE_DIARIO_SAQUE:
      print("Limite Excedido")
      continue    

    while True:
      valor_saque = float(input("    Digite o valor que deseja sacar: "))

      if valor_saque <= 0.00:
        print("Valor Inválido")

      elif valor_saque > LIMITE_SAQUE:
        print("    Saque negado, o valor máximo é de R$ 500.00")
      
      elif valor_saque > saldo:
        print("O Saldo não é suficiente")
    
      else:
        quantidade_saques += 1
        saldo -= valor_saque
        extrato_conta += f"Saque de R$ {valor_saque:.2f} efetuado\n".center(33)
        print(f"    Seu saldo agora é: {saldo:2f}")
        print()
        print(f"Saques restantes hoje: {3 - quantidade_saques}  ")
        print()
        break
    
## EXTRATO
  elif menu_escolha == 3:

      print("     Não foram realizadas movimentações." if not      extrato_conta else extrato_conta)

      def exibir_menu_extrato(extrato_conta):
        print(f"""
    ========== EXTRATOS ==========

    {extrato_conta}
      
    Seu saldo é de: R$ {saldo:.2f}

    ==============================
""")  
      exibir_menu_extrato(extrato_conta)
