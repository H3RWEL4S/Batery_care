#Es importante instalar la librería
#pip install win10toast
import win10toast 
import time
#pip install wmi
import wmi

# Batería completamente cargada al 100%
porcentaje_carga_completa = 100

# Inicializar la biblioteca win10toast
toaster = win10toast.ToastNotifier()

# Define la función para obtener el porcentaje de la batería
def get_battery_percentage():
  # Obtener la instancia de la clase Win32_Battery
  battery = wmi.WMI().Win32_Battery()

  # Obtener el porcentaje de carga actual
  porcentaje_carga = battery[0].BatteryStatus
  
  # Convertir el valor a un número entero
  porcentaje_carga_int = int(porcentaje_carga)

  # Devolver el porcentaje de carga
  return porcentaje_carga_int

while True:
    # Obtener el porcentaje actual de carga de la batería
    porcentaje_carga_actual = get_battery_percentage()
    # Función para obtener el porcentaje de batería

    # Si la batería está completamente cargada
    if porcentaje_carga_actual >= porcentaje_carga_completa:
        # Mostrar la notificación
        toaster.show_toast(
            "¡Batería cargada al 100%!",
            "Desconecte el cargador para evitar daños a la batería.",
            icon_path=None,
            duration=10  # Duración de la notificación en segundos
        )

        # Esperar un minuto antes de volver a comprobar la carga
        time.sleep(60)

    # Si la batería no está completamente cargada, seguir comprobando cada 5 segundos
    else:
        time.sleep(5)
