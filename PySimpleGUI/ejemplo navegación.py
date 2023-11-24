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

def crearVentanaRegistro():
    col1 = sg.Col([
        [sg.Text("Email")],
        [sg.Text("Contraseña")],
        [sg.Text("Repetir contraseña")],
        [sg.Text("Nombre")],
        [sg.Text("Apellido paterno")],
        [sg.Text("Apellido materno")],
        [sg.Text("Recibir notificaciones")]
        ])
    col2 = sg.Col([
        [sg.Input(key="registro input email")],
        [sg.Input(key="registro input password",
                  password_char="*")],
        [sg.Input(key="registro input repetir password",
                  password_char="*")],
        [sg.Input(key="registro input nombre")],
        [sg.Input(key="registro input apellido paterno")],
        [sg.Input(key="registro input apellido materno")],
        [sg.Radio("Sí",
                  key="registro radio notificaciones sí",
                  group_id="registro notificaciones",
                  default=True),
         sg.Radio("No",
                  key="registro radio notificaciones no",
                  group_id="registro notificaciones")]
        ])
    layout = [
        [col1, col2],
        [sg.Button("Registrarse", key="registro button registro"),
         sg.Button("Cancelar", key="registro button cancelar")]
        ]
    return sg.Window("Registro de usuario",
                     layout,
                     finalize=True,
                     element_justification="center")

def crearVentanaMenuPrincipal():
    layout = [
        [sg.Text("Menú principal")]
        ]
    return sg.Window("Menú principal",
                     layout,
                     finalize=True,
                     element_justification="center")

ventanaLogin = crearVentanaLogin()
ventanaRegistro = None
ventanaMenuPrincipal = None

while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WINDOW_CLOSED:
        window.close()
        break
    # ¿En qué ventana estamos?
    # ¿A qué botón se le dio clic (evento)?
    # ¿La ventana a la que nos dirigimos está cerrada (None)?
    # ---------------------
    # Cerrar la ventana actual
    # Guardar el valor de None en la venta actual
    # Ejecutar la función de la ventana a la que nos dirigimos
    
    # Ventana Login
    # Login
    elif window == ventanaLogin and \
         event == "login button login" and \
         ventanaMenuPrincipal is None:
        email = values["login input email"]
        contraseña = values["login input password"]
        df = pd.read_csv("usuarios.csv")
        if len(df[(df["Email"] == email)&(df["Contraseña"] == contraseña)]) >= 1:            
            window.close()
            ventanaLogin = None
            ventanaMenuPrincipal = crearVentanaMenuPrincipal()
        else:
            sg.Popup("Error, usuario o contraseña incorrectos.",
                     title="Error")
    # Registro
    elif window == ventanaLogin and \
         event == "login button registro" and \
         ventanaRegistro is None:
        window.close()
        ventanaLogin = None
        ventanaRegistro = crearVentanaRegistro()