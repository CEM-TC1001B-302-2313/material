# match - case
variable = 10
match variable:
    case 5:
        print("Cinco...")
    case 10:
        print("Diez...")
    case "Uno":
        print("Texto uno...")
    case _:
        print("Caso por default...")