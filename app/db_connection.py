import mysql.connector

# Datos de conexión
host = "localhost"
user = "root"
password = ""
dbname = "postcodes_db"


try:
    # Conexión a la base de datos
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=dbname
    )

    # Verifica si hay errores en la conexión
    if conn.is_connected():
        print("Conexión exitosa a la base de datos")

except mysql.connector.Error as e:
    print("Conexión fallida:", e)
finally:
    # Cerrar la conexión
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("Conexión cerrada")
