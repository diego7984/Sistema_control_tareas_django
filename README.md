# Sistema de Control de Tareas

Proyecto backend desarrollado con Python, Django, Django REST Framework y MySQL.

## Descripción

El Sistema de Control de Tareas es una aplicación backend creada para organizar y gestionar tareas.

El proyecto cuenta con una API REST que permite administrar usuarios, categorías y tareas mediante operaciones CRUD. La información se almacena en una base de datos MySQL y las credenciales de conexión se administran mediante variables de entorno.

## Tecnologías utilizadas

- Python
- Django
- Django REST Framework
- MySQL
- mysqlclient
- python-decouple
- Git y GitHub

## Modelos

El sistema cuenta con los siguientes modelos:

### Usuario

- nombre
- correo

### Categoria

- nombre
- descripcion

### Tarea

- titulo
- descripcion
- fecha_creacion
- fecha_limite
- completada
- usuario
- categoria

El modelo Tarea se relaciona con Usuario y Categoria mediante claves foráneas.

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/diego7984/Sistema_control_tareas_django.git
```

### 2. Entrar a la carpeta del proyecto

```bash
cd Sistema_control_tareas_django
```

### 3. Crear el ambiente virtual

```bash
python -m venv ambiente
```

### 4. Activar el ambiente virtual en Windows

```bash
ambiente\Scripts\activate
```

### 5. Instalar las dependencias

```bash
pip install -r requirements.txt
```

## Configuración de variables de entorno

Crear un archivo `.env` en la raíz del proyecto.

Se puede utilizar `.env.example` como referencia.

Ejemplo:

```env
SECRET_KEY=tu_secret_key

DB_NAME=control_tareas_db
DB_USER=usuario_tareas
DB_PASSWORD=tu_password
DB_HOST=localhost
DB_PORT=3306
```

El archivo `.env` no debe subirse al repositorio porque contiene información sensible.

## Base de datos

El proyecto utiliza MySQL.

El script para crear la base de datos, el usuario y asignar los permisos se encuentra en:

```text
scripts/crear_base_datos.sql
```

Antes de ejecutar el proyecto se debe crear y configurar la base de datos.

## Migraciones

Aplicar las migraciones con:

```bash
python manage.py migrate
```

Para comprobar las migraciones:

```bash
python manage.py showmigrations
```

## Ejecutar el proyecto

Iniciar el servidor con:

```bash
python manage.py runserver
```

Abrir en el navegador:

```text
http://127.0.0.1:8000/
```

## API REST

La raíz de la API se encuentra en:

```text
http://127.0.0.1:8000/api/
```

Endpoints disponibles:

```text
/api/usuarios/
/api/categorias/
/api/tareas/
```

## Operaciones CRUD

La API permite realizar las siguientes operaciones:

- GET: consultar registros.
- POST: crear registros.
- PUT: actualizar completamente un registro.
- PATCH: actualizar parcialmente un registro.
- DELETE: eliminar un registro.

Estas operaciones son gestionadas mediante `ModelViewSet` de Django REST Framework.

## Ejemplos

### Crear usuario

```json
{
    "nombre": "Diego Neumann",
    "correo": "diego@ejemplo.cl"
}
```

### Crear categoría

```json
{
    "nombre": "Estudios",
    "descripcion": "Tareas relacionadas con estudios"
}
```

### Crear tarea

```json
{
    "titulo": "Estudiar Backend",
    "descripcion": "Preparar evaluación de Django REST Framework",
    "fecha_limite": "2026-10-10",
    "completada": false,
    "usuario": 1,
    "categoria": 1
}
```

## Funcionalidades

- Proyecto Django configurado.
- Aplicación `tareas`.
- Página de bienvenida.
- Página personalizada de error 404.
- Base de datos MySQL.
- Modelos Usuario, Categoria y Tarea.
- Relaciones mediante claves foráneas.
- Serialización mediante Django REST Framework.
- API REST.
- Rutas generadas mediante Router.
- CRUD completo.
- Variables de entorno mediante `.env`.
- Script SQL para creación y configuración de la base de datos.
- Control de versiones mediante Git y GitHub.