import nmap
import sys
import concurrent.futures
import threading

# Variable global para controlar el modo verbose
verbose = True

# Logo de MAFIA
def mostrar_logo():
    print("""
███╗░░░███╗░█████╗░███████╗██╗░█████╗░
████╗░████║██╔══██╗██╔════╝██║██╔══██╗
██╔████╔██║███████║█████╗░░██║███████║
██║╚██╔╝██║██╔══██║██╔══╝░░██║██╔══██║
██║░╚═╝░██║██║░░██║██║░░░░░██║██║░░██║
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝
    """)

# Función de impresión en modo verbose
def print_verbose(message):
    if verbose:
        print(f"[VERBOSE] {message}")

# Función para realizar escaneo de ping y encontrar hosts activos
def escanear_hosts_activos(red):
    nm = nmap.PortScanner()
    print_verbose(f"Escaneando hosts activos en la red {red}...")
    try:
        nm.scan(hosts=red, arguments='-sn')
        hosts_activos = [host for host in nm.all_hosts() if nm[host].state() == 'up']
        print_verbose(f"Hosts activos encontrados: {len(hosts_activos)}")
        return hosts_activos
    except Exception as e:
        print(f"[ERROR] No se pudo realizar el escaneo de hosts activos: {e}")
        sys.exit(1)

# Función para realizar escaneo detallado de puertos y servicios en un host
def escanear_servicios(host):
    nm = nmap.PortScanner()
    print_verbose(f"Iniciando escaneo detallado en el host {host}")
    try:
        nm.scan(host, arguments='-sC -sV -O -Pn')
        info_host = {
            'host': host,
            'estado': nm[host].state(),
            'sistema_operativo': nm[host]['osmatch'][0]['name'] if 'osmatch' in nm[host] and nm[host]['osmatch'] else "No detectado",
            'puertos': []
        }
        
        for proto in nm[host].all_protocols():
            for port in nm[host][proto].keys():
                puerto_info = nm[host][proto][port]
                servicio = {
                    'puerto': port,
                    'estado': puerto_info['state'],
                    'servicio': puerto_info['name'],
                    'version': puerto_info['version'] if 'version' in puerto_info else "No detectado"
                }
                info_host['puertos'].append(servicio)
        
        print_verbose(f"Escaneo de {host} completado.")
        return info_host
    except Exception as e:
        print(f"[ERROR] No se pudo realizar el escaneo detallado en {host}: {e}")
        return None

# Función para generar el reporte en archivo
def generar_reporte(resultados, nombre_archivo="reporte_escaner.txt"):
    try:
        with open(nombre_archivo, 'w') as f:
            f.write("===== Reporte de Escaneo =====\n")
            for info_host in resultados:
                f.write(f"\nHost: {info_host['host']}\n")
                f.write(f"Estado: {info_host['estado']}\n")
                f.write(f"Sistema Operativo: {info_host['sistema_operativo']}\n")
                f.write("Puertos:\n")
                for puerto in info_host['puertos']:
                    f.write(f"  - Puerto: {puerto['puerto']}\n")
                    f.write(f"    Estado: {puerto['estado']}\n")
                    f.write(f"    Servicio: {puerto['servicio']}\n")
                    f.write(f"    Versión: {puerto['version']}\n")
            f.write("\nProceso de análisis completado exitosamente.\n")
        print(f"\n[+] Reporte generado exitosamente en {nombre_archivo}")
    except Exception as e:
        print(f"[ERROR] No se pudo generar el reporte: {e}")

# Función principal para el escaneo usando hilos
def main():
    mostrar_logo()
    red = input("Ingrese la dirección de red (ejemplo: 192.168.1.0/24): ")
    
    # Escaneo de hosts activos
    hosts_activos = escanear_hosts_activos(red)
    if not hosts_activos:
        print("[*] No se encontraron hosts activos.")
        sys.exit(0)
    
    # Lista para almacenar los resultados de cada host
    resultados = []
    
    # Utilizamos hilos para escanear cada host activo en paralelo
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Ejecutamos escanear_servicios en cada host activo usando hilos
        futures = {executor.submit(escanear_servicios, host): host for host in hosts_activos}
        
        for future in concurrent.futures.as_completed(futures):
            host = futures[future]
            try:
                info_host = future.result()
                if info_host:
                    resultados.append(info_host)
            except Exception as e:
                print(f"[ERROR] No se pudo obtener el resultado del host {host}: {e}")
    
    # Generación del reporte final
    generar_reporte(resultados)

if __name__ == "__main__":
    main()
