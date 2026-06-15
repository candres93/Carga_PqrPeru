from app.lectura_xlsx import leer_excel
from config.insert import insertar_datos,truncar_tabla

table = '[Dwh_VivaPeru].[Data_Peru].[His_Pqrs]'

# ==========================================
# MAIN
# ==========================================

def main():

    # print("Leyendo archivo Excel...")

    df = leer_excel()
    
    print(f"Registros encontrados: {len(df)}")
    
    print("Truncando tabla...")
    truncar_tabla()
    
    print("Insertando data...")
    insertar_datos(df,table)

    print("Proceso finalizado correctamente.")

if __name__ == "__main__":
    main()