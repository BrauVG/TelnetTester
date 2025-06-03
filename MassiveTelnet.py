import socket

def cargar_ips():
    print("Pega las direcciones IP (una por línea). Cuando termines, presiona Enter dos veces:")
    ips = []
    while True:
        linea = input()
        if not linea.strip():
            break
        ips.append(linea.strip())
    return ips

def cargar_puertos():
    puertos = input("Introduce los puertos separados por coma (ej. 8888,5432,5985): ")
    return [int(p.strip()) for p in puertos.split(",") if p.strip().isdigit()]

def probar_conexion(ip, puerto, timeout=2):
    try:
        with socket.create_connection((ip, puerto), timeout=timeout):
            return True
    except Exception:
        return False

def main():
    ips = cargar_ips()
    puertos = cargar_puertos()

    print("\n🔎 Iniciando pruebas de conexión...\n")

    for ip in ips:
        for puerto in puertos:
            resultado = "OK" if probar_conexion(ip, puerto) else "Falló"
            print(f"Probando {ip}:{puerto}...{resultado}")
        print("-" * 40)

if __name__ == "__main__":
    main()
