import psycopg2
import sys
from dotenv import load_dotenv 
import os

# Cargar variables desde .env (Seguridad y Modularidad)
load_dotenv()

# DETALLES DE CONEXIÓN
# Usamos 'postgres' como base de datos inicial para poder crear la nuestra.
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
PROJECT_DB = os.getenv("PROJECT_DB") # environment_profit

try:
    # 1. Conexión inicial al servidor (usando 'postgres' como DB temporal)
    conn = psycopg2.connect(
        dbname="postgres",
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )
    print(f"✅ Conexión al servidor Docker en puerto {DB_PORT} exitosa.")
    
    # 2. SOLUCIÓN: Habilitar autocommit para que CREATE DATABASE funcione
    conn.autocommit = True  

    with conn.cursor() as cursor:
        try:
            # 3. Crear la base de datos del proyecto
            cursor.execute(f"CREATE DATABASE {PROJECT_DB}")
            print(f"✅ Base de datos '{PROJECT_DB}' creada exitosamente.")
        except psycopg2.errors.DuplicateDatabase:
            print(f"✅ Base de datos '{PROJECT_DB}' ya existe. ¡El espacio de trabajo está listo!")
            
except Exception as e:
    print(f"❌ ERROR CRÍTICO al conectar o crear la DB: {e}")
    sys.exit(1)
finally:
    if 'conn' in locals() and conn:
        conn.close()