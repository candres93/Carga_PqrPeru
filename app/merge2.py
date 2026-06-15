import pandas as pd

# ==========================================
# CONFIGURACIÓN
# ==========================================

ARCHIVO_EXCEL = r"C:\Users\cguzman\Desktop\Carga_PqrPeru\data\tmp\RECLAMOS Y SOLICITUDES PERÚ.xlsx"
HOJA = "DATA CORREO"

# Excluir:
# 15 = DESCRIPCIÓN QUEJA
# 20 = RESPUESTA
USECOLS = [i for i in range(28) if i not in [15, 20]]


# ==========================================
# LEER EXCEL
# ==========================================

def leer_excel():

    df = pd.read_excel(
        ARCHIVO_EXCEL,
        sheet_name=HOJA,
        usecols=USECOLS,
        dtype=str
    )

    df = df.fillna("")

    df.columns = [
        "PERIODO",
        "ASEGURADOR",
        "SEDE",
        "CONTRATO",
        "TIPO_CONTRATO",
        "TIPO_DOCUMENTO",
        "DOCUMENTO",
        "PACIENTE",
        "DIRECCION",
        "TELEFONO",
        "CORREO",
        "RADICADO",
        "COD_SUBASTA",
        "PROCESO",
        "VIA_RECEPCION",
        "MOTIVO",
        "SERVICIO",
        "ESPECIALIDAD",
        "FECHA_DEL_INCIDENTE",
        "FECHA_DE_RESPUESTA",
        "ESTADO",
        "T_RESPUESTA",
        "ESTADO_FINAL",
        "HORAS_DIAS2",
        "ESTADO_2",
        "FECHA_SI"
    ]

    return df
