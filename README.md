# CRUD de Usuarios + Prueba Controlada de Fuerza Bruta (FastAPI)

##  Descripción
Este proyecto implementa una **API REST con FastAPI** que permite realizar operaciones CRUD sobre usuarios y ejecutar **una prueba controlada de fuerza bruta contra la propia API**, únicamente con fines educativos.

 **Advertencia ética**  
La prueba de fuerza bruta se realiza **exclusivamente sobre esta API en entorno local/laboratorio**, usando usuarios creados para la práctica. **Nunca debe ejecutarse contra sistemas reales o sin autorización.**

---
## Pasos par la ejecucion de la Api 

1.usando el comando: git clone clonamos mi repositorio de github. 
2.creamos una interfaz virtual para tener un entorno seguro en el cual ejecutar nustras pruebas:
- python -m venv venv
- .\venv\Scripts\activate
3.ya en nuestra interfaz virtual(venv) ejecutamos el comando fastapi dev
4.Ejecutada la Fastapi debemos encotrar en nuestra terminal la siguientes lineas:
  <img width="747" height="178" alt="image" src="https://github.com/user-attachments/assets/674a4dbb-2da2-47b9-9ef2-22a20f56207b" />
  Entraremos al la documentacion atravez de la URL con terminacion en DOCS
5.Deberiamos encontrar nuestra fastapi asi :

  <img width="1866" height="822" alt="image" src="https://github.com/user-attachments/assets/f1f30702-8899-44fa-8d62-286d4a831c82" />


  

##  Objetivos
- Implementar endpoints CRUD seguros para usuarios.
- Comprender cómo un ataque de fuerza bruta explota credenciales débiles.
- Medir tiempo, número de intentos y efectos del ataque.
- Analizar vulnerabilidades y proponer mitigaciones.

---

## Tecnologías usadas
- **Python 3.10+**
- **FastAPI**
- **Requests** (para el script de ataque)

---

## Modelo User
El modelo de usuario contiene los siguientes campos:

<img width="412" height="206" alt="image" src="https://github.com/user-attachments/assets/7358b917-bcf3-48ee-90cf-013f78ee2c7a" />


---

##  Endpoints disponibles

### Usuarios (CRUD)
<img width="544" height="557" alt="image" src="https://github.com/user-attachments/assets/4ea2c8ec-058c-4e1f-8625-1515c84a9b33" />
<img width="473" height="111" alt="image" src="https://github.com/user-attachments/assets/d4ac7659-6553-4886-8760-ca094d9bc8e9" />

### Autenticación

<img width="812" height="129" alt="image" src="https://github.com/user-attachments/assets/11274980-6810-43f7-85ce-5c632a27634c" />

---

## RESULTADOS: 

<img width="535" height="114" alt="image" src="https://github.com/user-attachments/assets/bfa3141c-ce90-401d-b843-83ef7194ff30" />

## Conclusión:

La prueba controlada de fuerza bruta realizada contra la API propia demuestra de forma práctica y contundente la vulnerabilidad de un sistema de autenticación cuando no existen mecanismos de protección. Tal como se observa en la ejecución mostrada en la imagen, el ataque logró descubrir la contraseña correcta del usuario “Juan” tras 65 450 intentos, empleando un tiempo total aproximado de 984,5 segundos.
