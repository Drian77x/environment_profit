import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv 
import os

# CONFIGURACIÓN Y CONEXIÓN
load_dotenv() 

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
PROJECT_DB = os.getenv("PROJECT_DB") 

TABLE_NAME = "environmental_impact" 

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{PROJECT_DB}"

# CARGA DE DATOS (EJECUCIÓN DIRECTA)
if __name__ == "__main__":
    
    engine = create_engine(DATABASE_URL)
    
    # RUTA SIMPLE Y DIRECTA, basada en tu screenshot
    raw_data = pd.read_csv("final_raw_sample_0_percent.csv")
    
    # Limpieza de nombres de columnas
    raw_data.columns = raw_data.columns.str.lower().str.replace(' ', '_')
    
    # Cargar a PostgreSQL
    raw_data.to_sql(
        TABLE_NAME, 
        engine, 
        if_exists='replace',
        index=False,
        chunksize=1000
    )