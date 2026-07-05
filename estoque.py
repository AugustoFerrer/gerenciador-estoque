estoque = {}
tamanhos_disponiveis = ["solteiro", "casal", "queen", "king"]


def adicionar_item():
    print("Adicionando item...")
    produto = input("\nNome do produto: ").lower()
    tamanho = input("\nTamanho: ").lower()
    if tamanho in tamanhos_disponiveis:
        
        cor = input("\nCor: ").lower()
        caracteristicas = (tamanho, cor) 
        qtd = int(input("\nQuantidade: "))

        if produto not in estoque:
            estoque[produto] = {}

        if caracteristicas in estoque[produto]:
            estoque[produto][caracteristicas] += qtd
        else:
            estoque[produto][caracteristicas] = qtd
    
    else:
        print("\nERRO: Tamanho não encontrado")



def registrar_venda():
    print("Registrando venda...")
    produto = input("\nNome do produto vendido: ").lower()

    if produto in estoque:
        
        tamanho = input("\nTamanho: ").lower()    
        cor = input("\nCor: ").lower()
        caracteristicas = (tamanho, cor)

        if caracteristicas in estoque[produto]:
                
                qtd_vendida = int(input("\nQuantidade vendida: "))
                
                if estoque[produto][caracteristicas] >= qtd_vendida:
                    estoque[produto][caracteristicas] -= qtd_vendida
                    print("\nVenda registrada com sucesso")

                    if estoque[produto][caracteristicas] <= 5:
                        print("ATENÇÃO: Estoque baixo para este modelo!")
                else:
                    print("\nERRO: Quantidade insuficiente no estoque")
        
        else:
            print("\nERRO: Modelo não encontrado")

    else:
        print("\nERRO: Produto não encontrado")



def listar_estoque():
    print("\n--- ESTOQUE ATUAL ---")
    
    #.items() só recebe 2 variaveis pra separar, então tive que fazer um for dentro de outro pra extrair o dicionario interno (informacoes)

    for produto, informacoes in estoque.items():
        
    # Nesse momento:
    # produto = "Ravenna"
    # informacoes = {("Casal", "Branco"): 10} <--- O Python guardou o dicionário de dentro aqui!  
    
        for caracteristicas, qtd in informacoes.items():
    
        # caracteristicas = ("Casal", "Branco")
        # qtd = 10
    
            tamanho = caracteristicas[0]
            cor = caracteristicas[1]

            print(f"Produto: {produto} | Tamanho: {tamanho} | Cor: {cor} | Quantidade: {qtd}")
    print("---------------------")



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