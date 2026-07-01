estoque = {}

def adicionar_item():
    print("Adicionando item...")
    produto = input("\nNome do produto: ")
    qtd = int(input("\nQuantidade: "))
    
    if produto in estoque:
        estoque[produto] += qtd
    else:
        estoque[produto] = qtd

def registrar_venda():
    print("Registrando venda...")
    produto = input("\nNome do produto vendido: ")

    if produto in estoque:
        qtd_vendida = int(input("Quantidade vendida: "))
        
        if estoque[produto] >= qtd_vendida:
            estoque[produto] -= qtd_vendida
            print("\nVenda registrada com sucesso")
        else:
            print("\nERRO: Quantidade insuficiente no estoque")
    else:
        print("\nERRO: Produto não encontrado")

def listar_estoque():
    print(estoque)

while True:
    print("""
    ==============================
        CONTROLE DE ESTOQUE
    ==============================
    [1] ADICIONAR ITEM
    [2] REGISTRAR VENDA
    [3] LISTAR ESTOQUE
    [4] SAIR
    ==============================
          """)
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_item()

    elif opcao == "2":
        registrar_venda()

    elif opcao == "3":
        listar_estoque()

    elif opcao == "4":
        break

    else:
        print("Opção indisponível. Escolha uma das opcões disponíveis.")