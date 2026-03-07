#!/bin/bash

# Preguntar al usuario durante cuanto tiempo debe ejecutarse la captura de datos MQTT
echo "Introduce el tiempo de captura en segundos (default= 10 secs):"
read CAPTURE_TIME

# Si el usuario no ingresa nada, use un valor predeterminado (10 segundos)
if [ -z "$CAPTURE_TIME" ]; then 
	CAPTURE_TIME=10
fi

# Archivo donde se almacenara la salida MQTT
LOG_FILE="mqtt_capture.log"

echo "[1/4] Ejecutando MQTT.."

# Toda la salida (stdout y stderr) se redirige al archivo de registro
./Ejecutables/mqtt_subscribe_emqx_linux > "$LOG_FILE" 2>&1 & 
PID=$!

echo " Proceso iniciado correctamnte con PID: $PID"

#Contador de  segundos para seguir cuantos segundos han pasado
SECONDS_PASSED=0


while kill -0 $PID 2>/dev/null && [ $SECONDS_PASSED -lt $CAPTURE_TIME ]; do
	sleep 1
	SECONDS_PASSED=$((SECONDS_PASSED +1))
done

# Si el proceso sigue ejecutandose después del limite de tiempo
if kill -0 $PID 2>/dev/null; then
	echo "[2/4] Tiempo maximo alcanzado. finalizando proceso.."

# Primero intente una parada suave usando SIGINT
	kill -SIGINT $PID
	sleep 2

# si el proceso no se detiene, intente SIGTERM
	if kill -0 $PID 2>/dev/null; then
		echo "Enviando SIGTERM.."	
		kill -SIGTERM $PID
		sleep 2
	fi

# Si aun se niega a detenerse, fuerza la muerte con SIGKILL
	if kill -0 $PID 2>/dev/null; then
		echo "forzando cierre con SIGKILL"
		kill -SIGKILL $PID
	fi
fi

# Espere hasta que el proceso finalice
wait $PID 2>/dev/null
echo "[3/4] Ejecutando ejemplo python dentro de bash"  

# Ejemplo de ejecucion de codigo Python dentro del script Bash
python3 - <<'PY'
print("Hola mundo desde python ejecutado dentro de bash")
PY

# Ejecute el script de Python que analiza los datos MQTT capturados
echo "[4/4] Ejecutando analisis en Python.."
python3 plots_mqtt.py "$LOG_FILE"

echo "Proceso finalizado correctamente"
