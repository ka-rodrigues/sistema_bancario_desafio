def exibir_menu():  
  print(f"""
========== MENU ==========
 
[0] Sair
[1] Depósito
[2] Saque
[3] Extrato
[4] Criar Usuário
[5] Criar Conta
        
==========================
""")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Já existe usuário com esse CPF! ")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print(" Usuário criado com sucesso! ")

    print("Cadastro Concluído.")
      
      
def criar_conta(AGENCIA, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso! ")
        return {"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario}

    print("\n Usuário não encontrado, fluxo de criação de conta encerrado! ")
   
## DEPÓSITO
def realizar_deposito(saldo, extrato_conta):
    valor_deposito = float(input("Valor que deseja depositar: "))
    saldo += valor_deposito
    print(f"Seu saldo agora é: R${saldo:.2f}")
    print()
    extrato_conta += f"Depósito de R$ {valor_deposito:.2f} efetuado  \n".center(33)
    print()

    return saldo, extrato_conta

## SAQUE
def realizar_saque(saldo, extrato_conta, quantidade_saques, LIMITE_DIARIO_SAQUE, LIMITE_SAQUE):       

    while True:
      if quantidade_saques >= LIMITE_DIARIO_SAQUE:
        print("Limite Excedido")
        return saldo, extrato_conta, quantidade_saques  
      
      valor_saque = float(input("Digite o valor que deseja sacar: "))

      if valor_saque <= 0.00:
          print("Valor Inválido")

      elif valor_saque > LIMITE_SAQUE:
          print("Saque negado, o valor máximo é de R$ 500.00")
        
      elif valor_saque > saldo:
          print("O Saldo não é suficiente")
      
      else:
          quantidade_saques += 1
          saldo -= valor_saque
          extrato_conta += f"Saque de R$ {valor_saque:.2f} efetuado\n".center(33)
          print(f"Seu saldo agora é: {saldo:.2f}")
          print()
          print(f"Saques restantes hoje: {3 - quantidade_saques}  ")
          print()
          break
      
    return saldo, extrato_conta, quantidade_saques

## EXTRATO
def solicitar_extrato(saldo, extrato_conta):
      
    print(f"========== EXTRATOS ==========")
    print()
    print("Não foram realizadas movimentações." if not extrato_conta else extrato_conta)    
    print()  
    print(f"Seu saldo é de: R$ {saldo:.2f}")
    print("==============================")

def main():
  contas = []
  usuarios = []
  saldo = 0.00
  quantidade_saques = 0
  LIMITE_DIARIO_SAQUE = 3
  LIMITE_SAQUE = 500.00
  AGENCIA = "0001"
  extrato_conta = ""
  


  while True: 
    exibir_menu()
    menu_escolha = int(input("Digite a operação que você deseja: "))
    print()

    if menu_escolha < 0 or menu_escolha > 5:
      print("Operação inválida, digite uma operação válida: ")
    elif menu_escolha == 1:
      saldo, extrato_conta = realizar_deposito(saldo, extrato_conta)  

    elif menu_escolha == 2:
       saldo, extrato_conta, quantidade_saques = realizar_saque(saldo, extrato_conta, quantidade_saques, LIMITE_DIARIO_SAQUE, LIMITE_SAQUE)

    elif menu_escolha == 3:
       solicitar_extrato(saldo, extrato_conta)

    elif menu_escolha == 4:
      criar_usuario(usuarios) 

    elif menu_escolha == 5:
      numero_conta = len(contas) + 1
      conta = criar_conta(AGENCIA, numero_conta, usuarios)
      
      if conta:
                contas.append(conta)

    else:
       print("Saindo . . .")
       break   

main()

