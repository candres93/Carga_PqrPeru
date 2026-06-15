from config.conexion import establecer_conexion
from datetime import datetime


# ==========================================
# INSERTAR DATOS
# ==========================================
def truncar_tabla():

    conexion = establecer_conexion()
    cursor = conexion.cursor()

    cursor.execute("TRUNCATE TABLE [Dwh_VivaPeru].[Data_Peru].[His_Pqrs]")

    conexion.commit()

    cursor.close()
    conexion.close()

    print("Tabla truncada correctamente.")
    



def insertar_datos(df, table_name):

    batch_size = 3000
    total_rows = len(df)

    print(f"Intentando insertar un total de {total_rows} filas.")

    conexion = establecer_conexion()
    cursor = conexion.cursor()

    # 🔥 Optimización clave
    cursor.fast_executemany = True

    sql = f"""
    INSERT INTO {table_name}
    (
        PERIODO, ASEGURADOR, SEDE, CONTRATO, TIPO_CONTRATO,
        TIPO_DOCUMENTO, DOCUMENTO, PACIENTE, DIRECCION, TELEFONO,
        CORREO, RADICADO, COD_SUBASTA, PROCESO, VIA_RECEPCION,
        MOTIVO, SERVICIO, ESPECIALIDAD, FECHA_DEL_INCIDENTE,
        FECHA_DE_RESPUESTA, ESTADO, T_RESPUESTA, ESTADO_FINAL,
        HORAS_DIAS2, ESTADO_2, FECHA_SI, Fecha_Cargue
    )
    VALUES (
        ?,?,?,?,?,?,?,?,?,?,
        ?,?,?,?,?,?,?,?,?,?,
        ?,?,?,?,?,?,GETDATE()
    )
    """

    for start in range(0, total_rows, batch_size):

        end = min(start + batch_size, total_rows)
        batch = df.iloc[start:end].values.tolist()

        start_time = datetime.datetime.now()

        try:
            cursor.executemany(sql, batch)
            conexion.commit()

            end_time = datetime.datetime.now()
            duration = end_time - start_time

            print(f"Lote {start}-{end} insertado en {duration.total_seconds()}s")

        except Exception as e:
            print(f"Error en lote {start}-{end}: {str(e)}")
            conexion.rollback()
            return False

    cursor.close()
    conexion.close()

    print("Carga finalizada correctamente.")
    return True