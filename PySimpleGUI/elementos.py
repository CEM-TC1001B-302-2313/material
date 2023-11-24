import PySimpleGUI as sg

sg.theme("DarkRed1")
sg.set_options(font="Arial 18")

def crearVentanaPrincipal():
    listado_oficinas = [
        "Atizapán de Zaragoza",
        "Cuautitlán Izcalli",
        "Nicolás Romero",
        "Naucalpan de Juarez",
        "Tlalnepantla de Baz"
        ]
    listado_calificaciones = [
        "Mala",
        "Regular",
        "Buena"
        ]
    layout = [
        # Text
        [sg.Text("Mi primer texto",
                 font="Arial 30",
                 text_color="blue",
                 background_color="pink")],
        # Button
        [sg.Button("Soy un botón",
                   key="botón 1",
                   image_filename="gato.png"),
         sg.Button("Soy otro botón",
                   key="botón 2")],
        # Input
        [sg.Text("Usuario"),
         sg.Input(key="input usuario")],
        [sg.Text("Contraseña"),
         sg.Input(key="input contraseña",
                  password_char="*")],
        # Checkbox
        [sg.Text("Comida que te gusta"),
         sg.Checkbox("Tacos", key="check tacos"),
         sg.Checkbox("Chilaquiles", key="check chilaquiles"),
         sg.Checkbox("Pasta", key="check pasta")],
        # Radio
        [sg.Text("¿Eres mayor de edad?"),
         sg.Radio("Sí",
                  key="radio mayor sí",
                  group_id="grupo mayor edad",
                  enable_events=True),
         sg.Radio("No",
                  key="radio mayor no",
                  group_id="grupo mayor edad",
                  default=True,
                  enable_events=True)],
        # Combo
        [sg.Text("Selecciona tu oficina del INE"),
         sg.Combo(listado_oficinas,
                  key="combo oficinas",
                  default_value="Atizapán de Zaragoza",
                  disabled=True,
                  readonly=True)],
        # Slider
        [sg.Text("Cantidad de hijos"),
         sg.Slider(range=(0,10),
                   key="slider hijos",
                   default_value=5,
                   orientation="horizontal")],
        # Spin
        [sg.Text("¿Cómo calificarías tu experiencia?"),
         sg.Spin(listado_calificaciones,
                 key="spin calificaciones",
                 initial_value="Regular",
                 readonly=True)],
        # Image
        [sg.Image("gato.png")]
        ]
    return sg.Window("Mi primera ventana", layout, finalize=True)

ventanaPrincipal = crearVentanaPrincipal()

while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WINDOW_CLOSED:
        window.close()
        break
    elif event == "botón 1":
        print("Click en botón 1...")
    elif event == "botón 2":
        usuario = values["input usuario"]
        contraseña = values["input contraseña"]
        print(f"Usuario: {usuario}")
        print(f"Contraseña: {contraseña}")
        if values["check tacos"]:
            print("Me gustan los tacos")
        if values["check chilaquiles"]:
            print("Me gustan los chilaquiles")
        if values["check pasta"]:
            print("Me gusta la pasta")
        if values["radio mayor sí"]:
            print("Soy mayor de edad")
        else:
            print("Soy menor de edad")
    elif event == "radio mayor sí":
        window["combo oficinas"].update(disabled=False)
    elif event == "radio mayor no":
        window["combo oficinas"].update(disabled=True)