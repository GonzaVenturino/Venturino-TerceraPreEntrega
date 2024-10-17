# Proyecto Django con MVT

## Requisitos
- Python 3.x
- Django 4.x

## Instrucciones para correr el proyecto
1. Clonar el repositorio de GitHub:
   ```bash
   git clone https://github.com/GonzaVenturino/Venturino-TerceraPreEntrega.git
   cd proyecto
   ```

2. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecutar las migraciones y correr el servidor:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## Funcionalidades principales
- **Agregar Producto:** Navegar a `/agregar/` para insertar un nuevo producto.
- **Listar Productos:** Ver todos los productos en `/productos/`.
- **Buscar Producto:** Buscar productos por nombre en `/buscar/`.
