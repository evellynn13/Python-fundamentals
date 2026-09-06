# atribuicao da valores a variaveis
hamburguer = 10.00   
batata_frita = 3.50
refrigerante = 2.00
# entrada de dados do restaurante
quantidade_hamburguer = int(input("Digite a quantidade de hambúrgueres desejados: "))
quantidade_batata = int(input("Digite a quantidade de batatas fritas desejadas: "))
quantidade_refrigerante = int(input("Digite a quantidade de refrigerantes desejados: "))

# calculo do valor total do pedido
preco_total = (hamburguer * quantidade_hamburguer) + (batata_frita * quantidade_batata) + (refrigerante * quantidade_refrigerante)    
print("o valor total do pedido é: R$", preco_total)
