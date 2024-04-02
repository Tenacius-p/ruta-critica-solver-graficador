# ruta-critica-solver
Script para resolver problemas de ruta critica de Organizacion 3

# Requerimientos para usar

- python3
- virtualenv
- PIL (pillow)

# Pasos para ejecutar el script

1. Clonar proyecto

    ```bash
    git clone https://github.com/epeat96/ruta-critica-solver.git
    ```
2. Ingresar al directorio del repositorio

    - En Linux o gitbash

    ```bash
    cd ruta-critica-solver
    ```

    - En Windows

    ```powershell
    dir ruta-critica-solver
    ```

3. Crear entorno virtualenv
    
    ```bash
    python -m venv .venv
    ```

4. Entrar en el entorno virtualenv

    - En Linux o gitbash ubicarnos en el directorio raiz del proyecto y correr el siguiente comando:

      ```bash
      source .venv/bin/activate 
      ```

    - En windows ubicarnos en el directorio raiz del proyecto y correr el siguiente comando:

      ```powershell
      .venv\Scripts\activate
      ```
5. Ejecutar el script
    ```bash
    ./rutaCritica.py
    ```

# Como usar el script

1. Para usar correctamente el script y obtener la tabla con los valores calculados y las rutas criticas es necesario que el CSV tenga datos en las siguientes columnas:

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

* Holgura: Es el resultado de la diferencia "LF - EF" y representa la cantidad de tiempo que una tarea puede retrasarse sin aumentar la duracion del proyecto.

* Rutas Criticas: En esta columna se pondran cadenas que representan la/las ruta/s critica/s del problema.
