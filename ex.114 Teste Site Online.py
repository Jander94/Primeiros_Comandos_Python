from matematica import limpar
import urllib.request
limpar()
try:
    n = urllib.request.urlopen("http://pudim.com.br/").getcode()
    if n == 200:
        print('O site está acessível')
except:
    print('O Site não esta acessível no momento. \nVerifique sua conexão e tente novamente')
    