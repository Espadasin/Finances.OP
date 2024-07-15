import PySimpleGUI as sg
from Menu import *
from cotacao import tela_cotacoes

def menu(nome):
  layout = [
    [sg.Button("Juros Compostos"), sg.Text(nome, justification="right")],
    [sg.Button("Juros Simples")],
    [sg.Button("Gastos")],
    [sg.Button("Cotação")],
    [sg.Button("Voltar")]
  ]
  
  window = sg.Window("  Finances.OP", layout, size=(553,228))

  while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
      break

    if event == "Juros Compostos":
      window.hide()
      juros()
      window.un_hide()
    if event == "Juros Simples":
      window.hide()
      juros_simples()
      window.un_hide()
    if event == "Cotação":
      window.hide()
      tela_cotacoes()
      window.un_hide()
    if event == "Gastos":
      window.hide()
      gastos()
      window.un_hide()     
    if event == "Voltar":
      window.hide()
      return
      