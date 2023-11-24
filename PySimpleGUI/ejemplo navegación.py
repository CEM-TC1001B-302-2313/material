import pandas as pd
import PySimpleGUI as sg

def crearVentanaLogin():
    col1 = sg.Col([
        [sg.Text("Email")],
        [sg.Text("Contraseña")]
        ])
    col2 = sg.Col([
        [sg.Input(key="login input email")],
        [sg.Input(key="login input password",
                  password_char="*")]
        ], element_justification="right")
    layout = [
        [col1, col2],
        [sg.Button("Login", key="login button login"),
         sg.Button("Registrarse", key="login button registro")]
        ]
    return sg.Window("Inicio de sesión",
                     layout,
                     finalize=True,
                     element_justification="center")

ventanaLogin = crearVentanaLogin()

while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WINDOW_CLOSED:
        window.close()
        break