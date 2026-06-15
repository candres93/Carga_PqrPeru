import pyodbc

# Variables de acceso a la base de datos
server = '172.27.83.199\EVEREST_NEBI'
database = 'Stage_Area'
username = 'Dwhviva1a'
password = 'Viv@2023#*'

def establecer_conexion():
    connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    return pyodbc.connect(connection_string)
