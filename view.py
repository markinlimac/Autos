import urllib.request, urllib.parse, urllib.error
from PyPDF2 import PdfFileReader
import requests, sys, time, os
import time
from datetime import datetime
from socket import error as SocketError
import errno

#class AutosJuridico():

def get(path, search):

  url = 'http://www.cnj.jus.br/dje/jsp/dje/DownloadDeDiario.jsp?dj=DJ{}_{}-ASSINADO.PDF&statusDoDiario=ASSINADO'.format(numDj, anoAtual)
  response = requests.get(url)
  contagem = []
  contagem = response.content[2:42]
  determinado = [79, 32, 97, 114, 113, 117, 105, 118, 111, 32, 115, 111, 108, 105, 99, 105, 116, 97, 100, 111, 32, 110, 227, 111, 32, 102, 111, 105, 32, 101, 110, 99, 111, 110, 116, 114, 97, 100, 111, 33]
  contador = 0
  for i in range(40):
    if(contagem[i] == determinado[i]):
      contador = contador + 1
  if contador == 40:
    print("Este arquivo nao existe!")
    print("")
    pass
  else:
    try:
        response = urllib.request.urlretrieve(url, "DJ-{}-{}.pdf".format(numDj, anoAtual))
        print('baixado')
        text_extractor(path, search)
    except SocketError as e:
        if e.errno != errno.ECONNRESET:
            raise # Not error we are looking for
        print('excessao')
        pass # Handle error here.

def text_extractor(path, search):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        number_of_pages = pdf.getNumPages()

        try:
            arquivo = open("DJ-{}-{}.txt".format(numDj, anoAtual), 'r+')
        except FileNotFoundError:
            arquivo = open("DJ-{}-{}.txt".format(numDj, anoAtual), 'w+')

        for numPage in range(number_of_pages):
            page = pdf.getPage(numPage)
            text = page.extractText()
            arquivo.write(text)

        arquivo.close()
        get_dataDj(path, search)

def search_word(path, search):
    datafile = open("DJ-{}-{}.txt".format(numDj,anoAtual), 'r+')
    for line in datafile:
        if search in line:
            found = True
            break
        else:
            found = False
    datafile.close()
    if found == True:
        print('Encontrado o processo {}'.format(search))
        local = os.getcwd()
        dir = os.listdir(local)
        for file in dir:
            if (file == "DJ-{}-{}.txt".format(numDj,anoAtual)):
                os.remove(file)
    else:
        print('Nao existe esse processo nesse DJ')
        local = os.getcwd()
        dir = os.listdir(local)
        for file in dir:
            if (file == "DJ-{}-{}.txt".format(numDj,anoAtual) or file == "DJ-{}-{}.pdf".format(numDj,anoAtual)):
                os.remove(file)
                print("arquivo removido com sucesso!")

