import unicodedata

historico_vendas = {}
estoque = {}
tamanhos_disponiveis = ["solteiro", "casal", "queen", "king"]
tipos_disponiveis = ["colchao", "base", "bau", "travesseiro", "cabeceira", "guarda roupa"]


def limpar_texto(texto):
    texto_limpo = texto.strip().lower()
    
    texto_limpo = unicodedata.normalize('NFKD', texto_limpo)
    
    texto_limpo = texto_limpo.encode('ascii', 'ignore').decode('utf-8')

    texto_limpo = texto_limpo.replace("-", " ")
    
    return texto_limpo



def adicionar_item():
    print("Adicionando item...")

    ficha_infos = {}
    
    tipo = limpar_texto(input("\nTipo do produto (Ex: Colchão, Base, Baú, Travesseiro...): "))
    if tipo not in tipos_disponiveis:
        print("\nERRO: Tipo não encontrado")
        return
    ficha_infos["tipo"] = tipo   
    
    produto = limpar_texto(input("\nNome do produto: "))

    if tipo in ("travesseiro", "guarda roupa"):
        tamanho = "unico"
    else:
        tamanho = limpar_texto(input("\nTamanho: "))
        if tamanho not in tamanhos_disponiveis:
                print("\nERRO: Tamanho não encontrado")
                return
        
    if produto not in estoque:
        estoque[produto] = {}
    
    if tipo in ("colchao", "travesseiro"):
        pass

    # TENHO QUE ADICIONAR VERIFICACAO DE INPUT DE COR MATERIAL E PORTAS

    elif tipo == "base":
        ficha_infos["cor"] = limpar_texto(input("\nCor: "))

    elif tipo in ("bau", "cabeceira"):
        ficha_infos["cor"] = limpar_texto(input("\nCor: "))
        ficha_infos["material"] = limpar_texto(input("\nMaterial: "))

    elif tipo == "guarda roupa":
        ficha_infos["cor"] = limpar_texto(input("\nCor: "))
        ficha_infos["portas"] = limpar_texto(input("\nQuantidade de portas: "))
       
    qtd = int(input("\nQuantidade: "))
    ficha_infos["qtd"] = qtd

    if tamanho not in estoque[produto]:
         estoque[produto][tamanho] = ficha_infos
    else:
        estoque[produto][tamanho]["qtd"] += qtd
    
    return


def listar_estoque():
    print("\n--- ESTOQUE ATUAL ---")
    
    #.items() só recebe 2 variaveis pra separar, então tive que fazer um for dentro de outro pra extrair o dicionario interno (informacoes)

    for produto, tamanho in estoque.items():
        
    # Nesse momento:
    # produto = "bau"
    # tamanho = ("casal" : ficha_infos) <--- O Python guardou o dicionário de dentro aqui!  
    
        for tamanho, ficha in tamanho.items():

            tipo = ficha["tipo"]
            cor = ficha.get("cor", "-")
            material = ficha.get("material", "-")
            portas = ficha.get("portas", "-")   
    
        # tamanho = "Casal"
        # ficha = (ficha_infos)
    
            print(f"tipo: {tipo} || produto: {produto} / tamanho: {tamanho} / cor: {cor} / material: {material} / portas: {portas}")
    print("---------------------")

    return


def registrar_venda():
    print("Registrando venda...")
    
    id = limpar_texto(input("\nID da venda: "))
    if id in historico_vendas:
        print("\nERRO: ID já existente")
        return
    
    produto = limpar_texto(input("\nNome do produto vendido: "))
    if produto not in estoque:
        print("\nERRO: Produto não encontrado")
        return
    
    tamanho = limpar_texto(input("\nTamanho: "))  
    cor = limpar_texto(input("\nCor: "))
    caracteristicas = (tamanho, cor)

    if caracteristicas not in estoque[produto]:
        print("\nERRO: Modelo não encontrado")
        return
    else:    
        qtd_vendida = int(input("\nQuantidade vendida: "))
        
        if estoque[produto][caracteristicas] < qtd_vendida:
            print("\nERRO: Quantidade insuficiente no estoque")
            return
        else:
            estoque[produto][caracteristicas] -= qtd_vendida
            print("\nVenda registrada com sucesso")

            if estoque[produto][caracteristicas] <= 5:
                print("ATENÇÃO: Estoque baixo para este modelo!")
    return


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