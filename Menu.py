import time
import os
import PySimpleGUI as sg

def juros():
    layout = [
        [sg.Text("Juros Compostos")],
        [sg.Text("Capital:"), sg.InputText(key="Capital")],
        [sg.Text("Taxa % a.m.:"),sg.InputText(key="Taxa")],
        [sg.Text("Tempo (meses):"),sg.InputText(key="Qnt_anos/meses")],
        [sg.Button("Calcular"), sg.Button("Voltar")]
    ]

    window = sg.Window("Finances.OP", layout, element_justification="left", finalize=True)

    while True:
      event,values = window.read()

      if event == sg.WIN_CLOSED:
          break

      if event == "Voltar":
        window.hide()
        return

      try:
          int(values["Capital"])
          int(values["Qnt_anos/meses"])
          int(values["Taxa"])
      except:
          sg.popup("Valor invalido",title=" ")
      else:
          if event == "Calcular":
              mo = int(values["Capital"]) * pow((1 + int(values["Taxa"]) / 100), int(values["Qnt_anos/meses"]))
              sg.popup(f"\nJuros Compostos -> {mo:,.2f}",title=" ")
            
def juros_simples():
    layout = [
        [sg.Text("Juros Simples")],
        [sg.Text("Capital:"), sg.InputText(key="Capital")],
        [sg.Text("Taxa:"),sg.InputText(key="Taxa")],
        [sg.Button("Calcular"), sg.Button("Voltar")]
    ]

    window = sg.Window("Finances.OP", layout, element_justification="left", finalize=True)

    while True:
      event, values = window.read()

      if event == sg.WIN_CLOSED:
        break

      if event == "Voltar":
        window.hide()
        return

      try:
        int(values["Capital"])
        int(values["Taxa"])
      except:
        sg.popup("Valor Invalido", title=" ")
      else:
        if event == "Calcular":
          e = int(values["Capital"])*(int(values["Taxa"])/100)
          m = int(values["Capital"]) + e
          
          sg.popup(f"Montante -> {m:,.2f}" ,title=" ")

def gastos():
  gastos = []
  with open("gastosBD.txt","r+") as arquivo:
    for frases in arquivo:
      frases = frases[:-1]
      gastos.append(frases)
      print("adicionado")
      
			

    print(gastos)
    
    layout = [
      [sg.Listbox(values=gastos, size=(20,10),key="Lista")],
      [sg.Text("Nome da loja")],
      [sg.InputText(key="loja")],
      [sg.Text("Gasto na loja")],
      [sg.InputText(key="gastos")],
      [sg.Button("Adicionar"), sg.Button("Limpar Tudo") ,sg.Button("Voltar")]
    ]
  
    window = sg.Window("Finances.OP", layout, size=(400,400))
  	
    while True:
      event, values = window.read()
      if event == sg.WIN_CLOSED:
        break
  
      if event == "Adicionar":
        try:
          int(values["gastos"])
        except:
          sg.popup("Caracteres Invalidos",title=" ")
        else:
          gastos.append([values["loja"],":",int(values["gastos"])])
          window["Lista"].update(values=gastos)
          arquivo.write((values["loja"]+" : "+values["gastos"]+"\n"))
          window.refresh()
        
      if event == "Voltar":
        window.hide()
        return
        window.un_hide()

      if event == "Limpar Tudo":
        arquivo.truncate(0)
        gastos.clear()
        window["Lista"].update(values=gastos)
        window.refresh()
      
      

                
      