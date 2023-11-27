import pandas as pd
import PySimpleGUI as sg

sg.set_options(font="Arial 18")

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
    # Login -> Menú Principal
    elif window == ventanaLogin and \
         event == "login button login" and \
         ventanaMenuPrincipal is None:
        email = values["login input email"]
        contraseña = values["login input password"]
        df = pd.read_csv("usuarios.csv")
        if len(df[(df["Email"] == email)
                  &(df["Contraseña"] == contraseña)]) >= 1:            
            window.close()
            ventanaLogin = None
            ventanaMenuPrincipal = crearVentanaMenuPrincipal()
        else:
            sg.Popup("Error, usuario o contraseña incorrectos.",
                     title="Error")
    # Registrarse -> Ventana Registro
    elif window == ventanaLogin and \
         event == "login button registro" and \
         ventanaRegistro is None:
        window.close()
        ventanaLogin = None
        ventanaRegistro = crearVentanaRegistro()
    # Ventana Registro
    # Cancelar -> Login
    elif window == ventanaRegistro and \
         event == "registro button cancelar" and \
         ventanaLogin is None:
        window.close()
        ventanaRegistro = None
        ventanaLogin = crearVentanaLogin()
    # Registrar -> Login
    elif window == ventanaRegistro and \
         event == "registro button registro" and \
         ventanaLogin is None:
        email = values["registro input email"].strip()
        password = values["registro input password"].strip()
        repetir_password = values["registro input repetir password"].strip()
        nombre = values["registro input nombre"].strip()
        apellido_paterno = values["registro input apellido paterno"].strip()
        apellido_materno = values["registro input apellido materno"].strip()
        if values["registro radio notificaciones sí"]:
            notificaciones = "sí"
        else:
            notificaciones = "no"
        lista_errores = []
        if "@" not in email:
            lista_errores.append("El formato del correo es incorrecto.")
        if not nombre:
            lista_errores.append("Debes llenar el nombre.")
        if not apellido_paterno:
            lista_errores.append("Debes llenar el apellido paterno.")
        if not apellido_materno:
            lista_errores.append("Debes llenar el apellido materno.")
        if not password:
            lista_errores.append("Debes llenar la contraseña.")
        if password != repetir_password:
            lista_errores.append("Las contraseñas deben coincidir.")
        # Revisamos que no haya errores en la lista
        if not lista_errores:
            nuevo_registro = pd.DataFrame([{
                "Email": email,
                "Contraseña": password,
                "Nombre": nombre,
                "Apellido paterno": apellido_paterno,
                "Apellido materno": apellido_materno,
                "Notificaciones": notificaciones
                }])
            df = pd.read_csv("usuarios.csv")
            df = pd.concat([df, nuevo_registro], ignore_index=False)
            df.to_csv("usuarios.csv", index=False)
            sg.Popup("Registro exitoso", title="¡Éxito!")
            window.close()
            ventanaRegistro = None
            ventanaLogin = crearVentanaLogin()
        else:
            sg.Popup("\n".join(lista_errores),
                     title="Error en el registro.")
        
        
        
        