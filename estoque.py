# SEPARAR EM OUTROS ARQUIVOS .py

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



def adicionar_item_ANTIGO():
    print("Adicionando item...")

    ficha_infos = {}
    
    tipo = limpar_texto(input("\nTipo do produto (Ex: Colchão, Base, Baú, Travesseiro...): "))
    if tipo not in tipos_disponiveis:
        print("\nERRO: Tipo não encontrado")
        return
    ficha_infos["tipo"] = tipo
    if tipo not in estoque:
        estoque[tipo] = {}   
    
    produto = limpar_texto(input("\nNome do produto: "))
    ficha_infos["produto"] = produto
    if tipo in ("travesseiro", "guarda roupa"):
        tamanho = "unico"
    else:
        tamanho = limpar_texto(input("\nTamanho: "))
        if tamanho not in tamanhos_disponiveis:
                print("\nERRO: Tamanho não encontrado")
                return
        
    # gurdar apenas tamanho na ficha logo abaixo, tirar tipo e nao por produto pra nao ter redundancia ja que eles são chaves (bug)
    ficha_infos["tamanho"] = tamanho
        
    if produto not in estoque[tipo]:
        estoque[tipo][produto] = {}
    
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

    # criando chave variante (SKU)
    caracteristicas = [tamanho]

    if "cor" in ficha_infos:
        cor = ficha_infos["cor"]
        caracteristicas.append(cor)

    if "material" in ficha_infos:
        material = ficha_infos["material"]
        caracteristicas.append(material)   

    if "portas" in ficha_infos:
        portas = ficha_infos["portas"]
        caracteristicas.append(portas)

    chave_sku = "-".join(caracteristicas)     

    # chave criada

    if chave_sku not in estoque[tipo][produto]:
         estoque[tipo][produto][chave_sku] = ficha_infos
    else:
        estoque[tipo][produto][chave_sku]["qtd"] += qtd
    
    return




def adicionar_item(tipo, produto, tamanho, cor, material, portas):
    print("Adicionando item...")

    ficha_infos = {}
    
    tipo = limpar_texto(input("\nTipo do produto (Ex: Colchão, Base, Baú, Travesseiro...): "))
    if tipo not in tipos_disponiveis:
        print("\nERRO: Tipo não encontrado")
        return
    ficha_infos["tipo"] = tipo
    if tipo not in estoque:
        estoque[tipo] = {}   
    
    produto = limpar_texto(input("\nNome do produto: "))
    ficha_infos["produto"] = produto
    if tipo in ("travesseiro", "guarda roupa"):
        tamanho = "unico"
    else:
        tamanho = limpar_texto(input("\nTamanho: "))
        if tamanho not in tamanhos_disponiveis:
                print("\nERRO: Tamanho não encontrado")
                return
        
    # gurdar apenas tamanho na ficha logo abaixo, tirar tipo e nao por produto pra nao ter redundancia ja que eles são chaves (bug)
    ficha_infos["tamanho"] = tamanho
        
    if produto not in estoque[tipo]:
        estoque[tipo][produto] = {}
    
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

    # criando chave variante (SKU)
    caracteristicas = [tamanho]

    if "cor" in ficha_infos:
        cor = ficha_infos["cor"]
        caracteristicas.append(cor)

    if "material" in ficha_infos:
        material = ficha_infos["material"]
        caracteristicas.append(material)   

    if "portas" in ficha_infos:
        portas = ficha_infos["portas"]
        caracteristicas.append(portas)

    chave_sku = "-".join(caracteristicas)     

    # chave criada

    if chave_sku not in estoque[tipo][produto]:
         estoque[tipo][produto][chave_sku] = ficha_infos
    else:
        estoque[tipo][produto][chave_sku]["qtd"] += qtd
    
    return


def listar_estoque():
    print("\n--- ESTOQUE ATUAL ---")
    
    #.items() só recebe 2 variaveis pra separar

    for nome_tipo, diconario_produtos in estoque.items(): 
    
        for nome_produto, dicionario_skus in diconario_produtos.items():

            for chave_sku, ficha in dicionario_skus.items():

                tamanho = ficha["tamanho"]
                cor = ficha.get("cor", "-")
                material = ficha.get("material", "-")
                portas = ficha.get("portas", "-")   
        
                print(f"tipo: {nome_tipo} || produto: {nome_produto} / tamanho: {tamanho} / cor: {cor} / material: {material} / portas: {portas}")
        print("---------------------")

    return


def registrar_venda():
    print("Registrando venda...")
    
    id = limpar_texto(input("\nID da venda: "))
    if id in historico_vendas:
        print("\nERRO: ID já existente")
        return

    tipo = limpar_texto(input("\nNome do tipo vendido: "))
    if tipo not in estoque:
        print("\nERRO: Tipo não encontrado")
        return

    produto = limpar_texto(input("\nNome do produto vendido: "))
    if produto not in estoque[tipo]:
        print("\nERRO: Produto não encontrado")
        return

    # fazendo busca por indice
    skus_disponiveis = list(estoque[tipo][produto].keys())
    
    for index, sku in enumerate(skus_disponiveis):
        print(f"{index} - {sku}")

    opcao = int(input("\nEscolha a opção: "))

    sku_escolhido = skus_disponiveis[opcao]
    
    qtd_vendida = int(input("\nQuantidade vendida: "))


    if estoque[tipo][produto][sku_escolhido]["qtd"] < qtd_vendida:
        print("\nERRO: Quantidade insuficiente no estoque")
        return
    else:
        estoque[tipo][produto][sku_escolhido]["qtd"] -= qtd_vendida

        ficha_vendas = estoque[tipo][produto][sku_escolhido].copy()
        del ficha_vendas["qtd"]
        ficha_vendas["qtd_vendida"] = qtd_vendida
        ficha_vendas["vendedor"] = limpar_texto(input("\nVendedor: "))
        historico_vendas[id] = ficha_vendas

        print("\nVenda registrada com sucesso")

        if estoque[tipo][produto][sku_escolhido]["qtd"] <= 5:
            print("\nATENÇÃO: Estoque baixo para este modelo!")
    return


def mostrar_layout():
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


while True:

    mostrar_layout()
    
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