def get_dataDj(path, search):
    datafile = open("DJ-{}-{}.txt".format(numDj,anoAtual), 'r+')
    mes_ext = {'janeiro': '1', 'fevereiro': '2', 'março': '3', 'abril': '4', 'maio': '5', 'junho': '6', 'julho': '7', 'agosto': '8', 'setembro': '9', 'outubro': '10', 'novembro': '11', 'dezembro': '12'}
    numeroLinha = 0
    for line in datafile:
        numeroLinha += 1
        if numeroLinha == 3:
            try:
                date = line.split(',')
                date = date[2].strip()
                dia, separador, mes, separador, ano = date.split(' ')
                print('{}/{}/{}'.format(dia, mes_ext[mes], ano))
                print(data_process)
                if int(ano) < int(year):
                    print('Este processo ainda nao havia sido criado! Finalizando programa')
                    datafile.close()
                    local = os.getcwd()
                    dir = os.listdir(local)
                    for file in dir:
                        if (file == "DJ-{}-{}.txt".format(numDj,anoAtual) or file == "DJ-{}-{}.pdf".format(numDj,anoAtual)):
                            os.remove(file)
                            print("arquivo removido com sucesso!")
                            print("")
                    sys.exit()
                elif int(mes_ext[mes]) < int(month) and int(ano) <= int(year):
                    print('Este processo ainda nao havia sido criado! Finalizando programa')
                    datafile.close()
                    local = os.getcwd()
                    dir = os.listdir(local)
                    for file in dir:
                        if (file == "DJ-{}-{}.txt".format(numDj,anoAtual) or file == "DJ-{}-{}.pdf".format(numDj,anoAtual)):
                            os.remove(file)
                            print("arquivo removido com sucesso!")
                            print("")
                    sys.exit()
                elif int(dia) < int(day) and int(mes_ext[mes]) <= int(month) and int(ano) <= int(year):
                    print('Este processo ainda nao havia sido criado! Finalizando programa')
                    datafile.close()
                    local = os.getcwd()
                    dir = os.listdir(local)
                    for file in dir:
                        if (file == "DJ-{}-{}.txt".format(numDj,anoAtual) or file == "DJ-{}-{}.pdf".format(numDj,anoAtual)):
                            os.remove(file)
                            print("arquivo removido com sucesso!")
                            print("")
                    sys.exit()
            except IndexError:
                print('')
        if numeroLinha == 4:
            try:
                date = line.split(',')
                date = date[2].strip()
                dia, separador, mes, separador, ano = date.split(' ')
                print('{}/{}/{}'.format(dia, mes_ext[mes], ano))
                print(data_process)
                if int(ano) < int(year):
                    print('Este processo ainda nao havia sido criado! Finalizando programa')
                    datafile.close()
                    local = os.getcwd()
                    dir = os.listdir(local)
                    for file in dir:
                        if (file == "DJ-{}-{}.txt".format(numDj,anoAtual) or file == "DJ-{}-{}.pdf".format(numDj,anoAtual)):
                            os.remove(file)
                            print("arquivo removido com sucesso!")
                            print("")
                    sys.exit()
                elif int(mes_ext[mes]) < int(month) and int(ano) <= int(year):
                    print('Este processo ainda nao havia sido criado! Finalizando programa')
                    datafile.close()
                    local = os.getcwd()
                    dir = os.listdir(local)
                    for file in dir:
                        if (file == "DJ-{}-{}.txt".format(numDj,anoAtual) or file == "DJ-{}-{}.pdf".format(numDj,anoAtual)):
                            os.remove(file)
                            print("arquivo removido com sucesso!")
                            print("")
                    sys.exit()
                elif int(dia) < int(day) and int(mes_ext[mes]) <= int(month) and int(ano) <= int(year):
                    print('Este processo ainda nao havia sido criado! Finalizando programa')
                    datafile.close()
                    local = os.getcwd()
                    dir = os.listdir(local)
                    for file in dir:
                        if (file == "DJ-{}-{}.txt".format(numDj,anoAtual) or file == "DJ-{}-{}.pdf".format(numDj,anoAtual)):
                            os.remove(file)
                            print("arquivo removido com sucesso!")
                            print("")
                    sys.exit()
            except IndexError:
                pass
    search_word(path, search)

if __name__ == '__main__':
  data_atual = str(datetime.now().date())
  anoAtual, mesAtual, diaAtual = data_atual.split('-')
  search = input("Digite o numero do processo: ")
  data_process = input("Digite a data do processo: ")
  day, month, year = data_process.split('/')
  for ano in range(int(anoAtual), 2008, -1):
      anoAtual = ano
      for i in range(400,0,-1):
        numDj = i#int(input("Digite o numero do diario de justica: "))
        path = 'DJ-{}-{}.pdf'.format(numDj, anoAtual)
        print('')
        print(path)
        get(path, search)

#0000876-86.2017.2.00.0000 WELLINGTON DOS SANTOS SILVA
#56 2017
#pesquisar por nome e data (data atual implementar)
#consultar todos djs procurando pelo nome
#caso nao ache excluir pdf e txt, passar para o proximo
#caso ache salve o pdf e exclui o txt e passa para o proximo
