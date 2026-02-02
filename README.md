# CRUD de Usuarios + Prueba Controlada de Fuerza Bruta (FastAPI)

##  Descripción
Este proyecto implementa una **API REST con FastAPI** que permite realizar operaciones CRUD sobre usuarios y ejecutar **una prueba controlada de fuerza bruta contra la propia API**, únicamente con fines educativos.

 **Advertencia ética**  
La prueba de fuerza bruta se realiza **exclusivamente sobre esta API en entorno local/laboratorio**, usando usuarios creados para la práctica. **Nunca debe ejecutarse contra sistemas reales o sin autorización.**

---

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
