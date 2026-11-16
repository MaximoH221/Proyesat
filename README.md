# Proyesat 

Trabajo Práctico (Etapa 1 y 2). Paquete de módulos en Python para analizar datos de satélites usando la librería `skyfield`.

## Integrantes y división de tareas
* **Máximo Rodríguez:** Desarrollo del módulo `analisis.py` (métricas, conteos, ordenamiento, extremos y zonas).
* **Máximo Hansen:** Desarrollo de los módulos `catalogo.py` y `satelite.py` (lectura del JSON, categorización y clase principal).
* **Desarrollo conjunto:** Notebook de reporte final (`informe.ipynb`).

## Cómo correr el proyecto

1. Clonar este repositorio localmente y entrar a la carpeta del proyecto:
   ```bash
   git clone git clone https://github.com/MaximoH221/Proyesat.git
   cd Proyesat
   ```

2. Abrir la terminal y crear el entorno virtual:
   ```bash
   python -m venv .venv
   ```

3. Activar el entorno virtual según el sistema operativo:
   - **Windows (Git Bash):**
     ```bash
     source .venv/Scripts/activate
     ```
   - **Windows (PowerShell):**
     ```powershell
     .venv\Scripts\Activate.ps1
     ```
   - **Linux / macOS:**
     ```bash
     source .venv/bin/activate
     ```

4. Instalar las dependencias necesarias:
   ```bash
   pip install skyfield matplotlib numpy jupyter
   ```

5. Abrir `informe.ipynb`, seleccionar el entorno `.venv` como kernel y ejecutar todas las celdas con **Run All**.