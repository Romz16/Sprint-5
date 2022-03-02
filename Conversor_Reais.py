#Bibilhotecas 
import requests
from bs4 import BeautifulSoup

#Funções 
def dolar():#Função para converter dolares para reais 
    x = float(input("Digite o valor para conversao em dolares para reais :"))#coleta a quantidade a ser convertida
    #requerimentos para que acesse a pagina no google com o valor atualizado 
    headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0'}
    page = requests.get("https://www.google.com/search?q=dolar&oq=dola&aqs=chrome.0.69i59j69i57j0i131i433i512l3j0i433i512l2j0i10i433i512j0i433i512l2.1401j1j9&sourceid=chrome&ie=UTF-8",headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    atributos = {'class':'g'}
    valor_dolar = soup.find_all("span",class_="DFlfde SwHCTb")[0]
    #pega o valor em texto e transforma em numero
    st = valor_dolar.text
    new_st = st.replace(',','.')
    numero = float(new_st)
    #calcula quanto o valor passado esta valendo em reais 
    valor = numero * x
    print("O valor atual da moeda é de : {} reais ".format(numero))
    print("A conversão do seu valor fica em : {} reais".format(valor))
    
def euro():#Função para converter euros para reais 
    x = float(input("Digite o valor para conversao em euros para reais :"))
    headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0'}
    page = requests.get("https://www.google.com/search?client=opera&q=euro&sourceid=opera&ie=UTF-8&oe=UTF-8",headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    atributos = {'class':'g'}
    valor_euro = soup.find_all("span",class_="DFlfde SwHCTb")[0]
    st = valor_euro.text
    new_st = st.replace(',','.')
    numero = float(new_st)
    valor = numero * x
    print("O valor atual da moerda é de : {} reais ".format(numero))
    print("A conversão do seu valor fica em : {} reais ".format(valor))
    
def peso():#Função para converter pesos para reais 
    x = float(input("Digite o valor para conversao em pesos para reais :"))
    headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0'}
    page = requests.get("https://www.google.com/search?q=pesos+argentinos&client=opera&ei=JATvYZPeEebZ1sQP6bCLkA0&ved=0ahUKEwiTgMvHlcv1AhXmrJUCHWnYAtIQ4dUDCA0&uact=5&oq=pesos+ar&gs_lcp=Cgdnd3Mtd2l6EAMyDQgAEIAEELEDEEYQggIyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgAEEcQsAM6BwgAELADEEM6CggAEOQCELADGAA6DAguEMgDELADEEMYAToECAAQQzoHCAAQgAQQCjoGCAAQFhAeOgkIABBDEEYQggI6CAgAEIAEELEDSgQIQRgASgQIRhgBUJABWIIQYL5DaAJwAngAgAGcAYgBvAqSAQMwLjmYAQCgAQHIARHAAQHaAQYIABABGAnaAQYIARABGAg&sclient=gws-wiz",headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    atributos = {'class':'g'}
    valor_peso = soup.find_all("span",class_="DFlfde SwHCTb")[0]
    st = valor_peso.text
    new_st = st.replace(',','.')
    numero = float(new_st)
    valor = numero * x
    print("O valor atual da moerda é de : {} reais ".format(numero))
    print("A conversão do seu valor fica em : {} reais".format(valor))
    
    
#Incio do programa 
while (True):#repetição para que o programa so termine quando o usuario quiser sair
    print("\nDeseja converter qual moeda para reais (A conversão usa valores atualizados) ?\n")
    print(" 1.Dolar\n 2.Euro\n 3.Pesos\n 4.sair")
    opcao = input ("Digite uma opção:  ")
#Chama uma função conforme o usuario queira 
    if (opcao =='1'):
        dolar()
    elif(opcao =='2'):
        euro()
    elif(opcao =='3'):
        peso()
    elif(opcao =='sair'):
        break
    