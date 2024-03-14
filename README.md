# ruta-critica-solver
Script para resolver problemas de ruta critica de Organizacion 3

# Requerimientos para instalar

- python3
- pip
- virtualenv

# Pasos para instalar dependencias del proyecto

1. Crear entorno virtualenv
    
    ```bash
    python -m venv .venv
    ```

2. Entrar en el entorno virtualenv

    - En linux ( o gitbash ) ubicarnos en el directorio raiz del proyecto y correr el siguiente comando:

      ```bash
      source .venv/bin/activate 
      ```

    - En windows ubicarnos en el directorio raiz del proyecto y correr el siguiente comando:

      ```powershell
      .venv\Scripts\activate
      ```

3. Instalar las dependencias con pip ( igual para Linux o Windows )

    ```bash
    pip install -r requirements.txt
    ```

# Pasos para correr el script ( es igual para Linux o para Windows )

1. Entrar en el entorno virtualenv ( ver paso 2 de guia de instalacion )
2. ./rutaCritica.py

# Como usar el script

1. Para usar correctamente el script y obtener la tabla con los valores calculados y las rutas criticas es necesario que el CSV tenga completas las siguientes columnas:

    * Tareas: Los nombres de las tareas.

    * Duraciones: Las duraciones de las tareas ( todas en una misma unidad de medida, dias, semanas, etc.)

    * Dependencias: Una lista separada por comas de los nombres separados por comas de las dependencias de cada tarea.
2. Se ejecuta el script y se obtiene la tabla en formato CSV con todos los valores calculados

# Resultados de la ejecucion del script
Se obtiene un archivo CSV con las siguientes columnas calculadas:
    
    * ES: "Earliest Start" o inicio mas temprano, es la fecha mas temprana en la que la tarea correspondiente puede empezar

    * EF: "Earliest Finish" o finalizacion mas temprana, es la fecha mas temprana en la que la tarea correspondiente puede finalizar

    * LS: "Latest Start" o inicio mas tardio, es la fecha mas tardia con la que la tarea puede empezar.

    * LF: "Latest Finish" o finalizacion mas tardia, es la fecha mas tardia con la que la tarea puede finaizar.
