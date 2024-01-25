import xmltodict
import os
import pandas as pd

#função para ler o arquivo xml
def info_arquivo(arquivo_nome, valores):
    with open(f'nfs/{arquivo_nome}', "rb") as arquivo_xml:
        dicionario = xmltodict.parse(arquivo_xml)
        
        #pegando informaçoes no .xml
        if "NFe" in dicionario:
            inf_nf = dicionario["NFe"]['infNFe']
        else:
            inf_nf = dicionario['nfeProc']["NFe"]['infNFe']
        
        #pegando numero da nota
        numero_nota = inf_nf["@Id"]
        #pegando empresa emissora
        empresa_emissora = inf_nf['emit']['xNome']
        #nome
        nome_cliente = inf_nf["dest"]["xNome"]
        #endereco
        endereco = inf_nf["dest"]["enderDest"]
        
        #se existir volume imprima o volume, se não, imprima "nada informado"
        if"vol" in inf_nf["transp"]:
            peso = inf_nf["transp"]["vol"]["pesoB"]
        else:
            peso = "Nada informado"
        valores.append([numero_nota,empresa_emissora,nome_cliente,endereco,peso])

lista_arquivos = os.listdir("nfs")

colunas = ["numero_nota", "empresa_emissora", "nome_cliente","endereco", "peso"]
valores = []

for arquivo in lista_arquivos:
    info_arquivo(arquivo, valores)

tabela = pd.DataFrame(columns = colunas, data=valores)
tabela.to_excel("NotasFicais.xlsx", index=False)