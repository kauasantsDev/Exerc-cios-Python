print("="*20)
print(">>> LOJA PCISTA <<<")
print("="*20)
continuar = barato = ""
tot = caro = menor = cont = 0

while continuar != "N":
    produto = input("Nome do produto: ")
    preco = float(input("Preço: R$"))
    continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
    cont += 1
    tot += preco
    if preco > 1000:
        caro += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto

print("------- FIM DO PROGRAMA -------")
print(f"O total da compra foi R${tot:.2f}")
print(f"Temos {caro} produto (s) custando mais que R$1000,00.")
print(f"O produto mais barato é o (a) {barato} que custa {menor:.2f}.")
