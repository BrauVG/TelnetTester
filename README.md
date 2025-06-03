# tester masivo de puertos

Herramienta simple en Python para verificar la conectividad a múltiples direcciones IP y puertos especificados por el usuario.

## Descripción

Este script permite ingresar varias direcciones IP y puertos para probar si es posible establecer una conexión TCP con cada combinación. Es útil para administradores de red, desarrolladores y testers que necesitan validar accesos a servicios distribuidos.

## Ejemplo de uso

Pega las direcciones IP (una por línea). Cuando termines, presiona Enter dos veces:
192.168.1.1
8.8.8.8

Introduce los puertos separados por coma (ej. 8888,5432,5985): 80,53

🔎 Iniciando pruebas de conexión...

Probando 192.168.1.1:80... Falló
Probando 192.168.1.1:53... Falló
----------------------------------------
Probando 8.8.8.8:80... Falló
Probando 8.8.8.8:53... OK
----------------------------------------

## Requisitos

- Python 3.x

## Uso

1. Clona el repositorio o descarga el archivo.
2. Ejecuta el script con Python:
   ```bash
   python ip_port_connection_tester.py
