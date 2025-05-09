import serial

# Configura el puerto serie y la velocidad (9600 baudios en este caso)
puerto = 'COM5'  # Para Linux o Mac, puede variar
# En Windows, el puerto podría ser algo como 'COM3'
velocidad = 9600

# Abre la conexión serial
ser = serial.Serial(puerto, velocidad)

print("Esperando datos...")

# Lee los datos desde el puerto serie
while True:
    if ser.in_waiting > 0:
        dato = ser.readline().decode('utf-8').strip()  # Lee y decodifica el dato
        print(f"Recibido: {dato}")
