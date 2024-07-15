import PySimpleGUI as sg



def tela_de_cadastro(user):

    layout = [
        [sg.Text("Nome:",font="arial 12 bold"), sg.InputText(pad=(49,0), key="Nome")],
        [sg.Text("Senha:",font="arial 12 bold"), sg.InputText(pad=(44,0), password_char="*", key="Senha")],
        [sg.Text("Idade:",font="arial 12 bold"), sg.InputText(pad=(44,0), key="Idade")],
        [sg.Button("Voltar"), sg.Button("Cadastrar")]
    ]

    window = sg.Window("Cadastro", layout,finalize=True)

    while True:
        event, values = window.read()


        if event == sg.WIN_CLOSED:
            quit()


        if event == "Voltar":
            print((values["Idade"]))
            window.hide()
            return

        if event == "Cadastrar" and values["Senha"] == "" and values["Nome"] == "" and values["Idade"] == "":
            sg.popup("Insira os valores",title="")

        try:
            int(values["Idade"])
        except:
            pass
        else:
            if len(values["Senha"]) < 8:
                sg.popup("Insira uma senha com no minimo 8 caracteres",title="")
            
            elif int(values["Idade"]) >= 18 and int(values["Idade"]) <= 100:
                if event == "Cadastrar" and values["Senha"] != "" and values["Nome"] != "" and values["Idade"] != "":
                  user.update({"nome":values["Nome"],"senha":values["Senha"],"idade":values["Idade"]})         
                  window.hide()
                  return user
            else:
                sg.popup("Você e menor de idade",title="")