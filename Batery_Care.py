#Es importante instalar la librería
#pip install win10toast
import win10toast 
import time

# Batería completamente cargada al 100%
porcentaje_carga_completa = 100

# Inicializar la biblioteca win10toast
toaster = win10toast.ToastNotifier()

while True:
    # Obtener el porcentaje actual de carga de la batería
    porcentaje_carga_actual = get_battery_percentage()
    # Función para obtener el porcentaje de batería (no implementada)

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