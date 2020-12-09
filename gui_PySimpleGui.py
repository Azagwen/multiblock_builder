import PySimpleGUI as sg

sg.theme("DarkGreen5")

layout = [
    [sg.Text("Hewo fwend UwU")],
    [sg.Button("Ok"), sg.Button("no")]
]
window = sg.Window(
    title="Hell... OwO Wowd !",
    layout=layout,
    margins=(200, 200)
)

while True:
    event, values = window.read()

    if event == "Ok" or event == sg.WIN_CLOSED:
        break
