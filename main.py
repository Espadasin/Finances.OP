import time
import PySimpleGUI as sg
from Menu_principal import *
from Menu import *
from Cadastro import *

Tema_claro = True
user = {"nome": None, 
        "senha": None, 
        "idade": None}

sg.theme("SystemDefault")
print(user)


#Windows:
def main():
  global Tema_claro

  layout = [[sg.Text("Bem-Vindo(a)", text_color="blue", font="arial 12 bold")],
            [
              sg.Text("Nome: ", font="arial 12 bold"),
              sg.InputText(key="Nome_Input")
            ],
            [
              sg.Text("Senha:", font="arial 12 bold"),
              sg.InputText(password_char="*", key="Senha_Input")
            ],
            [
              sg.Button("Login"),
              sg.Button("Cadastrar"),
              sg.Button("",
                        image_filename="img1.png",
                        image_size=(20, 20),
                        key="Tema Escuro")
            ]]

  window1 = sg.Window("Finances.OP",
                      layout,
                      element_justification='center',
                      finalize=True)

  pass

  while True:
    event, values = window1.read()

    if event == sg.WIN_CLOSED:
      break

    if event == "Cadastrar":
      window1.hide()
      tela_de_cadastro(user)
      window1.un_hide()
      print(event)

    if event == "Login" and values["Nome_Input"] in user.values(
    ) and values["Senha_Input"] in user.values():
      window1.hide()
      menu(user["nome"])
      window1.un_hide()
    elif event == "Login" and values["Nome_Input"] == "" and values[
        "Senha_Input"] == "":
      sg.popup("Insira nome e senha", title=" ")
    elif event == "Login" and values["Nome_Input"] == "":
      sg.popup("Insira nome", title=" ")
    elif event == "Login" and values["Senha_Input"] == "":
      sg.popup("Insira senha", title=" ")
    elif event == "Login" and values["Senha_Input"] == user[
        "senha"] and values["Nome_Input"] != user["nome"]:
      sg.popup("Nome incorreto", title=" ")
    elif event == "Login" and values["Nome_Input"] in user[
        "nome"] and values["Senha_Input"] != user["senha"]:
      sg.popup("Senha incorreta", title=" ")
    elif event == "Login" and values["Nome_Input"] != user["nome"] and values[
        "Senha_Input"] != user["senha"]:
      sg.popup("Nome ou senha incorreto", title=" ")

    if event == "Tema Escuro" and Tema_claro:
      window1.hide()
      sg.theme("Black")
      Tema_claro = False
      main()
      window1.un_hide()

    elif event == "Tema Escuro" and not Tema_claro:
      window1.hide()
      sg.theme("SystemDefault")
      Tema_claro = True
      main()
  
  window1.close()


#Start Window
main()
