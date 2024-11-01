class Produto:
    def __init__(self, id, nome, imagem, preco):
        self.id = id
        self.nome = nome
        self.imagem = imagem
        self.preco = preco

listProdutos = []
listProdutos.append(Produto("1", "Headset JBL Tune 520BT", "jbl", 239.00))
listProdutos.append(Produto("2", "Apple AirPods (3ª geração)​​​​​​", "apple", 1405.98))
listProdutos.append(Produto("3", "Samsung Galaxy Buds3", "samsung", 1249.00))
