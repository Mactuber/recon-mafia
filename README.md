/*MAFIA - Herramienta de Reconocimiento de Infraestructura*/

MAFIA es una herramienta de reconocimiento de infraestructura escrita en Python que permite escanear redes y detectar hosts activos, sistemas operativos, puertos y servicios abiertos o filtrados, así como las versiones de los mismos. Basada en nmap, esta herramienta facilita la identificación de dispositivos en una red, proporcionando un reporte detallado y automatizado. Además, el script permite escanear en paralelo gracias al uso de hilos, y ofrece un modo verbose para un seguimiento detallado de cada paso.

Características:
Escaneo de hosts activos: Identifica dispositivos activos en una red dada.
Detección de puertos y servicios: Escanea puertos abiertos/filtrados y detecta servicios en ejecución.
Identificación del sistema operativo: Identifica posibles sistemas operativos en los hosts escaneados.
Multihilo: Utiliza hilos para realizar escaneos en paralelo, maximizando la eficiencia.
Modo Verbose: Opción para seguimiento detallado del progreso y estado de cada escaneo.
Generación de reportes: Crea un archivo .txt con un resumen completo del análisis.
Requisitos
Para utilizar MAFIA, necesitas:

Python 3.7 o superior.
Nmap instalado en el sistema:
bash
Copiar código
sudo apt install nmap
Paquete python-nmap para interactuar con Nmap desde Python.
Instalación
Clonar el Repositorio:

bash
Copiar código
git clone https://github.com/tuusuario/mafia.git
cd mafia
Crear un Entorno Virtual (opcional, pero recomendado):

bash
Copiar código
python3 -m venv venv
source venv/bin/activate  # Para activar el entorno en Linux/macOS
Instalar las Dependencias: Con el entorno virtual activado (o directamente si decides no usar uno), instala las dependencias:

bash
Copiar código
pip install -r requirements.txt
Uso
Ejecución Básica
Para comenzar un escaneo en una red específica, ejecuta:

bash
Copiar código
python3 mafia.py
El script mostrará un logo de bienvenida y pedirá la dirección de red en formato CIDR. Ejemplo:

plaintext
Copiar código
Ingrese la dirección de red (ejemplo: 192.168.1.0/24): 192.168.1.0/24
Parámetros de Salida
El script generará un reporte en reporte_escaner.txt con la siguiente información:

Host: IP del host.
Estado: Estado general del host.
Sistema Operativo: Sistema operativo identificado (si es posible).
Puertos: Listado de puertos abiertos/filtrados y servicios, incluyendo versión.
Ejemplo de Escaneo
Escaneo de Red Local: Para identificar los dispositivos en tu red local, ingresa el rango IP de tu red. Por ejemplo, si tu red local está en 192.168.1.0/24:

plaintext
Copiar código
Ingrese la dirección de red (ejemplo: 192.168.1.0/24): 192.168.1.0/24
El reporte generará información detallada de cada host activo en esa red.

Escaneo en Redes más Amplias: Puedes usar rangos mayores (por ejemplo, 10.0.0.0/16) para escanear redes corporativas, aunque esto puede aumentar significativamente el tiempo de escaneo. Nota: Ejecutar el escaneo en redes amplias puede ser intensivo en recursos.

Ejemplo de Reporte Generado
El archivo reporte_escaner.txt incluirá una salida como esta:

plaintext
Copiar código
===== Reporte de Escaneo =====

Host: 192.168.1.1
Estado: up
Sistema Operativo: Linux 3.x
Puertos:
  - Puerto: 80
    Estado: open
    Servicio: http
    Versión: Apache httpd 2.4.41
  - Puerto: 22
    Estado: open
    Servicio: ssh
    Versión: OpenSSH 7.6p1

Host: 192.168.1.2
Estado: up
Sistema Operativo: No detectado
Puertos:
  - Puerto: 443
    Estado: open
    Servicio: https
    Versión: nginx 1.18.0
    
Modo Verbose
Para monitorear el progreso de cada escaneo, el script imprime mensajes en tiempo real si el modo verbose está activado. Puedes cambiar el valor de la variable verbose en el código para desactivar esta opción si prefieres una salida menos detallada.

Notas de Seguridad
Uso Ético: Esta herramienta debe usarse con autorización en redes bajo tu control. No está permitido utilizarla para realizar escaneos en redes sin permiso, ya que esto podría infringir las leyes locales.
Recursos del Sistema: En redes grandes, el escaneo multihilo puede consumir muchos recursos de red y CPU. Ajusta el rango de IP y el uso de hilos de acuerdo a la capacidad de tu red y sistema.
Contribuciones
Las contribuciones son bienvenidas. Puedes enviar un pull request para mejorar la funcionalidad o solucionar problemas. Asegúrate de seguir las buenas prácticas y documentar cualquier cambio importante.

¡Gracias por usar MAFIA!
