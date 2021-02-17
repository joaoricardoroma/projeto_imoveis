import requests
from FunImoveis import Imovel
from bs4 import BeautifulSoup



r = requests.get('https://venda-imoveis.caixa.gov.br/listaweb/Lista_imoveis_RJ.htm').text
soup = BeautifulSoup(r, "lxml")
lista_imoveis = []
imoveis = soup.find_all("tr")
del imoveis[0]
for imovel in imoveis:
    endereco = imovel.find_all("td")[1].text.strip()
    bairro = imovel.find_all("td")[2].text.strip()
    descricao = imovel.find_all("td")[3].text.strip()
    preco = imovel.find_all("td")[4].text.strip()
    cidade = imovel.find_all("td")[-2].text.strip()
    estado = imovel.find_all("td")[-1].text.strip()
    desconto = imovel.find_all("td")[6].text.strip()
    modalidade_venda = imovel.find_all("td")[7].text.strip()

    obj_imovel = Imovel(endereco, bairro, descricao, preco, cidade, estado, desconto, modalidade_venda)
    lista_imoveis.append(obj_imovel)

while True:
    print("1) Cidade")
    print("2) Bairro")
    print("3) Desconto")
    print("4) modalidade de venda")
    print("5) filtro de preco personalizado")

    p1 = input("Como deseja filtrar os imoveis?(Escolha uma opcao acima)")

    if p1 == "1":
        lista_cidades = []
        for imovel in lista_imoveis:
            lista_cidades.append(imovel.cidade)

        lista_cidades_unicas = list(set(lista_cidades))
        for cidade in lista_cidades_unicas:
            print(cidade)

        resposta_cidade = input("Qual cidade deseja?").upper()
        print(f"Segue a lista de cidades")

        for imovel in lista_imoveis:
            if imovel.cidade == resposta_cidade:
                print(imovel)

    if p1 == "2":
        lista_bairros = []

        for imovel in lista_imoveis:
            lista_bairros.append(imovel.bairro)

        lista_bairros_unica = list(set(lista_bairros))
        for bairro in lista_bairros_unica:
            print(bairro)

        resposta_bairro = input("Qual Bairro deseja?").upper()
        print(f"Segue a lista de bairros")

        for imovel in lista_imoveis:
            if imovel.bairro == resposta_bairro:
                print(imovel)

    if p1 == "3":

        resposta_desconto = float(input("Acima de quantos porcento deseja filtrar?"))
        for imovel in lista_imoveis:
            if imovel.desconto >= resposta_desconto:
                print(imovel)

    if p1 == "4":
        resposta_venda= input("Qual dos dois tipos de venda deseja ver?")
        for imovel in lista_imoveis:
            if imovel.modalidade_venda == resposta_venda:
                print(imovel)

    if p1 == "5":
        resposta_preco = input("Deseja ordenar os precos em ordem decrescente ou crescente?").lower()
        for imovel in lista_imoveis:
            if resposta_preco == "decrescente":
                lista_imoveis.sort(key=lambda x: x.preco, reverse=True)
                print(imovel)
            else:
                lista_imoveis.sort(key=lambda x: x.preco, reverse=False)
                print(imovel)

