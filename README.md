# Sistema Bancário Simples em Python

Este é um sistema bancário simples desenvolvido em Python, que simula operações básicas de conta e gerenciamento de usuários. O projeto foi criado com foco em demonstrar conceitos fundamentais de programação e lógica de negócio.

## Funcionalidades

O sistema oferece as seguintes operações através de um menu interativo:

*   **[0] Sair:** Encerra a aplicação.
*   **[1] Depósito:** Permite realizar depósitos em uma conta.
*   **[2] Saque:** Permite realizar saques de uma conta, com controle de limite diário e valor máximo por saque.
*   **[3] Extrato:** Exibe o histórico de movimentações e o saldo atual da conta.
*   **[4] Criar Usuário:** Permite cadastrar novos usuários no sistema, verificando a existência de CPF duplicado.
*   **[5] Criar Conta:** Permite criar uma nova conta bancária para um usuário existente.

## Tecnologias Utilizadas

*   **Python 3:** Linguagem de programação principal.

## Estrutura do Código

O código é organizado em funções que representam cada operação do sistema:

*   `exibir_menu()`: Mostra as opções disponíveis para o usuário.
*   `filtrar_usuario()`: Função auxiliar para buscar um usuário pelo CPF.
*   `criar_usuario()`: Lógica para cadastrar um novo usuário.
*   `criar_conta()`: Lógica para criar uma nova conta.
*   `realizar_deposito()`: Gerencia a operação de depósito.
*   `realizar_saque()`: Gerencia a operação de saque, incluindo validações de limite.
*   `solicitar_extrato()`: Exibe o extrato da conta.
*   `main()`: Função principal que inicializa o sistema e gerencia o fluxo do menu.

## Próximos Passos e Melhorias 

Este projeto pode ser expandido e aprimorado de diversas formas, como:

*   **Refatoração para POO (Programação Orientada a Objetos):** Organizar o código em classes como `Cliente`, `Conta`, `Transacao` para melhor modularidade e manutenção.
*   **Persistência de Dados:** Implementar o armazenamento de dados em um banco de dados (ex: SQLite, MySQL) para que as informações não sejam perdidas ao encerrar o programa.
*   **Tratamento de Erros:** Adicionar mais validações e tratamento de exceções para entradas inválidas do usuário.
*   **Interface Gráfica:** Desenvolver uma interface de usuário mais amigável (GUI).
*   **Testes Unitários:** Criar testes para garantir o correto funcionamento de cada função.

---
