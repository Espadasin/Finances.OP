import requests
import PySimpleGUI as sg

def pegar_cotacoes(moeda):
  try:
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    requisicao_dic = requisicao.json()
    cotacao = requisicao_dic[f'{moeda}BRL']['bid']

    return cotacao
  except:
    sg.popup("Cotaçao não identificada")

def tela_cotacoes():
  layout = [
      [sg.Text("Cotação da Moeda")],
      [sg.InputText(key="nome_cotacao")],
      [sg.Button("Pegar Cotação"), sg.Button("Cancelar")],
      [sg.Text("", key="texto_cotacao")],
  ]
  
  janela = sg.Window("Sistema de Cotações", layout)
  
  while True:
      evento, valores = janela.read()
      if evento == sg.WIN_CLOSED or evento == "Cancelar":
          break
      if evento == "Pegar Cotação":
          codigo_cotacao = valores["nome_cotacao"]
          cotacao = pegar_cotacoes(codigo_cotacao)
          janela["texto_cotacao"].update(f"A cotação do {codigo_cotacao} é de R${cotacao}")
  
  janela.close()