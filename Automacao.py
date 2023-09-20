#Importando a Biblioteca
from playwright.sync_api import sync_playwright
from tkinter import messagebox

import pandas as pd
import time

tmp =time.localtime()


#Chamando a Função e colocando um Nome para Chamar a Função
with sync_playwright() as navegador:

    # Chamadno o Navegador do Chrome para Inicializar, Headless = False é para mostrar a Tela do Google
    browser = navegador.chromium.launch(headless=False)
    page = browser.new_page()  # Mando o Navegador abrir uma Nova Página
    page.goto("https://geradornv.com.br/gerador-pessoas")  # Colocando o Link na Página

    # Criando um Contador para Gerar um Loop
    contador = 0
    # Inicializando as Listas da Automaçao
    nomes=[]
    nascimentos=[]
    cpfs=[]
    rgs=[]
    titulos=[]
    cnhs=[]
    categorias=[]
    passaportes=[]
    pisp=[]
    tsangue=[]

    for contador in range (5000):
        #Geranndo os Nomes, Nascimento, CPF

        #Clicando no Botão de Gerar Pessoa no Site
        page.locator('//*[@id="nv-new-generator-people"]').click()

        #Copiando os Nomes gerado pelo Site
        nome = page.locator('//*[@id="nv-field-name"]').text_content()
        #Copiando os Nascimento gerado pelo Site
        nascimento = page.locator('//*[@id="nv-field-birthday"]').text_content()
        #Copiando os CPF gerado pelo Site
        cpf = page.locator('//*[@id="nv-field-cpf"]').text_content()
        #Copiando os RGs gerado pelo Site
        rg = page.locator('//*[@id="nv-field-rg"]').text_content()
        #Copiando os Títulos de Eleitores pelo Site
        titulo = page.locator('//*[@id="nv-field-voter-registration"]').text_content()
        #Copiando a CNH pelo Site
        cnh= page.locator('//*[@id="nv-field-cnh"]').text_content()
        #Copiando a Categoria da CNH pelo Site
        categoria = page.locator('//*[@id="nv-field-category-cnh"]').text_content()
        #Copiando o Passaporte pelo Site
        passaporte = page.locator('//*[@id="nv-field-passport"]').text_content()
        #Copiando o Pis/Pasep pelo Site
        pis = page.locator('//*[@id="nv-field-pis-pasep"]').text_content()
        #Copiando o Tipo de Sangue pelo Site
        sangue= page.locator('//*[@id="nv-field-blood-types"]').text_content()

######################### 'Criando as Listas de Dados' #########################
        #Salvando os Dados Gerado pelo Contador na Lista
        #Criando uma Lista para os Nomes
        nomes.append({'Nome':nome})
        #Criando uma Lista para os Nascimento
        nascimentos.append(nascimento)
        #Criando uma Lista para os CPFs
        cpfs.append(cpf)
        #Criando uma Lista para os RGs
        rgs.append(rg)
        #Criando uma Lista para os Titulos de Eleitor
        titulos.append(titulo)
        #Criando uma lista para as CNHs
        cnhs.append(cnh)
        #Criando uma Lista para a Categoria das CNH
        categorias.append(categoria)
        #Criando uma Lista para o Passaporte
        passaportes.append(passaporte)
        #Crianco uma Lista para o Pis/Pasep
        pisp.append(pis)
        #Criando uma Lista para o Tipo de Sangue
        tsangue.append(sangue)

######################### 'Gerando a Planilha de Dados' #########################

    #Criando o Data Frame para Salvar os Dados da Planilha
    dados = pd.DataFrame(data=nomes)

    #Criando a Coluna com as Datas de Nascimento
    dados['Nascimento']=nascimentos
    #Criando a Coluna com os CPFs
    dados['CPF']=cpfs
    #Criando a Coluna com os RGs
    dados['RG']=rgs
    #Criando a Coluna com os Titulos
    dados['Titulo de Eleitor']=titulos
    #Criando a Coluna com as CNHs
    dados['CNH']=cnhs
    #Criando a Coluna com as Categorias da CNH
    dados['Categoria']=categorias
    #Criando a Coluna com os Passaportes
    dados['Passaporte']=passaportes
    #Criando a Coluna com o Pis/Pasep
    dados['PIS/PASEP']=pisp
    #Criando a Coluna com o Tipo de Sangue
    dados['Sangue']=tsangue

    #Arquivo XLSX criado
    dados.to_excel('Dados.xlsx',index=False)

messagebox.showinfo('Processo Concluido','Automação Terminou !\n'
                                         f'Data:{tmp[2]}/{tmp[1]}/{tmp[0]} Às {tmp[3]}h:{tmp[4]}m ')















