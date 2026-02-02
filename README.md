# CRUD de Usuarios + Prueba Controlada de Fuerza Bruta (FastAPI)

##  Descripción
Este proyecto implementa una **API REST con FastAPI** que permite realizar operaciones CRUD sobre usuarios y ejecutar **una prueba controlada de fuerza bruta contra la propia API**, únicamente con fines educativos.

 **Advertencia ética**  
La prueba de fuerza bruta se realiza **exclusivamente sobre esta API en entorno local/laboratorio**, usando usuarios creados para la práctica. **Nunca debe ejecutarse contra sistemas reales o sin autorización.**

---

##  Ejecución del Proyecto (Paso a Paso)

### 1️. Clonar el repositorio
Primero clonamos el repositorio desde GitHub utilizando el comando:

```bash
git clone https://github.com/mateovivas453-dot/First-term-exam-Practical.git
```
Entramos a la carpeta:
```bash
cd .\First-term-exam-Practical\

```

### 2. Crear un entorno virtual (venv)

Creamos una interfaz virtual para trabajar en un entorno aislado y seguro:

```bash

python -m venv venv

```

### - Activamos el entorno virtual:

```bash

.\venv\Scripts\activate


```
### Si todo salió bien, en la terminal debería aparecer algo como:

<img width="484" height="56" alt="image" src="https://github.com/user-attachments/assets/ba7af876-bd61-410c-9fb8-4f6837e5aa93" />

### 3. Ejecutar la API con FastAPI

Instalamos los requirements.txt

bash

```

pip install -r .\requirements.txt


```



### 4. Ejecutar la API con FastAPI

Una vez dentro del entorno virtual, ejecutamos la aplicación (Fast api)
```bash


fastapi dev


```
### 5. Veridicacion 

Si la ejecucion fue correcta tenemos que ver la sigueintes lineas en nuestra terminal:
<img width="595" height="562" alt="image" src="https://github.com/user-attachments/assets/a44ea66f-15e3-415b-9e76-ef5d90860216" />

### 5. Acceder a la documentación interactiva

Abrimos el navegador y accedemos a la documentación automática de FastAPI mediante la URL:

```bash



http://127.0.0.1:8000/docs


```

### 6. Interfaz de FastAPI

<img width="1863" height="827" alt="image" src="https://github.com/user-attachments/assets/ca3b4e1c-0fad-483f-92bf-8c633353b7cc" />



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
