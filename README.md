# MAFIA - Herramienta de Reconocimiento de Infraestructura

**MAFIA** es una herramienta de reconocimiento de infraestructura escrita en Python que permite escanear redes y detectar hosts activos, sistemas operativos, puertos y servicios abiertos o filtrados, así como las versiones de los mismos. Basada en `nmap`, esta herramienta facilita la identificación de dispositivos en una red, proporcionando un reporte detallado y automatizado. Además, el script permite escanear en paralelo gracias al uso de hilos y ofrece un modo `verbose` para un seguimiento detallado de cada paso.

## Características

- **Escaneo de hosts activos**: Identifica dispositivos activos en una red dada.
- **Detección de puertos y servicios**: Escanea puertos abiertos/filtrados y detecta servicios en ejecución.
- **Identificación del sistema operativo**: Identifica posibles sistemas operativos en los hosts escaneados.
- **Multihilo**: Utiliza hilos para realizar escaneos en paralelo, maximizando la eficiencia.
- **Modo Verbose**: Opción para seguimiento detallado del progreso y estado de cada escaneo.
- **Generación de reportes**: Crea un archivo `.txt` con un resumen completo del análisis.

## Requisitos

Para utilizar **MAFIA**, necesitas:

1. **Python 3.7 o superior**.
2. **Nmap** instalado en el sistema:
   ```bash
   sudo apt install nmap

## INSTALACIÓN
Clonar el Repositorio:
git clone https://github.com/tuusuario/mafia.git
cd mafia

Crear un Entorno Virtual (opcional, pero recomendado):
python3 -m venv venv
source venv/bin/activate  # Para activar el entorno en Linux/macOS

Instalar las Dependencias: Con el entorno virtual activado (o directamente si decides no usar uno), instala las dependencias:
pip install -r requirements.txt

## EJECUCIÓN BÁSICA
python3 mafia.py
Ingrese la dirección de red (ejemplo: 192.168.1.0/24): 192.168.1.0/24

## Parámetros de Salida
El script generará un reporte en reporte_escaner.txt con la siguiente información:

Host: IP del host.
Estado: Estado general del host.
Sistema Operativo: Sistema operativo identificado (si es posible).
Puertos: Listado de puertos abiertos/filtrados y servicios, incluyendo versión.


