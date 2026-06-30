estoque = {}

while True:
    print("""
    ==============================
        CONTROLE DE ESTOQUE
    ==============================
    [1] ADICIONAR ITEM
    [2] REGISTRAR VENDA
    [3] SAIR
    ==============================
          """)
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("adicionando item...")

    elif opcao == "2":
        print("registrando venda...")

    elif opcao == "3":
        break

    else:
        print("Opção indisponível. Escolha uma das opcões disponíveis.")
