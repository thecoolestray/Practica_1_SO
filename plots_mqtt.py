import json
import os
import matplotlib.pyplot as plt

#Archivo generado por el script Bash
log_file = "mqtt_capture.log"
#Altura de grafica ASCII
ALTURA_GRAFICA = 20

#lee el archivo log
def leer_log_file():

    lineas = []

    try:
        with open(log_file, "r") as f:
            for linea in f:
                lineas.append(linea)

    except FileNotFoundError:
        print("Log file no encontrado")

    return lineas

#extraer todos los valores numericos de los mensajes JSON
def extraer_values(lineas):

    values = []

    for linea in lineas:

        if "Payload:" in linea:

            text_json = linea.split("Payload:", 1)[1].strip()

            try:
                #convertir el texto JSON en un diccionario de python
                data = json.loads(text_json)

                for value in data.values():

                    if isinstance(value, (int, float)):
                        values.append(value)

            except json.JSONDecodeError:
                pass

    return values

#Generar un grafica PNG utilizando matplotlib
def crear_PNG(values):
    #se crea la carpeta plots si no existe
    os.makedirs("plots", exist_ok=True)

    plt.plot(values)
    plt.grid()
    plt.title("datos del sensor")
    plt.xlabel("indice")
    plt.ylabel("Value")
    plt.savefig("plots/data.png")
    plt.close()

    print("PNG grafica guardada")

#generar una grafica ASCII en la terminal
def grafica_ASCII(values):

    if len(values) == 0:
        print("no hay datos para monstrar")
        return

    max_value = int(max(values))
    #Ancho d ela grafica 
    ancho = len(values)

    scaled_values = []

    for v in values:

        level = int((v/max_value) * ALTURA_GRAFICA)
        scaled_values.append(level)

    print("\n Grafica ASCII \n")
    #dibujar la grafica de arriba hacia abajo
    for y in range(ALTURA_GRAFICA, -1, -1):

        linea = ""
        #eje y
        if y == ALTURA_GRAFICA:
            linea += f"{max_value:>3} |"
        elif y == 0:
            linea += " 1 |"
        else:
            linea += "   |" 
         
        for x in range(ancho):
            if scaled_values[x] == y:
                linea += " * "
            else:
                linea += "   "
        
    print(linea)
    print("  +" + "---" * ancho)

    linea_form = "    "
    #Eje x
    for i in range(ancho):
        linea_form += f"{i:>3}"
    print(linea_form)

    print("\n ultimos valores:", values)    

#funcion principal del programa 
def main():

    lineas = leer_log_file()

    values = extraer_values(lineas)

    crear_PNG(values)

    grafica_ASCII(values)


if __name__ == "__main__":
    main()
