---
#Gestión de Créditos

Aplicación web en Flask y SQLite que permite registrar, consultar, editar y eliminar créditos.

---

## Backend

* [Python 3.8+](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/installation/) (gestor de paquetes de Python)
* SQLite3 

### Dependencias de Python
Instalables con `pip install -r requirements.txt`:

* Flask

---

##  Frontend

Estas librerías se cargan automáticamente desde CDN en el `index.html`:

* **Bootstrap 5**: Estilos y componentes.
* **Chart.js**: Gráficos

---

Instalación y ejecución

1. **Clonar el repositorio**

   ```bash
   git clone https://github.com/tu-usuario/gestion-creditos.git
   cd gestion-creditos
   ```

2. **Crear un entorno virtual (opcional pero recomendado)**

   ```bash
   python -m venv venv
   source venv/bin/activate    # Linux / Mac
   venv\Scripts\activate       # Windows
   ```

3. **Instalar dependencias**

   ```bash
   pip install -r requirements.txt
   ```

   > Si no tienes un `requirements.txt`, créalo con:
   >
   > ```bash
   > pip freeze > requirements.txt
   > ```

4. **Ejecutar la aplicación**

   ```bash
   python app.py
   ```

   Por defecto se abrirá en:
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

##Estructura del proyecto

```
/proyecto
 ┣ app.py               # Backend Flask (API + frontend)
 ┣ creditos.db          # Base de datos SQLite (se crea automáticamente)
 ┣ templates/
 ┃ ┗ index.html         # Frontend con Bootstrap + JS
 ┣ static/              # Archivos estáticos (si agregas CSS/JS extra)
 ┗ requirements.txt     # Dependencias de Python
```

---

##  Endpoints principales (API REST)

* `GET /api/creditos` → Lista todos los créditos
* `POST /api/creditos` → Crea un nuevo crédito
* `PUT /api/creditos/<id>` → Actualiza un crédito existente
* `DELETE /api/creditos/<id>` → Elimina un crédito

Formato de JSON esperado en `POST` y `PUT`:

```json
{
  "cliente": "Juan Pérez",
  "monto": 10000,
  "tasa_interes": 5.5,
  "plazo": 12,
  "fecha_otorgamiento": "2025-09-01"
}
```

---

##  Funcionalidades del frontend

* Registro de nuevos créditos mediante formulario.
* Listado dinámico en tabla con botones **Editar** y **Eliminar**.
* Modal para editar créditos.
* Gráfico de pastel mostrando la **distribución de créditos por cliente** (con Chart.js).

---

##  Tecnologías usadas

* **Backend**: Flask (Python) + SQLite
* **Frontend**: Bootstrap 5 + Chart.js + Fetch API
* **Base de datos**: SQLite (archivo local `creditos.db`)

---

##  Nota

* La base de datos se crea automáticamente al iniciar el proyecto.


---



