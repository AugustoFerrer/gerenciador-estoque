import unicodedata

estoque = {}
tamanhos_disponiveis = ["solteiro", "casal", "queen", "king"]

def limpar_texto(texto):
    texto_limpo = texto.strip().lower()
    
    texto_limpo = unicodedata.normalize('NFKD', texto_limpo)
    
    texto_limpo = texto_limpo.encode('ascii', 'ignore').decode('utf-8')
    
    return texto_limpo


def adicionar_item():
    print("Adicionando item...")
    
    tipo = limpar_texto(input("\nTipo do produto (Ex: Colchão, Base, Baú, Travesseiro...): "))
    produto = limpar_texto(input("\nNome do produto: "))

    if tipo == "colchao":
        
        tamanho = limpar_texto(input("\nTamanho: "))
        
        if tamanho in tamanhos_disponiveis:
            
            qtd = int(input("\nQuantidade: "))

            if produto not in estoque:
                estoque[produto] = {}

            if tamanho not in estoque[produto]:
                estoque[produto][tamanho] = { "Quantidade": qtd }
            else:
                estoque[produto][tamanho]["Quantidade"] += qtd
    
        else:
            print("\nERRO: Tamanho não encontrado")

    elif tipo == "base":

        tamanho = limpar_texto(input("\nTamanho: "))
        
        if tamanho in tamanhos_disponiveis:

            cor = limpar_texto(input("Cor: "))
            qtd = int(input("\nQuantidade: "))

            if produto not in estoque:
                estoque[produto] = {}

            if tamanho not in estoque[produto]:
                estoque[produto][tamanho] = { "Cor": cor, "Quantidade": qtd }
            else:
                estoque[produto][tamanho]["Quantidade"] += qtd
    
        else:
            print("\nERRO: Tamanho não encontrado")

    elif tipo in ["bau", "cabeceira"]:

        tamanho = limpar_texto(input("\nTamanho: "))
        
        if tamanho in tamanhos_disponiveis:

            cor = limpar_texto(input("Cor: "))
            material = limpar_texto(input("\nMaterial: "))
            qtd = int(input("\nQuantidade: "))

            if produto not in estoque:
                estoque[produto] = {}

            if tamanho not in estoque[produto]:
                estoque[produto][tamanho] = { "Cor": cor, "Material": material, "Quantidade": qtd }
            else:
                estoque[produto][tamanho]["Quantidade"] += qtd
    
        else:
            print("\nERRO: Tamanho não encontrado")



    






def registrar_venda():
    print("Registrando venda...")
    produto = limpar_texto(input("\nNome do produto vendido: "))

    if produto in estoque:
        
        tamanho = limpar_texto(input("\nTamanho: "))  
        cor = limpar_texto(input("\nCor: "))
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